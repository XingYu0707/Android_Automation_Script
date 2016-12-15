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

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\HOMEVOD");
device = MonkeyRunner.waitForConnection('192.168.0.200:65432')
i=1
x=0
print "yi_you_log"
MonkeyRunner.sleep(3)
device.press("KEYCODE_HOME",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
jietu1 = device.takeSnapshot()
jietu1.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\HOMEVOD\\HOMEVOD.png','png')
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
print "jietu1"
jietu1 = device.takeSnapshot()
jietu1.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\HOMEVOD\\HOMEVOD01.png','png')
print "HOMEVOD"
list_UP_DOWN = {1:'KEYCODE_DPAD_DOWN',2:'KEYCODE_DPAD_UP'}
list_RIGHT_LEFT = {1:'KEYCODE_DPAD_RIGHT',2:'KEYCODE_DPAD_LEFT'}
while(i<=10):
 MonkeyRunner.sleep(1)
 if i%5==0:
  #print "i%5"+str(i%5)
  press=list_UP_DOWN[1]
  device.press(press,MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(1)
  device.press(press,MonkeyDevice.DOWN_AND_UP)
  MonkeyRunner.sleep(1)
 j=str(i)
 press=list_UP_DOWN[random.randint(1,2)]
 device.press(press,MonkeyDevice.DOWN_AND_UP)
 #print press
 press=list_RIGHT_LEFT[random.randint(1,2)]
 for r in range(5):
  MonkeyRunner.sleep(1)
  device.press(press,MonkeyDevice.DOWN_AND_UP)
  #print "r="+str(r)
 #print press
 jietu = device.takeSnapshot()
 jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\HOMEVOD\\HOMEVOD'+j+'.png','png')
 print "HOMEVOD"+j
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
