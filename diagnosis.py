#!/usr/bin/env/ python
#Written by Martijn "de clown"Rombouts 17/8/2017
#
#Quick Data logger.
#

import usb
import time
import datetime
import serial
import socket
import serial.tools.list_ports
import urllib
#
#PORT = "/dev/ttyUSB1"
#port = serial.Serial(PORT, baudrate=9600, timeout=3.0)     #serial port settings
REMOTE_SERVER = "www.google.com"



def filewrite(rcv):                             #Function to write data to a .txt file
        logfile = open("USB_Devices2.txt", "a")      #open file
        logfile.write(rcv)                      #write line in file
        logfile.close                           #close file
i = 0



while i < 20:
        time.sleep(2)
        busses = usb.busses()
        filewrite("---------------" + str(i) + "\n")
        print(datetime.datetime.now())
        try:
                stri = "https://www.google.co.in"
                data = urllib.urlopen(stri)
                #host = socket.create_connections(("www.google.com", 80))
                filewrite("socket met google gelukt" + "\n")
        except Exception as e:
                filewrite("ethernet " + str(e) + "\n")
        try:
                port = list(serial.tools.list_ports.grep("09d7:0100"))[1][0]
                filewrite("Port is: " + str(port))
                rcv = port.readline()                   #rvc is the serial data received
                print("received " + repr(rcv) + "\n")           #show the data in terminal
                filewrite(rcv)                          #use function filewrite to put serial data in file
        except Exception as e:
                port = 0
                filewrite("serialpoort " + str(e) + "\n")
        filewrite(str(datetime.datetime.now()) + "\n")

        for bus in busses:
                devices = bus.devices
                for dev in devices:
                        print "Device:", dev.filename
                        filewrite("Device \n")
                        print " idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor)
                        filewrite("ID Vendor: " + hex(dev.idVendor) + "\n")
                        print " idProduct: %d (0x%04x) " % (dev.idProduct, dev.idProduct)
                        filewrite("ID Product: " + hex(dev.idProduct) + "\n")
        i += 1

