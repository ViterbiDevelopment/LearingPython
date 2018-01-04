
import os
import shutil

PROJECT_NAME = 'FLTv'
SRCROOT = '.'

FMK_NAME = PROJECT_NAME

INSTALL_DIR = '%s/Products/%s.framework' %(SRCROOT,PROJECT_NAME)

WRK_DIR = './build'

DEVICE_DIR = '%s/Release-iphoneos/%s.framework' % (WRK_DIR,FMK_NAME)
SIMULATOR_DIR = '%s/Release-iphonesimulator/%s.framework' % (WRK_DIR,FMK_NAME)

IPHONEOS_CMD = 'xcodebuild -project %s.xcodeproj -configuration "Release" -target %s -sdk iphoneos clean build' % (PROJECT_NAME,FMK_NAME)
IPHONESIMULATOR_CMD = 'xcodebuild -project %s.xcodeproj -configuration "Release" -target %s -sdk iphonesimulator clean build' % (PROJECT_NAME,FMK_NAME)

os.system(IPHONEOS_CMD)
os.system(IPHONESIMULATOR_CMD)

if os.path.exists(INSTALL_DIR):
	shutil.rmtree(INSTALL_DIR)
	pass

shutil.copytree(DEVICE_DIR + '/',INSTALL_DIR + '/')

LIPOCREATE_CMD = 'lipo -create "%s/%s" "%s/%s" -output "%s/%s"' % (DEVICE_DIR,FMK_NAME,SIMULATOR_DIR,FMK_NAME,INSTALL_DIR,FMK_NAME)
os.system(LIPOCREATE_CMD)

shutil.rmtree(WRK_DIR)

