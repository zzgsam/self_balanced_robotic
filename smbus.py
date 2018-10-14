#!/usr/bin/python

import smbus
import time

f = open("test","w")
bus = smbus.SMBus(1)
vol_sup=bus.read_i2c_block_data(0x48,0x00,2)
print >>f,"voltage read from i2c 0x%x" % (vol_sup[1])

f.close();
