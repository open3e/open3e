# open3e-docker
open3e on Docker

This repository contains the Dockerfiles for running open3e in a Docker container. It is split into a container image for the command open3e_depictSystem and open3e. To keep the images as minimal as possible they are based on the official Python Alpine images.

Before running the container images you should follow the best practices to peristently map the CAN adapter: https://github.com/open3e/open3e/blob/master/bestPractices/USB%20Adapter%20and%20udev.md 

For initially creating the devices.json and the Open3Edatapoints you run the open3depict image:

`sudo docker run -d --name open3edepict --network host -e CLI_ARGS="-c can0" -v ./data:/open3e fleckem/open3e-depict`

- Network Host is needed, so the container can interact with the CAN-Interface
- CLI_ARGS is used to handover the open3e_depictSystem CLI_ARGS (e.g. naming of the CAN-Interface)
- mapping a local volume on the host (e.g. ./data) to have the devices.json and the Open3Edatapoints persistantly stored
- the image name need to be adjusted if it is your own build

After the container has run you need to remove the exited container with `sudo docker rm CONTAINER__ID`

When open3e_depictSystem is finished you need to create an args file within ./data on your host machine. It is important that the file is named "args" without any file extention. You can refer to the args file in the main repository as reference https://github.com/open3e/open3e/blob/master/args

When the args file is complete simply start the container and you are able to interact with it through MQTT which is configured in the args file.

Example of a simple docker compose file for running open3e in Docker:

```
services:
  open3e:
    container_name: open3e
    image: "fleckem/open3e"
	network_mode: "host"
    volumes:
      - "./data/:/open3e/"
    restart: always
```

There are Raspberry Pi 4 images available on docker hub `docker pull fleckem/open3e` and `docker pull fleckem/open3e-depict` Please note: this is only an ARM64 image and tested on the Raspberry Pi 4. It might work on other ARM64 based systems.
