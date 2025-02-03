from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector
import udsoncan
#from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *

from can.interface import Bus
from udsoncan.connections import PythonIsoTpConnection
from can.interfaces.socketcan import SocketcanBus
from can.interfaces.slcan import slcanBus
import isotp

from isotp.protocol.transceiver import NotifierBasedCanStack
from isotp.notifier import Notifier, Listener

import open3e.Open3Eclass
from open3e.Open3EudsClient import Open3EudsClient

# Erstelle einen einfachen Listener
class MyListener(Listener):
    def on_message_received(self, frame):
        print(f"Frame received: {frame}")


SLCANBUS = None

def create_o3eclass_instance(ecutx:int, doip, can, slcan, dev) -> open3e.Open3Eclass.O3Eclass:
    global SLCANBUS
    conn = None
    ecurx = ecutx + 0x10

    # select CAN / DoIP ~~~~~~~~~~~~~~~~~~
    if(doip != None): #DoIP
        conn = DoIPClientUDSConnector(DoIPClient(doip, ecutx))
    elif(slcan != None): #SLCAN Serial CAN Interface either locally via USB or remote via Telnet
        # Reuse global slcanbus instance for all instances of O3Eclass because COM port can not be bound multiple times
        if(SLCANBUS is None):
            print(f"Creating new SLCANBUS Instance for ECU: {ecutx:03x}")
            bus = slcanBus(channel=slcan, tty_baudrate=115200, bitrate=250000)
            SLCANBUS = bus
        else:
            print(f"Reusing SLCANBUS Instance for ECU: {ecutx:03x}" )
            bus = SLCANBUS

        tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx) # Network layer addressing scheme
        stack = isotp.CanStack(bus=bus, address=tp_addr, params=isotp_params())               # Network/Transport layer (IsoTP protocol)
        stack.set_sleep_timing(0.01, 0.01)                                                  # Balancing speed and load
        conn = PythonIsoTpConnection(stack)   

        # # mit NotifierBasedCanStack
        # tp_addr = isotp.Address(addressing_mode=isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx)
        # # Erstelle den Listener
        # my_listener = MyListener()
        # # Erstelle den Notifier mit dem Listener
        # notifier = Notifier(bus, [my_listener])        
        # # Erstelle den Notifier-basierten IsoTP-Stack
        # stack = NotifierBasedCanStack(bus=bus, notifier=notifier, address=tp_addr, params=isotp_params())
        # # Füge den Stack als Listener hinzu
        # notifier.add_listener(stack)
        # stack.set_sleep_timing(0.01, 0.01)
        # conn = PythonIsoTpConnection(stack)

    else:
        bus = SocketcanBus(channel=can, bitrate=250000)                                     # Link Layer (CAN protocol)
        tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=ecutx, rxid=ecurx) # Network layer addressing scheme
        stack = isotp.CanStack(bus=bus, address=tp_addr, params=isotp_params())               # Network/Transport layer (IsoTP protocol)
        stack.set_sleep_timing(0.01, 0.01)                                                  # Balancing speed and load
        conn = PythonIsoTpConnection(stack)                                            # interface between Application and Transport layer

    # now the class +++++++++++++++++++++++
    return open3e.Open3Eclass.O3Eclass(conn, ecutx, ecurx, dev)



def isotp_params():
    # Refer to isotp documentation for full details about parameters
    return {
        'stmin': 10,                            # Will request the sender to wait 10ms between consecutive frame. 0-127ms or 100-900ns with values from 0xF1-0xF9
        'blocksize': 0,                         # Request the sender to send 8 consecutives frames before sending a new flow control message
        'wftmax': 0,                            # Number of wait frame allowed before triggering an error
        'tx_data_length': 8,                    # Link layer (CAN layer) works with 8 byte payload (CAN 2.0)
        'tx_data_min_length': 8,                # Minimum length of CAN messages. When different from None, messages are padded to meet this length. Works with CAN 2.0 and CAN FD.
        'tx_padding': 0,                        # Will pad all transmitted CAN messages with byte 0x00.
        'rx_flowcontrol_timeout': 1000,         # Triggers a timeout if a flow control is awaited for more than 1000 milliseconds
        'rx_consecutive_frame_timeout': 1000,   # Triggers a timeout if a consecutive frame is awaited for more than 1000 milliseconds
        'override_receiver_stmin': None,        # When sending, respect the stmin requirement of the receiver if set to None.
        'max_frame_size': 4095,                 # Limit the size of receive frame.
        'can_fd': False,                        # Does not set the can_fd flag on the output CAN messages
        'bitrate_switch': False,                # Does not set the bitrate_switch flag on the output CAN messages
        'rate_limit_enable': False,             # Disable the rate limiter
        'rate_limit_max_bitrate': 1000000,      # Ignored when rate_limit_enable=False. Sets the max bitrate when rate_limit_enable=True
        'rate_limit_window_size': 0.2,          # Ignored when rate_limit_enable=False. Sets the averaging window size for bitrate calculation when rate_limit_enable=True
        'listen_mode': False                    # Does not use the listen_mode which prevent transmission.
    }

def close():
    global SLCANBUS
    if(SLCANBUS is not None):
        SLCANBUS.shutdown()
    # ggf anderes schliessen?!


