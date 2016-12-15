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

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_VOLUME");
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
list_LiveTV_VOLUME = {1:'KEYCODE_VOLUME_UP',2:'KEYCODE_VOLUME_DOWN'}
while(i<=2):
	j=str(i)
	press=list_LiveTV_VOLUME[random.randint(1,2)]
	for r in range(2):
	 device.press(press,MonkeyDevice.DOWN_AND_UP)
	 MonkeyRunner.sleep(1)
	print press
	jietu = device.takeSnapshot()
	jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_VOLUME\\LiveTV_VOLUME'+j+'.png','png')
	i=i+1
i=1
while(i<=2):
	j=str(i)
	device.press('KEYCODE_VOLUME_MUTE',MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	print press
	jietu = device.takeSnapshot()
	jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_VOLUME\\KEYCODE_VOLUME_MUTE'+j+'.png','png')
	i=i+1
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
print "KEYCODE_BACK"
