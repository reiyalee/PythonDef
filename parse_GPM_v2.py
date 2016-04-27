# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 16:10:51 2016

@author: Yiting

this program is to download GPM GMI data from website (FTP)

"""

import ftplib  as FTP
import os

def ftp_callback(line):
    items=line.split()
    #print items[-3]
    files_gpm.append(items[-3])

def parse_gpm(year,month,day):
    #year=2015
    #month=1
    #day=31

    ftp=FTP.FTP('arthurhou.pps.eosdis.nasa.gov')
    ftp.login('summeryiting@gmail.com','summeryiting@gmail.com') # give username and password
    for i in range(7,day):
        if month < 10 and i < 10:
            path='/gpmdata/'+str(year)+'/'+'0'+str(month)+'/'+'0'+str(i)+'/'+'1C'+'/'
        elif month < 10 and i >= 10:
            path='/gpmdata/'+str(year)+'/'+'0'+str(month)+'/'+str(i)+'/'+'1C'+'/'
        elif month >= 10 and i < 10:
            path='/gpmdata/'+str(year)+'/'+str(month)+'/'+'0'+str(i)+'/'+'1C'+'/'
        elif month >= 10 and i >= 10:
            path='/gpmdata/'+str(year)+'/'+str(month)+'/'+str(i)+'/'+'1C'+'/'
        else:
            print "No data valid"
            
        #print path
        ftp.cwd(path)
        def ftp_callback(line):
            items=line.split()
            #print items[-3]
            files_gpm.append(items[-3])

        files_gpm = []
        files = ftp.retrlines('LIST',callback=ftp_callback)
        # get the filename in this directory

        files_gmi=[]
        for i in range(0,len(files_gpm)):
            lines=files_gpm[i].rstrip()
            print lines
            itemss=lines.split('.')
            if itemss[0]=='1C-R':
               files_gmi.append(files_gpm[i])
               # get filenames which start with 1C-R

        filename=files_gmi
        path2='F:\ATM298_Python\GPM_data'
        for i in range(0,len(filename)):
            print('starting download'+'i')
            ftp.retrbinary('RETR '+filename[i],open(os.path.join(path2,filename[i]),'wb').write)
            # download 1C-R GMI data from directory
#print 'hahha'
    
    ftp.quit()


        
parse_gpm(2015,11,30)
