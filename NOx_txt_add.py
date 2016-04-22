# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 19:27:19 2015

@author: Eating
"""

import glob

# directory of o3 data
directory='/Users/Eating/Desktop/ChewsRidge/NOx/raw_data/BLC/'
directoryClean='/Users/Eating/Desktop/ChewsRidge/NOx/all_NOx/'

temp=directoryClean+'NOx_1027_1112.txt'
tmp=open(temp,'w+')
#with open(temp,'w+') as tmp:
#tmp.write('number sec CountsOnline CountsOffline DifCounts OnlinePower OfflinePower THG Signal1 Signal2 Pressure RoomTemp Col13 Col14\n')

      
files=glob.glob(directory+'*txt')
#print(files)
#input()  

for f in files:
    for line in open(f).readlines():
        #print line.rstrip()
        tmp.writelines(line)
      
    
    #for row in reader:
    #    try: 
    #        writer.writerow(row)
            #print('done')
    #    except:
    #        print('oops')

tmp.close()

print('DONE')