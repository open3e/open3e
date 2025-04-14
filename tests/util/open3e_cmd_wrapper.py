import sys
import subprocess

from contextlib import contextmanager
from tests.util.wait import wait_for

OPEN3E_PROCESS_CMD = [sys.executable, "-m", "open3e.Open3Eclient"]
OPEN3E_DEFAULT_ARGUMENTS = ["-c", "vcan0"]

MQTT_BROKER_ADDRESS="127.0.0.1:1883"
MQTT_BASE_TOPIC="open3e"
MQTT_LISTEN_CMD_TOPIC=f"{MQTT_BASE_TOPIC}/cmnd"
MQTT_FORMAT_STRING="{ecuAddr:03X}_{didNumber:04d}"

def read(did):
  result = _run_open3e_process(["-r", did])
  return result.stdout, result.stderr


def write(did, value):
  result = _run_open3e_process(["-w", f"${did}=${value}"])
  return result.stdout, result.stderr


@contextmanager
def listen():
  try:
    process = _start_open3e_process_detached([
        "-l", MQTT_LISTEN_CMD_TOPIC,
        "-m", f"{MQTT_BROKER_ADDRESS}:{MQTT_BASE_TOPIC}",
        "-mfstr", f"{MQTT_FORMAT_STRING}"
      ]
    )
    yield process
  finally:
    # process.terminate()
    # TODO: workaround until SIGTERM handling in o3e is implemented
    process.send_signal(2)
    _wait_for_process_to_complete(process)


def _run_open3e_process(arguments):
  process_timeout = 10
  return subprocess.run(
    OPEN3E_PROCESS_CMD + OPEN3E_DEFAULT_ARGUMENTS + arguments,
    capture_output=True,
    check=True,
    text=True,
    timeout=process_timeout
  )

def _start_open3e_process_detached(arguments):
  return subprocess.Popen(
    OPEN3E_PROCESS_CMD + OPEN3E_DEFAULT_ARGUMENTS + arguments,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
  )


def _wait_for_process_to_complete(process):
  wait_for(lambda: process.poll() is not None)
  stdout, stderr = process.communicate(timeout=1)

  if process.poll() is None:
    process.kill()
    raise Exception(f"open3e process did not complete in time, process killed. stdout: {stdout}, stderr: {stderr}")

  if process.poll() != 0:
    raise Exception(f"open3e failed with exit code {process.poll()}. stdout: {stdout}, stderr: {stderr}")

  return stdout, stderr