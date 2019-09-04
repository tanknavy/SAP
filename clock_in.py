# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:53:45 2016

@author: ac32
"""
# requests???????
import requests

with requests.session() as c:
    url = 'https://webpunch/index.asp'
    punch_url='https://webpunch/scripts/usermode.asp'
    hist_url='https://webpunch/scripts/punchhist.asp'
    showtm_url='https://webpunch/scripts/showtime.asp'
    
    EMPLOYEE = '9XXXXXX'
    PWRD = '1234'
    login_data = dict(employee=EMPLOYEE, pwrd=PWRD, B1='login', mode='login')    
    
    c.get(url,verify=False)
    c.post(url, data=login_data,headers={"Referer":"https://webpunch/index.asp"}, verify=False)
    c.get('https://webpunch/index.asp', verify=False)
    page = c.get('https://webpunch/scripts/usermode.asp', verify=False)
#    print page.conten
  
########### server time: showtm
#    test = c.get('https://webpunch/scripts/showtime.asp', verify=False)
#    print test.content

########### clock in/out

#    clockin = dict(btnin1='IN')
#    clockot = dict(btnout1='OUT')
#   ??javascripts?in?out??
    inpage = c.post('https://webpunch/scripts/inout.asp?opt=IN', verify=False)
#    outpage = c.post('https://webpunch/scripts/inout.asp?opt=OUT', verify=False)
    
###########  history  
#    page = c.get(hist_url, verify=False)    
#    print page.content
    