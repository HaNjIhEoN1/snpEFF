import numpy as np
import pandas as pd

#parsing
data =[]
with open('output.vcf', 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        if line[0] == '#':
            pass
        else:
            if len(line.split('\t')) == 19:
                data.append(line.split('\n')[0].split('\t'))
            else:
                pass
              
test = pd.DataFrame(data)

# files by chromosomes
data =[]
with open('output.vcf', 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        if line[0] == '#':
            pass
        else:
            if line.split('\t') == chr#?
                data.append(line.split('\n')[0].split('\t'))
            else:
                pass

test$? = pd.DataFrame(data)
