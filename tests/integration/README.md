## Overview
Tests an open3e process against an instance of [virtualE3](https://github.com/philippoo66/vitualE3). For canbus communication a [virtual](https://netmodule-linux.readthedocs.io/en/latest/howto/can.html#virtual-can-interface-vcan) can interface is used.



## How to tests run localy (linux)
### Prerequisities
* Linux host with [Docker Compose](https://docs.docker.com/compose/) installed (optional if you like to manage an mqtt broker and virtualE3 instance by your own).
* Loaded vcan kernel module (may be already installed/loaded depending on the used linux distribution).

### Create vcan interface

To create a virtual can interface for communitcation between a open3e and virtualE3.

```
modprobe vcan
```

```
ip link add dev vcan0 type vcan
ip link set vcan0 up
```

See also: [virtual-can-interface](https://netmodule-linux.readthedocs.io/en/latest/howto/can.html#virtual-can-interface-vcan)


### Start docker compose environment

The compose file manages a mqtt broker ([mosquitto](https://mosquitto.org/)) and an instance of [virtualE3](https://github.com/philippoo66/vitualE3).

```
cd /open3e/tests/integration
docker compose up -d
```

This starts the services detached. To inspect logs from the services use `docker compose logs -f`.

To start/stop the services without recreating the containers use `docker compose st(art|op)`.

To cleanup your docker containers/network use `docker compose down`.

### Execute the tests

```
cd /open3e
pip install .[dev]
pytest --cov=open3e tests/integration
```