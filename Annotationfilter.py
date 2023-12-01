import numpy as np
import pandas as pd

with open('input.vcf')as f:
    with open('filtered.vcf','w')as w:
        while True:
            line = f.readline()
            if not line:break
            else:
                if line[0] == '#':
                    w.write(line)
                else:
                    if line.split('\t')[7].split('|')[1] == 'intergenic_region' or line.split('\t')[7].split('|')[1] == 'upstream_gene_variant' or line.split('\t')[7].split('|')[1] == 'downstream_gene_variant':
                        pass
                    else :
                        w.write("\t".join(line.split('\t')[0:7]) + "\t" + line.split('\t')[7].split('|')[0] + "\t" + "\t".join(line.split('\t')[8:])) 
