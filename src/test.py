#!/usr/bin/python

import os,sys,json,re,shutil

def main(compo,testtype):
    print('compo:%s testtype:%s' % (compo, testtype))

if __name__ == '__main__':

    #メイン処理
    main(sys.argv[1],sys.argv[2])
