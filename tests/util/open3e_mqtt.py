import json

import tests.util.open3e_cmd as open3e


class OnlineFlag:
    def __init__(self, flag):
        self.online = True if flag == "online" else False


class Open3EMqttClient:
    LWT_TOPIC = f"{open3e.MQTT_BASE_TOPIC}/LWT"

    def __init__(self, mqtt_client):
        self.received_messages = {}
        self.mqtt_client = mqtt_client
        self.online_flag = OnlineFlag("offline")
        self._setup()

    def _setup(self):
        self.mqtt_client.subscribe(self.LWT_TOPIC)

        def on_message(client, userdata, msg):
            if msg.topic == self.LWT_TOPIC:
                self.online_flag = OnlineFlag(msg.payload.decode())
            else:
                self.received_messages[msg.topic] = msg.payload.decode()

        self.mqtt_client.on_message = on_message

    def is_open3e_online(self):
        return self.online_flag.online

    def subscribe(self, ecu, did, did_topic_subpath=""):
        did_topic = self.__topic_name(ecu, did, did_topic_subpath)
        self.mqtt_client.subscribe(did_topic)

    def publish_cmd(self, mode, addr, data):
        cmd_payload = {"mode": mode, "addr": addr, "data": data}
        self.mqtt_client.publish(open3e.MQTT_LISTEN_CMD_TOPIC, json.dumps(cmd_payload))

    def received_messages_count(self):
        return len(self.received_messages)

    def received_message_payload(self, ecu, did, did_topic_subpath=""):
        did_topic = self.__topic_name(ecu, did, did_topic_subpath)
        return self.received_messages.get(did_topic, None)

    def __topic_name(self, ecu, did, topic_subpath):
        did_topic = open3e.MQTT_FORMAT_STRING.format(
            ecuAddr=int(ecu, 16),
            didNumber=did
            # TODO: to test mqtt string with did name, we must store the did name in the dataset, to build expected topic names
        )
        return f"{open3e.MQTT_BASE_TOPIC}/{did_topic}{topic_subpath}"
