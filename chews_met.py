# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 16:24:12 2015

@author: Andy,Max,Yiting
"""

#chews_met: Use this function to retrieve Chews ridge met data from the weatherunderground site.  Spits out a pandas dataframe with utc time as index, and pst time as 'pst'.
    #Use:  met = chews_met(1, 1, 2012, 365)  would yield dataframe with met data for 2012
def chews_met(startmonth, startday, startyear, dayspan,title,path):
    import os
    import urllib2
    import tempfile
    import csv
    import numpy
    import pandas
    import time
    import datetime
    import pytz
    print 'DOWNLOADING WEATHER DATA...\n'
    
    
    #urlString='http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KCACARME1&day='+str(startday)+'&year='+str(startyear)+'&month='+str(startmonth)+'&graphspan=day&format=1'
    #print urlString
    #raw_input()
    #url = urllib2.urlopen(urlString)
    #urlread = url.read()
    temp = path+'/temp.txt'
    fout = open(temp,'w+')
    

    for i in numpy.arange(0,dayspan):
        print 'Day # '+str(1+i)
        url = urllib2.urlopen ('http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KCACARME1&day='+str(startday+i)+'&year='+str(startyear)+'&month='+str(startmonth)+'&graphspan=day&format=1')
        #print url 
        #raw_input()
        for row in url:
            
            fout.write(row) 
                      
    fout.close()

    reader, writer = csv.reader(open(temp)),csv.writer(open(temp[:-4]+'cleaned.txt', 'wb')) 
    for row in reader:
        
        try:
            if (row[0].startswith('2') and len(row[0])==19):
                if row[-3].startswith('d'):
                    writer.writerow(row)
        except IndexError:
            print 'SKIPPED ROW: '+str(row)
            #raw_input()
            pass

            
    #metdf = pandas.io.parsers.read_csv(temp[:-4]+'cleaned.txt', converters = {0: chewsmet_converter}, delimiter=',', names=['Time(Epoch)', 'Temp(F)', 'Dewpnt(F)', 'Press(In)', 'Windirnull', 'Wdir', 'Wspd(mph)', 'Wspdgust(mph)NA', 'Humidity', 'HrlyPrecip(In)', 'ConditionsNA', 'CloudsNA', 'dailyrain(In)', 'SoftwareTypeNA', 'DateUTCNA', 'NA'])    
    metdf = pandas.io.parsers.read_csv(temp[:-4]+'cleaned.txt', delimiter=',', names=['DateTimeUTC', 'Temp(F)', 'Dewpnt(F)', 'Press(In)', 'Windirnull', 'Wdir', 'Wspd(mph)', 'Wspdgust(mph)NA', 'Humidity', 'HrlyPrecip(In)', 'ConditionsNA', 'CloudsNA', 'dailyrain(In)', 'SoftwareTypeNA', 'DateUTCNA', 'NA'])    

    dateTimeUTC=[]
   
    array = numpy.array(metdf)    
    for i in numpy.arange(len(array)):
            #print str(array[i,1])
            try:
                dateTimeUTC.append(datetime.datetime.strptime(array[i,0], '%Y-%m-%d %H:%M:%S')+ datetime.timedelta(hours=8))
            except:
                metdf=metdf.drop([i])
                print 'INDEX # '+str(i)+' DROPPED\n'
           
            
        
    #metdf['DateTimeUTC'] = dateTimeUTC
    
    metdf.index=dateTimeUTC
    #print metdf
    #raw_input()
    
    #pst = pandas.to_datetime(metdf['Time(Epoch)'], unit='s')
    #utc = pst+datetime.timedelta(hours=8)
    
   # metdf.index = utc
    #metdf['pst'] = pst
    #os.remove(temp)
    #os.remove(temp[:-4]+'cleaned.txt')
    metdf['Wspd'] = metdf['Wspd(mph)']*0.44
    metdf['T(C)'] = (metdf['Temp(F)']-32.)*(5./9.)
    metdf['Press'] = metdf['Press(In)']*0.0295299830714
    metdf['theta'] = (metdf['T(C)']+273.16) * (1013/metdf['Press'])**(287.0/1004)
    es = 6.11*(numpy.exp(6808*(1/273.15-1/(metdf['T(C)']+273.15))-5.09*(numpy.log((metdf['T(C)']+273.15)/273.15))))
    e = es*metdf['Humidity']/100
    w = 0.622/(metdf['Press']/e-1)   #mixing ratio, kg/kg
    metdf['q'] = 1/(1+1/w)*1e3       #specific humidity, g/kg
    #print metdf
    #raw_input()
    metdf2=pandas.DataFrame(metdf['Wspd'])
    metdf2['Wdir'] = metdf['Wdir']
    metdf2['temp']=metdf['T(C)']
    metdf2['H20Pres']=e
    metdf2['humidity']=metdf['Humidity']
    metdf2=metdf2.resample('H', how=numpy.nanmean)
    # average to every hour
    #print(metdf2)
    #raw_input()
    
    metdf2.save('/Users/Eating/Documents/ATM_R/python program/'+title+'.df')
    
    print 'Chews Ridge METEO DATA SAVED TO FILE : '+'/Users/Eating/Documents/ATM_R/python program/'+title+'.df\n'
   
    return(metdf2)

#Date format for Chews met data
def chewsmet_converter(u):
    import time
    return(time.mktime(time.strptime(u, '%Y-%m-%d %H:%M:%S')))
    
#convert df data to txt
def chewsmet_txt(title,path):
    import glob
    import csv
    import pandas


chews_met(6, 15, 2015, 30,'20150615_30_h','/Users/Eating/Documents/ATM_R/python program/')
