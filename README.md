# Updated Project Report: Data Scraping and Analysis of Jobs Data from LinkedIn

## Introduction

The project aims to scrape job data from LinkedIn using the Python library BeautifulSoup and collate information in the given format. The scraped data will be transformed into three tables, namely jobs, company, and details, using Pandas. A search bar will be created using the Flask web framework where users can search for skills, and information such as the most common experience level, industry, and company class where the skill is required, and the number of jobs available will be displayed. Additionally, the FuzzyBuzzy library will be used to correct user input errors in the search bar.

![Sample_User_interface](https://organic-meat-d9c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6924ce33-8b0b-48aa-b160-acda88d687e3%2FUntitled.png?id=737e0fc7-5be9-4416-ab42-4f44421e75ab&table=block&spaceId=c66c347d-9bbf-4d43-ac0c-5d6d4736cb3e&width=800&userId=&cache=v2)

## Data Description

Jobs Table: This table contains information related to the job postings, including the job ID, company ID, job location, job title, and details ID.

Company Table: This table contains information related to the companies posting job listings, including the company ID, company name, industry, number of employees, and number of LinkedIn followers.

Details Table: This table contains additional details related to the job postings, including the details ID, experience level, required skills, and total number of job applicants.



## Methodology

The following methodology was used to accomplish the project objectives:

1. **Data Scraping:** The job data was scraped from LinkedIn using the Python library BeautifulSoup. The data was scraped based on specific search criteria, such as job titles, job locations, and company names.

2. **Data Transformation:** The scraped data was transformed into three tables, namely jobs, company, and details, using Pandas. The jobs table contained attributes such as job_id, company_id, location, designation, and details_id. The company table contained attributes such as company_id, name, industry, employees_count, and linkedin_followers. The details table contained attributes such as details_id, involvement, level, total_applicants, and skills.

3. **Feature Extraction:** The NLTK library was used to gather the required skills from the job descriptions in the details table with the help of Natural Language Processing.

4. **Company Classification:** The companies were classified into four classes, namely Class1, Class2, Class3, and Class4, based on their employee count and LinkedIn followers using a clustering algorithm. A new column was added to the company table to represent the company class.

5. **User Interface:** A search bar was created using the Flask web framework where users could search for skills. The FuzzyBuzzy library was used to correct user input errors in the search bar. Upon entering the skill, the most common experience level, industry, and company class where the skill is required, and the number of jobs available for the skill were displayed.

## Results

### This is webpage that will take input from users and generate output according to searched skills.
![Sample_User_interface](https://drive.google.com/uc?export=download&id=1fwhxw2c6r0E55K9SPt5cZ6wCjC8GnK5h)

### This is webpage that show all the listed jobs with some additional information.
![Sample_User_interface](https://drive.google.com/uc?export=download&id=1hOy90FuvOg4csqVpLOLrg37hgQE-1hii)


