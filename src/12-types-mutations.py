#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:46:45 2018

@author: frank-lsy
"""

import re
import csv
import time

def ac(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)

def ag(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def at(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def ca(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def cg(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def ct(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def ga(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def gc(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def gt(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def ta(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def tc(row, output_file):
    head = 'Chromosome,Start_Position,End_Position,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)
    
def tg(row, output_file):
    head = 'Chromosome\tStart_Position\tEnd_Position\tReference_Allele\tTumor_Seq_Allele1\tTumor_Seq_Allele2\n'
    g = open(output_file,'a+')
    #g.writelines(head)
    g.writelines(row)

func={'AC':ac,'AG':ag,'AT':at,
      'CA':ca,'CG':cg,'CT':ct,
      'GA':ga,'GC':gc,'GT':gt,
      'TA':ta,'TC':tc,'TG':tg}

def extract(input_file,output_dir):
    f = open(input_file,'r')
    reader = csv.reader(f)
    for row in reader:
        row_comma = []
        for item in row:
            row_comma.append(item+',')
        #print(row)
        #time.sleep(2)
        row_comma += '\n' 
        print(row)
        if(row[4]==row[3]):
            output_file = "{0}/{1}.csv".format(output_dir,row[3]+row[5])
            func[row[3]+row[5]](row_comma,output_file)
        else:
            output_file = "{0}/{1}.csv".format(output_dir,row[3]+row[4])
            func[row[3]+row[4]](row_comma,output_file)            
        
        
input_file = "../dataset/SNP-only-chr.csv"
output_dir = "../12types-raw"
extract(input_file,output_dir)