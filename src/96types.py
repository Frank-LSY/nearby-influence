#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:09:51 2018

@author: frank-lsy
"""

count={'AA':0,'AC':0,'AG':0,'AT':0,
       'CA':0,'CC':0,'CG':0,'CT':0,
       'GA':0,'GC':0,'GG':0,'GT':0,
       'TA':0,'TC':0,'TG':0,'TT':0}

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

def seize_types(input_lr):
    #bases = []
    while 1:
        line = input_file.readline()
        if not line:
            input_file.close()
            break
        if (line[0]!='>'):
            count = input_lr()
            #time.sleep(2)
    return count 

func={'AA':aa,'AC':ac,'AG':ag,'AT':at,
      'CA':ca,'CC':cc,'CG':cg,'CT':ct,
      'GA':ga,'GC':gc,'GG':gg,'GT':gt,
      'TA':ta,'TC':tc,'TG':tg,'TT':tt}

def mut_ac(input_file):
    seize_types(input_file)
    
def mut_ag(input_file):
    seize_types(input_file)
    
def mut_at(input_file):
    seize_types(input_file)
    
def mut_ca(input_file):
    seize_types(input_file)

def mut_cg(input_file):
    seize_types(input_file)
    
def mut_ct(input_file):
    seize_types(input_file)
    
def mut_ga(input_file):
    seize_types(input_file)
    
def mut_gc(input_file):
    seize_types(input_file)
    
def mut_gt(input_file):
    seize_types(input_file)
    
def mut_ta(input_file):
    seize_types(input_file)
    
def mut_tc(input_file):
    seize_types(input_file)
    
def mut_tg(input_file):
    seize_types(input_file)

mutate={'AC':mut_ac,'AG':mut_ag,'AT':mut_at,
        'CA':mut_ca,'CG':mut_cg,'CT':mut_ct,
        'GA':mut_ga,'GC':mut_gc,'GT':mut_gt,
        'TA':mut_ta,'TC':mut_tc,'TG':mut_tg}



def quatre_vingt_seize_types(lr_file,snp_file):
    while 1:
        line = lr_file.readline()
        if not line:
            lr_file.close()
            break
        if (line[0]!='>'):
            input_lr = func[line[0].upper()+line[2].upper()]()
            #time.sleep(2)
    return count