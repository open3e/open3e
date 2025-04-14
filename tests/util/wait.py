import time

def wait_for(predicate, timeout=5):
  """Waits for a condition to be met within a timeout."""
  start_time = time.time()
  while not predicate():
    if time.time() - start_time > timeout:
        raise TimeoutError("Timeout waiting for condition")
    time.sleep(0.1)