# Project Name : Job Analytics

## Introduction

The project aims to scrape job data from LinkedIn using the Python library BeautifulSoup and collate information in the given format. The scraped data will be transformed into three tables, namely jobs, company, and details, using Power Query. A search bar will be created using the Flask web framework where users can search for skills, and information such as the most common experience level, industry, and company class where the skill is required, and the number of jobs available will be displayed. Additionally, the FuzzyBuzzy library will be used to correct user input errors in the search bar.
<p align="center">
  <img src="https://organic-meat-d9c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6924ce33-8b0b-48aa-b160-acda88d687e3%2FUntitled.png?id=737e0fc7-5be9-4416-ab42-4f44421e75ab&table=block&spaceId=c66c347d-9bbf-4d43-ac0c-5d6d4736cb3e&width=500&userId=&cache=v2" width="400">
</p>


## Problem aimed to solve

1. Time-consuming and manual job search
2. Lack of comprehensive job information
3. Inaccurate search queries
4. Difficulty in analyzing job market trends


## Data Description

- Jobs Table: This table contains information related to the job postings, including the job ID, company ID, job location, job title, and details ID.

- Company Table: This table contains information related to the companies posting job listings, including the company ID, company name, industry, number of employees, and number of LinkedIn followers.

- Details Table: This table contains additional details related to the job postings, including the details ID, experience level, required skills, and total number of job applicants.



## Methodology

The following methodology was used to accomplish the project objectives:

1. **Data Scraping:** The job data was scraped from LinkedIn using the Python library BeautifulSoup. The data was scraped based on specific search criteria, such as job titles, job locations, and company names.

2. **Data Transformation:** The scraped data was transformed into three tables, namely jobs, company, and details with the help of Power Query and Excel. The jobs table contained attributes such as job_id, company_id, location, designation, and details_id. The company table contained attributes such as company_id, name, industry, employees_count, and linkedin_followers. The details table contained attributes such as details_id, involvement, level, total_applicants, and skills.

3. **Data Cleaning and Pre-processing:** The data cleaning process encompassed eliminating irrelevant data, addressing missing values, standardizing formats, removing duplicates, cleaning textual data, handling outliers, converting data types, checking for inconsistencies, normalizing categorical data, and validating data integrity.

4. **Dashboard Creation:** A dashboard was created using Power BI to provide an interactive visualization of the data. The dashboard included various charts and graphs to display the data in an easy-to-understand format. The charts included a skill distribution chart, a company class distribution chart, and a job location chart.

![Sample_User_interface](https://drive.google.com/uc?export=download&id=1PlrEg8wLSgjdHdEM70aSMQFMGwEZwTMg)

5. **Feature Extraction:** The NLTK library was used to gather the required skills from the job descriptions in the details table with the help of Natural Language Processing.

6. **Company Classification:** The companies were classified into four classes, namely Class1, Class2, Class3, and Class4, based on their employee count and LinkedIn followers using K-Means clustering algorithm. A new column was added to the company table to represent the company class. Additionally we also evaluated it by Elbow Method and the optimum number of clusters are 4.

<p align="center">
  <img src="https://drive.google.com/uc?export=download&id=1jmAdodfremotelYI3mMF0U9-w1CT63Js" width="400">
</p>

<h5 align=center>
  Optimum number of cluster 
<h5>
   
<p align="center">
  <img src="https://drive.google.com/uc?export=download&id=1EQ-MHNLCRd2GrtK_GC1nVAeK_jD2veZk" width="400">
</p>
   
 <h5 align=center>
  3-D Scatter Plot of Clusters
 <h5>
  
 <p>&nbsp;</p>

7. **User Interface:** A search bar was created using the Flask web framework where users could search for skills. The FuzzyBuzzy library was used to correct user input errors in the search bar. Upon entering the skill, the most common experience level, industry, and company class where the skill is required, and the number of jobs available for the skill were displayed.

## Results

### 1. Key Insights from Dashboard

- Maximum No of Jobs are in Bengaluru.

- Top Hiring Industries are Information and Technology, Financial, and Education.
 
- Top 5 States which have the most jobs are Delhi, Maharashtra, Haryana, Karnataka, and Uttar Pradesh.

- Most of the Jobs are Full Time.

- Large Company which are having employees count of 1000+ having 52% volume of total Jobs

- When we are selecting Delhi we get to know that we have most of the jobs in Education Sector and then Information and Technology

- We also get to know that Education sector has 37.29% Internships.

- If we select Maharastra then we get to know that the  top industries are IT and Finance.


### 2. This is webpage that will take input from users and generate output according to searched skills.

<p>
  <img src="https://drive.google.com/uc?export=download&id=1fwhxw2c6r0E55K9SPt5cZ6wCjC8GnK5h" width="1200">
</p>


<!-- ![Sample_User_interface](https://drive.google.com/uc?export=download&id=1fwhxw2c6r0E55K9SPt5cZ6wCjC8GnK5h) -->

### 3. This is webpage that show all the listed jobs for the particular skills with some additional information.

<p>
  <img src="https://drive.google.com/uc?export=download&id=1hOy90FuvOg4csqVpLOLrg37hgQE-1hii" width="1200">
</p>
<!-- ![Sample_User_interface](https://drive.google.com/uc?export=download&id=1hOy90FuvOg4csqVpLOLrg37hgQE-1hii) -->
   
## Limitation
   
- One limitation of this project is the dependency on the structure and layout of the LinkedIn website. If LinkedIn changes its webpage structure or adds additional security measures, it may affect the data scraping process and require adjustments to the scraping code.
- Another limitation of the project is that the accuracy and effectiveness of NLP in improving user input may vary depending on the complexity of the queries and the available training data. Ongoing research and improvements in NLP techniques can help enhance the accuracy and performance of user input correction.

## Challenges:
   
- One of the main challenges faced in this project is implementing natural language processing (NLP) techniques to improve user input. NLP is a complex field, and incorporating it to enhance user input requires in-depth research and understanding. Overcoming the challenge of integrating NLP effectively to correct user input errors can be time-consuming and technically demanding.


## References

- Python Software Foundation. (2022). Python Language Reference, version 3.10. Retrieved from https://docs.python.org/3/reference/index.html

- Wikipedia contributors. (2023, April 19). BeautifulSoup. In Wikipedia, The Free Encyclopedia. Retrieved 15:44, April 22, 2023, from "https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)"

- Wikipedia contributors. (2023, April 13). Flask (web framework). In Wikipedia, The Free Encyclopedia. Retrieved 15:48, April 22, 2023, from "https://en.wikipedia.org/wiki/Flask_(web_framework)"

- Pandas Development Team. (n.d.). pandas 1.4.5 documentation. Retrieved April 22, 2023, from "https://pandas.pydata.org/docs/"

- Scikit-learn developers. (n.d.). Clustering. Retrieved April 22, 2023, from "https://scikit-learn.org/stable/modules/clustering.html"

- FuzzyBuzzy. (n.d.). FuzzyBuzzy Documentation. Retrieved April 22, 2023, from "https://pypi.org/project/fuzzybuzzy/"

- Microsoft Corporation. (n.d.). Power BI. Retrieved April 22, 2023, from "https://powerbi.microsoft.com/en-us/"

- Selenium with Python: https://selenium-python.readthedocs.io/

