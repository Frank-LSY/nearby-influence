#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:21:07 2018

@author: frank-lsy
"""

import matplotlib.pyplot as plt
import pandas as pd

ac = pd.read_csv("../12types-16-less/AC.csv")
ag = pd.read_csv("../12types-16-less/AG.csv")
at = pd.read_csv("../12types-16-less/AT.csv")
ca = pd.read_csv("../12types-16-less/CA.csv")
cg = pd.read_csv("../12types-16-less/CG.csv")
ct = pd.read_csv("../12types-16-less/CT.csv")
ga = pd.read_csv("../12types-16-less/GA.csv")
gc = pd.read_csv("../12types-16-less/GC.csv")
gt = pd.read_csv("../12types-16-less/GT.csv")
ta = pd.read_csv("../12types-16-less/TA.csv")
tc = pd.read_csv("../12types-16-less/TC.csv")
tg = pd.read_csv("../12types-16-less/TG.csv")

name_list = ac["Type"]
#ac_list = ac["Amount"]
#ag_list = ag["Amount"]
#at_list = at["Amount"]
ca_list = ca["Amount"]
cg_list = cg["Amount"]
ct_list = ct["Amount"]
#ga_list = ga["Amount"]
#gc_list = gc["Amount"]
#gt_list = gt["Amount"]
ta_list = ta["Amount"]
tc_list = tc["Amount"]
tg_list = tg["Amount"]


plt.xlabel("Left&Right-Base")
plt.ylabel("Amount")
#plt.bar(name_list,ac_list,label = "a-c",fc = "#008B8B")
#plt.bar(name_list,ag_list,bottom = ac_list,label = "a-g",fc = "#FFDAB9")
#plt.bar(name_list,at_list,bottom = ag_list,label = "a-t",fc = "#00FFFF")
plt.bar(name_list,ca_list,label = "c-a",fc = "#708090")
'''
plt.bar(name_list,cg_list,label = "c-g",fc = "#008B45")
plt.bar(name_list,ct_list,label = "c-t",fc = "#000080")
#plt.bar(name_list,ga_list,bottom = ct_list,label = "g-a",fc = "#FFFF00")
#plt.bar(name_list,gc_list,bottom = ga_list,label = "g-c",fc = "#6B8E23")
#plt.bar(name_list,gt_list,bottom = gc_list,label = "g-t",fc = "#8B658B")
plt.bar(name_list,ta_list,label = "t-a",fc = "#FF0000")
plt.bar(name_list,tc_list,label = "t-c",fc = "#EE82EE")
plt.bar(name_list,tg_list,label = "t-g",fc = "#FF7F00")
plt.legend()
#plt.savefig("../12-16.png",dpi = 2560)
plt.show()
'''