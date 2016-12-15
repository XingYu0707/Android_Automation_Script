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

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\EPG");
device = MonkeyRunner.waitForConnection('192.168.0.200:65432')
i=1
x=0
#device.shell("logcat -v threadtime > /mnt/media_rw/usb0/zidonghua.log")
print "yi_you_log"
#shutil.rmtree("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\jietu")
#for d in ["F:\\java\\Android\\result\\qietai","F:\\java\\Android\\result\\home","F:\\java\\Android\\result\\dianbo"]:os.makedirs(d)#创建测试截图
#os.makedirs('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\jietu\\EPG')
#device.startActivity(component="com.topway.livetv.EntryActivity")#启动直播Activity
MonkeyRunner.sleep(3)
#device.press("KEYCODE_DPAD_UP",MonkeyDevice.DOWN_AND_UP)
#MonkeyRunner.sleep(5)
#device.press("KEYCODE_DPAD_UP",MonkeyDevice.DOWN_AND_UP)
#MonkeyRunner.sleep(5)
#device.press("KEYCODE_DPAD_CENTER", MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_MENU",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)

while(i<=4):
 MonkeyRunner.sleep(1)
 j=str(i)
 jietu = device.takeSnapshot()
 jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\EPG\\EPG-channel-type'+j+'.png','png')
 device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
 print "jietu-EPG-channel-type"+j
 i=i+1
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_RIGHT",MonkeyDevice.DOWN_AND_UP)
i=0
while(i<=7):
 MonkeyRunner.sleep(1)
 j=str(i)
 jietu = device.takeSnapshot()
 jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\EPG\\EPG-channel-list'+j+'.png','png')
 device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
 print "jietu-EPG-channel-list"+j
 i=i+1
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_LEFT",MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
device.press("KEYCODE_DPAD_LEFT",MonkeyDevice.DOWN_AND_UP)
i=0
while(i<=7):
 MonkeyRunner.sleep(1)
 j=str(i)
 jietu = device.takeSnapshot()
 jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\EPG\\EPG-channel-SevenDay'+j+'.png','png')
 device.press("KEYCODE_DPAD_DOWN",MonkeyDevice.DOWN_AND_UP)
 print "jietu-EPG-channel-SevenDay"+j
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