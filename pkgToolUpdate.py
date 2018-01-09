#-coding:utf-8-
import os
import re
files = os.listdir(os.getcwd())
#print(files)

for file in files:
    flag = False
    m = re.search('.sql', file)
    if m is not None:
        print(file)
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                str = re.search(' Pkg_Tool.', line)
                if str is not None:
                    flag = True
                    break
        f.close()
        if flag == True:
             with open(file, 'w', encoding='utf-8') as w:
                for n in lines:
                     w.write(n.replace(' Pkg_Tool.', ' ksfp.Pkg_Tool.'))
             w.close()

        with open(file, 'r', encoding='utf-8') as f2:
            lines2 = f2.readlines()

        f2.close()
        if flag == True:
             with open(file, 'w', encoding='utf-8') as w2:
                for n in lines2:
                    w2.write(n.replace(' p_Lg_Raise_Error', ' ksfp.p_Lg_Raise_Error'))

             w2.close()