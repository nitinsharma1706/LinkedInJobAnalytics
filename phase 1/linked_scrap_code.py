#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from datetime import date



with open(f"C:/Users/HP/OneDrive/Desktop/Completed Projects/LinkedIn_daily_data/LinkedIn {date.today()}.csv",'a+',encoding='UTF8' ,newline='') as f:
    writer = csv.writer(f)
    header = ["Date","Job_Name","Company",'Loaction','Job_type','Employees','Followers','Applicant','Industry','Invovlement']
    writer.writerow(header)


# Creating login page and getting jobs page

email = "donsengar123@gmail.com"
password= "rdldyx5rpp"

driver = webdriver.Chrome("chromedriver.exe")


driver.get("https://linkedin.com/uas/login")

time.sleep(3)



username = driver.find_element("id","username")

username.send_keys(email)

passw = driver.find_element("id","password")
passw.send_keys(password)

driver.find_element("xpath","//button[@type='submit']").click()

# heading to jobs page

time.sleep(5)
job_url="https://www.linkedin.com/jobs/collections/?currentJobId=3420238222"
driver.get(job_url)
time.sleep(5)
lnk = set()
print("going to next page")


# Changing pages and getting all links of pages

for i in range(2,41):
    driver.find_element("xpath",f"//button[@aria-label='Page {i}']").click()

    print(i)
    src = driver.page_source

    soup = BeautifulSoup(src,'html.parser')
        
    anc= soup.find_all('a')
            
    for i in anc:
        lnk.add(i.get('href'))
            
    print('link_added')
    time.sleep(3)
print(lnk)


# link added to lnk variable now selecting only jobs link and adding to XT variable


xt = []
for i in lnk:
    if i[:6] == '/jobs/':     
        m = 'https://www.linkedin.com/'+i   
        xt.append(m) 
        
        
# Links added now getting data from all the pages       
    
for i in xt:
    try:
        driver.get(i)
        time.sleep(5)
        src2 = driver.page_source
        soup2 = BeautifulSoup(src2,'html.parser')

        try:
            title = soup2.find('h1',class_='t-24 t-bold jobs-unified-top-card__job-title').text.replace('\n','').strip()
        except:
            try:
                title = soup2.find('a',class_='ember-view t-black t-normal').text.replace('\n','').strip()
            except :
                title = 'Null'

        try:
            company = soup2.find('span',class_='jobs-unified-top-card__company-name').text.replace('\n','').strip()
        except:
            try:
                company = soup2.find('a',class_='ember-view t-black t-normal').text.replace('\n','').strip()
            except :
                company = 'Null'


        location = soup2.find('span',class_='jobs-unified-top-card__bullet').text.replace('\n','').strip()
        typ = soup2.find('span',class_='jobs-unified-top-card__workplace-type').text.replace('\n','').strip()


        try:
            employees = soup2.find('span',class_='jobs-company__inline-information').text.replace('\n','').strip() 
        except:
            employees = 'Null'


        try:
            followers = soup2.find('div',class_='artdeco-entity-lockup__subtitle ember-view t-16').text.replace('\n','').strip().replace('\n','').strip()
        except:
            try:
                followers = soup2.find('div',class_='artdeco-entity-lockup__content ember-view flex-grow-1').text.replace('\n','').strip()
            except:
                followers = 'Null'  

        try:
            applicant = soup2.find('span',class_='jobs-unified-top-card__applicant-count').text.replace('\n','').strip() 
        except:
            try:
                applicant = soup2.find('span',class_='jobs-unified-top-card__subtitle-secondary-grouping t-black--light').text.replace('\n','').strip()
            except:
                applicant = 'Null'



        industry = soup2.find('div',class_='t-14 mt5')
        for i in industry:
            industry = i.text.replace('\n','').strip()
            break

        involvement = soup2.find('li',class_='jobs-unified-top-card__job-insight').text.replace('\n','').strip()
        Date = date.today()

        rows = [Date,title,company,location,typ,employees,followers,applicant,industry,involvement]
        print(rows)


        with open(f"C:/Users/HP/OneDrive/Desktop/Completed Projects/LinkedIn_daily_data/LinkedIn {date.today()}.csv",'a+',encoding='UTF8' ,newline='') as f:
            writer = csv.writer(f)     
            writer.writerow(rows)
    except:
        pass

