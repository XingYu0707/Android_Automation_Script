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

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime");
device = MonkeyRunner.waitForConnection('192.168.0.200:65432')
i=1
x=0
print "yi_you_log"
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
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime1.png','png')
MonkeyRunner.sleep(1)
while(i<=3):
	device.press("KEYCODE_1",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	device.press("KEYCODE_1",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	i=i+1
i=1
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
while(i<=2):
	device.press("KEYCODE_DPAD_LEFT",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	device.press("KEYCODE_2",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	device.press("KEYCODE_2",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	i=i+1
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime2.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime3.png','png')
MonkeyRunner.sleep(1)
i=1
while(i<=6):
	device.press("KEYCODE_0",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	i=i+1
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime4.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime5.png','png')
MonkeyRunner.sleep(2)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime6.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_LEFT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
jietu = device.takeSnapshot()
jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\CAWorkTime\\CAWorkTime7.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
i=1
while(i<=6):
	device.press("KEYCODE_0",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	i=i+1
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
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