# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:02:53 2015

@author: Yiting
"""
def chewsmet_txt(path,title):
    
    import pandas

    metdf=pandas.load(path+title+'.df')
    # open all file end with .df
#metdf=pandas.load('/Users/Eating/Documents/ATM_R/python program/20150615_7.df')
#print metdf['Wdir'][-1]
#raw_input()
#print metdf.index

#raw_input()
    metdfFile=open(path+title+'.txt','w')
#metdfFile=open('/Users/Eating/Documents/ATM_R/python program/20150615_7.txt','w')

    metdfFile.write('Date_Time, Wind Speed, Wind Dir, Temperature, WaterPress, Humidity\n ')
    for i in range(0,len(metdf.index)):
    ##print metdf['Wdir'][i]
    #print metdf['Wspd'][i]

         metdfFile.write(str(metdf.index[i])+', '+str(metdf['Wspd'][i])+', '+str(metdf['Wdir'][i])+','+str(metdf['temp'][i])+','+str(metdf['H20Pres'][i])+','+str(metdf['humidity'][i])+'\n')
    
    #raw_input()
    metdfFile.close()  
  
    print('done')

chewsmet_txt('/Users/Eating/Documents/ATM_R/python program/','20150615_30_h')