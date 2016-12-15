#coding:utf-8
import shutil
import os
from com.android.monkeyrunner import MonkeyRunner,MonkeyImage,MonkeyDevice
device = MonkeyRunner.waitForConnection('192.168.0.200:65432')

device.press("KEYCODE_PROG_RED",MonkeyDevice.DOWN_AND_UP)
print "KEYCODE_PROG_RED "