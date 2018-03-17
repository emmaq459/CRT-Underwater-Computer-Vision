'''Generate parent classes give a list of orignial classes from training data
and a map of which child classes correspond to which parent classes. Modifies
the file in place'''

import glob
import os

# path of orignial training files
path = ''

# dictionary of child to parent classes (<child classes>): <parent class>
d = {(0, 1): 3, (2,): 4}

for filename in glob.glob(os.path.join(path, '*.txt')):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    with open(filename, 'a') as f:
        for line in lines:
            if len(line) != 0:
                clss = int(line.split()[0])
                for i in d.keys():
                    if clss in i:
                        new_clss = d[i]
                        f.write('\n' + str(d[i]) + line[1:])
