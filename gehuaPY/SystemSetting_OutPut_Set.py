#coding:utf-8
import shutil
import os,random
from com.android.monkeyrunner import MonkeyRunner,MonkeyImage,MonkeyDevice

def directory_exists(filepath):
    if os.path.exists(filepath):
     message = 'OK, the "%s" file exists.'
    else:
     message = 'Sorry, I cannot find the "%s" file.Now mkdir'
     os.mkdir(filepath)
    print message % filepath

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\OutPutSet");
device = MonkeyRunner.waitForConnection('192.168.0.200:65432')
i=1
x=0
print "yi_you_log"
list = {1:'KEYCODE_DPAD_RIGHT',2:'KEYCODE_DPAD_LEFT'}
MonkeyRunner.sleep(3)
device.press("KEYCODE_MENU",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\OutPutSet\\OutPutSet1.png','png')
MonkeyRunner.sleep(2)
device.press(list[random.randint(1,2)],MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press(list[random.randint(1,2)],MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press(list[random.randint(1,2)],MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\OutPutSet\\OutPutSet2.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\OutPutSet\\OutPutSet3.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\OutPutSet\\OutPutSet4.png','png')
print "jietu-OutPutSet"
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