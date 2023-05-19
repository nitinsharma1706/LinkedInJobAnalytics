"5.Count the number of jobs across different industry across different locations. For instance, how many Frontend Engineer jobs are there in Bangalore 
as compared to Data Analytics jobs in Bangalore, or how many Data Analytics jobs are there in Bangalore as compared to number of Data Scientists job in Gurgaon - 
this needs to be done in SQL but presented in the above created Excel dashboard"

select industry, location, designation, count(job_id) as cnt
from jobs_table natural join company_table
group by  industry, location, designation