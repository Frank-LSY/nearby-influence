#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:56:45 2018

@author: frank-lsy
"""


import csv
import time
import os

ori_dir = "../12types-raw"
files = os.listdir(ori_dir)
print(files)

def mid(input_file,output_file):
    #print (input_file)
    reader = csv.reader(input_file)
    for item in reader:
        #print(len(item))
        chro = item[0]
        pos = item[1]
        tmp = chro+':'+str((int(pos)-1))+'-'+str((int(pos)+1))+'\n'
        #print(tmp)
        output_file.write(tmp)

for file in files:
    ori_file = open("{0}/{1}".format(ori_dir,file),"r")
    out_file = open("../12types-mid/{}".format(file),"a+")
    mid(ori_file,out_file)
    ori_file.close()
    out_file.close()