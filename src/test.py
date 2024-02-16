#!/usr/bin/python

import os,sys,json,re,shutil

def main(compo,testtype):
    print("compo:{} testtype:{}".format(compo, testtype))

　　f = open('myfile.txt', 'w')
　　f.write("compo:{} testtype:{}".format(compo, testtype))
　　f.close()

if __name__ == '__main__':

    #メイン処理
    main(sys.argv[1],sys.argv[2])
