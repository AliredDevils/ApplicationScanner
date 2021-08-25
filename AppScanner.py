#!/usr/bin/python3
# -*- coding:utf-8 -*-
import getopt
import sys
import os
from lib.apk import apkScan
from lib.ipa import ipaScan
from lib.tools import console

Version = 2.2


def printUse():
    console.print('''
    Usage:      
        python3 AppScanner.py -i *.apk/*.ipa
    
        -h help
        -i <inputPath>
        -s save cache (Default clear cache)
    ''', style='green')


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hsi:", ["ipath="])
    except getopt.GetoptError:
        printUse()
        sys.exit(2)

    save = False
    for (opt, arg) in opts:
        if opt == '-h':
            printUse()
            sys.exit()
        elif opt in ("-i", "--ipath"):
            inputfile = arg
        elif opt == '-s':
            save = True

    if len(inputfile) > 0:
        if not os.path.exists(inputfile):
            console.print('File not exist!', style='red bold')
            sys.exit(0)
        if '.apk' in inputfile:
            apkScan(inputfile, save)
        elif '.ipa' in inputfile:
            ipaScan(inputfile, save)
        else:
            console.print('Application must be *.apk or *.ipa', style='red bold')
            sys.exit(2)
    else:
        printUse()
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])
