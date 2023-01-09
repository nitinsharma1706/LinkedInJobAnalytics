

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


#List of email and passwords

emails_=[""] #Enter your E-mail addresss

passwords_=[""] #Enter your password

for email_address , email_password in zip(emails_,passwords_): #iterating two list in one go with zip function
    email = email_address
    password1= email_password
    #Using webdriver to  automate the chrome browser
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://linkedin.com/uas/login") #Link of page

    time.sleep(3)

    #Finding the path to fill eamil and assinging it to the valriable
    username = driver.find_element("id","username")
    #Sending email to that path
    username.send_keys(email)
    #Finding the path to fill password and assinging it to the valriable
    passw = driver.find_element("id","password")
    #Sending password to that path
    passw.send_keys(password1)
    
    driver.find_element("xpath","//button[@type='submit']").click()
    #clicking on login button on linkedIn
    
    time.sleep(20)
    #URl for the Job page
    job_url="https://www.linkedin.com/jobs/collections/?currentJobId=3420238222"
    driver.get(job_url) #browsing that Url 
    
    time.sleep(5)
    time.sleep(5)

    #Creating a empty set for Unique values 
    lnk = set()
    #for confirmation we are printing here
    print("going to next page")
    #Getting link for next pages of the link
    for i in range(2,41):
    #Divided on two bases--> "9>i" "i<9" <-- 
    #cause we have 9 different links for 9 pages but after that we have same link
        if i == 2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8 or i==9: 
            #xpath are dynamic so we are using try exception handling to not getting error 
            try:
                #assining to a variable
                click_button =  driver.find_element("xpath",f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/div[7]/ul/li[{i}]/button')
            except:
                try:
                    click_button =  driver.find_element("xpath",f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/div[6]/ul/li[{i}]/button')
                except:
                    try:
                        click_button =  driver.find_element("xpath",f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[7]/ul/li[{i}]/button')
                    except:
                        try:
                            click_button =  driver.find_element("xpath",f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[6]/ul/li[{i}]/button')
                        except:
                            try:
                                click_button =  driver.find_element("xpath",f'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/div[4]/ul/li[{i}]/button')
                            except:
                                click_button =  driver.find_element("xpath",f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[4]/ul/li[{i}]/button')

        else:

            try:
                click_button =  driver.find_element("xpath",'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/div[6]/ul/li[7]/button')
            except:
                try:
                    click_button =  driver.find_element("xpath",'/html/body/div[4]/div[3]/div[4]/div/div/main/div/section[1]/div/div[4]/ul/li[7]/button')
                except:
                    try:
                        click_button =  driver.find_element("xpath",'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[4]/ul/li[7]/button')
                    except:
                        click_button =  driver.find_element("xpath",'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/div[6]/ul/li[7]/button')
        #clicking on the link with the help of .click() function
        click_button.click()
        print(i)
        src = driver.page_source
        
        soup = BeautifulSoup(src,'html.parser')
        #finding all the link and 
        anc= soup.find_all('a')
        #adding links to lnk set
        for i in anc:
            lnk.add(i.get('href'))

        print('link_added')
        time.sleep(3)
    print(lnk)




    #Created a empty list
    xt = []
    #filtering the links which are related to job 
    for i in lnk:
        if i[:6] == '/jobs/': 
            #adding the domain of linkedin to the links
            m = 'https://www.linkedin.com/'+i   
            xt.append(m)             #appending links to the list

    #importing  csv 
    import csv
    #open the csv file in append mode
    with open('linkedin007.csv','a+',encoding='UTF8' ,newline='') as f:
        writer = csv.writer(f)
        #Writing the header columns to the csv file
        header = ["Job_Name","Company",'Loaction','Job_type','Employees','Followers','Applicant','Industry','Invovlement']
        writer.writerow(header)



    #Opening each link which is present in xt list
    for i in xt:
        try:

            driver.get(i)
            time.sleep(5)
            src2 = driver.page_source
            soup2 = BeautifulSoup(src2,'html.parser')
            #looking for title here with the help of beautiful soup
            try:
                title = soup2.find('h1',class_='t-24 t-bold jobs-unified-top-card__job-title').text.replace('\n','').strip()
            except:
                try:
                    title = soup2.find('a',class_='ember-view t-black t-normal').text.replace('\n','').strip()
                except :
                    title = 'Null'
            #looking for Company here with the help of beautiful soup
            try:
                company = soup2.find('span',class_='jobs-unified-top-card__company-name').text.replace('\n','').strip()
            except:
                try:
                    company = soup2.find('a',class_='ember-view t-black t-normal').text.replace('\n','').strip()
                except :
                    company = 'Null'

            #looking for Location here with the help of beautiful soup
            location = soup2.find('span',class_='jobs-unified-top-card__bullet').text.replace('\n','').strip()
            typ = soup2.find('span',class_='jobs-unified-top-card__workplace-type').text.replace('\n','').strip()

            #looking for Employees here with the help of beautiful soup
            try:
                employees = soup2.find('span',class_='jobs-company__inline-information').text.replace('\n','').strip() 
            except:
                employees = 'Null'
            #looking for Followers here with the help of beautiful soup
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
            #looking for Industry here with the help of beautiful soup
            Industry=soup.find('div',class_='t-14 mt5').text.replace('\n','').strip()   
            involvement = soup2.find('li',class_='jobs-unified-top-card__job-insight').text.replace('\n','').strip()

            mm = [title,company,location,typ,employees,followers,applicant,Industry,involvement]
            print(mm)
            
            #Opening the csv and writing the values which we have got from the above code
            with open('linkedin007.csv','a+',encoding='UTF8' ,newline='') as f:
                writer = csv.writer(f)     
                writer.writerow(mm)
        except:
            pass

        
