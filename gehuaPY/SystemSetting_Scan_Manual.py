#coding:utf-8
import shutil
import os
from com.android.monkeyrunner import MonkeyRunner,MonkeyImage,MonkeyDevice

def directory_exists(filepath):
    if os.path.exists(filepath):
     message = 'OK, the "%s" file exists.'
    else:
     message = 'Sorry, I cannot find the "%s" file.Now mkdir'
     os.mkdir(filepath)
    print message % filepath

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\SCAN");
device = MonkeyRunner.waitForConnection('192.168.0.200:65432')
i=1
x=0
print "yi_you_log"
MonkeyRunner.sleep(3)
device.press("KEYCODE_MENU",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
print "KEYCODE_DPAD_CENTER"
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
print "KEYCODE_BACK"
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\SCAN\\Manual.png','png')
print "jietu-Manual"
while(i<=2):
 MonkeyRunner.sleep(1)
 j=str(i)
 jietu = device.takeSnapshot()
 jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\SCAN\\Manual'+j+'.png','png')
 print "jietu-Manual"+j
 i=i+1
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
print "KEYCODE_BACK"

