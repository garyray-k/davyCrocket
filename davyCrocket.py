#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, os, csv, time, signal, sys, getpass, tempfile, datetime
import pyshark, numpy, serial

from subprocess import Popen

class davyCrocket(object):
    def __init__(self):
        print("init'd")

    @staticmethod
    def run():
        targetMAC = sys.argv[1]
        interfaces = [sys.argv[2], sys.argv[3]]
        targetChannel = sys.argv[4]

        rssiBufferSize = 50

        ser = serial.Serial(
            port='/dev/ttyACM0', 
            baudrate=9600, 
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
            )
        ser.isOpen()

        print('{+} Running davyCrocket Auto Wifi Tracker...')
        print('{+} Please ensure %s is set as the left antenna.' % interfaces[0])
        print('{+} Please ensure %s is set as the right antenna.' % interfaces[1])

        # camp the interfaces on desired channel
        davyCrocket.CampOnChannel(interfaces[0], targetChannel)
        davyCrocket.CampOnChannel(interfaces[1], targetChannel)
        
        try:
            # Until interrupted (Ctrl+C)
            print("{+} Working the target. Ctrl+C to quit")
            leftStream = RSSIstream(targetMAC, interfaces[0])
            rightStream = RSSIstream(targetMAC, interfaces[1])  
            leftRssis = []
            rightRssis = [] 
            start = time.time()
            left = leftStream.start("left stream")  
            right = rightStream.start("right stream")       
            while True:
                leftRssis.append(next(left))
                rightRssis.append(next(right))
                if(len(leftRssis) > rssiBufferSize and len(rightRssis) > rssiBufferSize):
                    avgLeft = numpy.mean(leftRssis)
                    avgRight = numpy.mean(rightRssis)
                    if (avgRight < avgLeft): # RSSI is in negative numbers, this means avgRight is a better signal than avgLeft
                        ser.write(b'r')
                        end = time.time()
                        print("{+} Took %s seconds." % (end-start))
                        print("{+} Move right.")
                    else:
                        ser.write(b'l')
                        end = time.time()
                        print("{+} Took %s seconds." % (end-start))
                        print("{+} Move left.")
                    leftRssis = leftRssis[(rssiBufferSize//2):]
                    rightRssis = rightRssis[(rssiBufferSize//2):]
        except KeyboardInterrupt:
            pass   
        except RuntimeError:
            print("Stopped running.")
            pass
        ser.close()
        leftStream.stop()
        rightStream.stop()
        print("{-} End of davyCrocket")   

    @staticmethod
    def CampOnChannel(interface, channel):
        channelCommand = ['iwconfig', interface, 'channel', channel]
        channelCamp = Popen(channelCommand)
        channelCamp.wait()

class RSSIstream(object):
    def __init__(self, bssid, interface):
        self.targetBssid = bssid
        self.wlanInterface = interface

    def start(self, streamName):
        displayFilter = 'wlan.sa=='+self.targetBssid
        self.tshark = pyshark.LiveCapture(interface=self.wlanInterface, display_filter=displayFilter)
        for packet in self.tshark.sniff_continuously():
            yield int(packet.wlan_radio.signal_dbm)

    def stop(self):
        self.tshark.close()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        raise Exception("Must use davyCrocket.py <tgtMAC> <leftAntennaInterface> <rightAntennaceInterface> <channelNumber>")
    davyCrocket.run()