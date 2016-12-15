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

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_ChannelList");
device = MonkeyRunner.waitForConnection('192.168.0.200:65432')
i=1
x=0
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
list_UP_DOWN = {1:'KEYCODE_DPAD_DOWN',2:'KEYCODE_DPAD_UP'}
list_RIGHT_LEFT = {1:'KEYCODE_DPAD_RIGHT',2:'KEYCODE_DPAD_LEFT'}
MonkeyRunner.sleep(3)
while(i<=10):
	j=str(i)	
	device.press('KEYCODE_DPAD_RIGHT',MonkeyDevice.DOWN_AND_UP)
	press=list_UP_DOWN[random.randint(1,2)]
	for r1 in range(7):
	 device.press(press,MonkeyDevice.DOWN_AND_UP)
	 MonkeyRunner.sleep(1)
	print press
	jietu = device.takeSnapshot()
	jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_ChannelList\\'+j+'LiveTV_ChannelList_ChangeChannel.png','png')
	press=list_RIGHT_LEFT[random.randint(1,2)]
	for r2 in range(7):
	 device.press(press,MonkeyDevice.DOWN_AND_UP)
	 MonkeyRunner.sleep(1)
	 jietu = device.takeSnapshot()
	 jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_ChannelList\\'+j+'LiveTV_ChannelList_ChangeList.png','png')
	MonkeyRunner.sleep(1)
	device.press("KEYCODE_DPAD_CENTER",MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	jietu = device.takeSnapshot()
	jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_ChannelList\\'+j+'LiveTV_ChannelList_Center.png','png')
	i=i+1
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
print "KEYCODE_BACK"

