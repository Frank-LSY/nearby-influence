#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:27:28 2018

@author: frank-lsy
"""
import time
import csv
import os

def seize_types(input_file):
    count={'AA':0,'AC':0,'AG':0,'AT':0,
       'CA':0,'CC':0,'CG':0,'CT':0,
       'GA':0,'GC':0,'GG':0,'GT':0,
       'TA':0,'TC':0,'TG':0,'TT':0}
    #print(count)
    
    def aa():
        count['AA'] += 1
        return count

    def ac():
        count['AC'] += 1
        return count

    def ag():
        count['AG'] += 1
        return count

    def at():
        count['AT'] += 1
        return count

    def ca():
        count['CA'] += 1
        return count

    def cc():
        count['CC'] += 1
        return count

    def cg():
        count['CG'] += 1
        return count

    def ct():
        count['CT'] += 1
        return count

    def ga():
        count['GA'] += 1
        return count

    def gc():
        count['GC'] += 1
        return count

    def gg():
        count['GG'] += 1
        return count

    def gt():
        count['GT'] += 1
        return count

    def ta():
        count['TA'] += 1
        return count

    def tc():
        count['TC'] += 1
        return count

    def tg():
        count['TG'] += 1
        return count

    def tt():
        count['TT'] += 1
        return count
    
    func={'AA':aa,'AC':ac,'AG':ag,'AT':at,
      'CA':ca,'CC':cc,'CG':cg,'CT':ct,
      'GA':ga,'GC':gc,'GG':gg,'GT':gt,
      'TA':ta,'TC':tc,'TG':tg,'TT':tt}
    
    while 1:
        line = input_file.readline()
        if not line:
            input_file.close()
            break
        if (line[0]!='>'):
            count = func[line[0].upper()+line[2].upper()]()
            #time.sleep(2)
    return count        


ori_dir = "../12types-lr"
dest_dir = "../12types-16-less/"
files = os.listdir(ori_dir)
for file in files:
    print(file)
    f = open("{0}/{1}".format(ori_dir,file),'r')
    end = seize_types(f)
    g = open("{0}/{1}".format(dest_dir,file),'a+')
    g.writelines("Type,Amount\n")
    for key,value in end.items():
        #print(key,value)
        #time.sleep(0.1)
        g.writelines(key+','+str(value)+'\n')
    g.close()
    #print(end)