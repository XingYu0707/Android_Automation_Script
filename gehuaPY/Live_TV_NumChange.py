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

directory_exists("F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_NumChange");
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
list_First_Num = {0:'KEYCODE_0',1:'KEYCODE_1',2:'KEYCODE_6'}
list_Num = {0:'KEYCODE_0',1:'KEYCODE_1',2:'KEYCODE_2',3:'KEYCODE_3',4:'KEYCODE_4',5:'KEYCODE_5',6:'KEYCODE_6',7:'KEYCODE_7',8:'KEYCODE_8',9:'KEYCODE_9'}
MonkeyRunner.sleep(3)
while(i<=10):
	j=str(i)
	press=list_First_Num[random.randint(0,2)]
	device.press(press,MonkeyDevice.DOWN_AND_UP)
	for r1 in range(2):
	 press=list_Num[random.randint(0,9)]
	 device.press(press,MonkeyDevice.DOWN_AND_UP)
	 MonkeyRunner.sleep(0.2)
	print press
	jietu = device.takeSnapshot()
	jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_NumChange\\'+j+'LiveTV_NumChange.png','png')
	MonkeyRunner.sleep(5)
	device.press('KEYCODE_PROG_RED',MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	jietu = device.takeSnapshot()
	jietu.writeToFile('F:\\java\\Android\\adt-bundle-windows-x86_64-20140702\\sdk\\tools\\gehuajietu\\LiveTV_NumChange\\'+j+'LiveTV_NumChange.png','png')
	MonkeyRunner.sleep(1)
	device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
	i=i+1
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
device.press("KEYCODE_BACK",MonkeyDevice.DOWN_AND_UP)
print "KEYCODE_BACK"
