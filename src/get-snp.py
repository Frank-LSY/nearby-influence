#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:17:01 2018

@author: frank-lsy
"""
import re

def extract(input_file,output_file):
    head = 'Hugo_Symbol	Entrez_Gene_Id	Center	NCBI_Build	Chromosome	Start_Position	End_Position	Strand	Variant_Classification	Variant_Type	Reference_Allele	Tumor_Seq_Allele1	Tumor_Seq_Allele2	dbSNP_RS	dbSNP_Val_Status	Tumor_Sample_Barcode	Matched_Norm_Sample_Barcode	Match_Norm_Seq_Allele1	Match_Norm_Seq_Allele2	Tumor_Validation_Allele1	Tumor_Validation_Allele2	Match_Norm_Validation_Allele1	Match_Norm_Validation_Allele2	Verification_Status	Validation_Status	Mutation_Status	Sequencing_Phase	Sequence_Source	Validation_Method	Score	BAM_File	Sequencer	Tumor_Sample_UUID	Matched_Norm_Sample_UUID	HGVSc	HGVSp	HGVSp_Short	Transcript_ID	Exon_Number	t_depth	t_ref_count	t_alt_count	n_depth	n_ref_count	n_alt_count	all_effects	Allele	Gene	Feature	Feature_type	One_Consequence	Consequence	cDNA_position	CDS_position	Protein_position	Amino_acids	Codons	Existing_variation	ALLELE_NUM	DISTANCE	TRANSCRIPT_STRAND	SYMBOL	SYMBOL_SOURCE	HGNC_ID	BIOTYPE	CANONICAL	CCDS	ENSP	SWISSPROT	TREMBL	UNIPARC	RefSeq	SIFT	PolyPhen	EXON	INTRON	DOMAINS	GMAF	AFR_MAF	AMR_MAF	ASN_MAF	EAS_MAF	EUR_MAF	SAS_MAF	AA_MAF	EA_MAF	CLIN_SIG	SOMATIC	PUBMED	MOTIF_NAME	MOTIF_POS	HIGH_INF_POS	MOTIF_SCORE_CHANGE	IMPACT	PICK	VARIANT_CLASS	TSL	HGVS_OFFSET	PHENO	MINIMISED	ExAC_AF	ExAC_AF_Adj	ExAC_AF_AFR	ExAC_AF_AMR	ExAC_AF_EAS	ExAC_AF_FIN	ExAC_AF_NFE	ExAC_AF_OTH	ExAC_AF_SAS	GENE_PHENO	FILTER	CONTEXT	src_vcf_id	tumor_bam_uuid	normal_bam_uuid	case_id	GDC_FILTER	COSMIC	MC3_Overlap	GDC_Validation_Status\n'
    f = open(input_file,'r')
    g = open(output_file,'a+')
    g.writelines(head)
    while 1:
        line = f.readline()
        t = re.findall(r'SNP',line)
        if (t):
            g.writelines(line)
        if not line:
            break
    f.close()
    g.close()
    
    
extract("../dataset/mutect.maf","../dataset/SNP-only.maf")