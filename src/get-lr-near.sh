#!/bin/bash

function lr ()
{
	mkdir -pv "../12types-lr/"
	for file in `ls $1`
	do 
		echo $1"/"$file
		dir=$1"/"`basename $file`
		for line in `cat $dir`
		do 
			echo $line
			samtools faidx ../dataset/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa $line >> ../12types-lr/`basename $file`
		done
	done
}

folder="../12types-mid"
lr $folder



