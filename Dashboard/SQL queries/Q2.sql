"2.Generate some insight with respect to number of jobs distribution across various industry. For instance, what is the total number of jobs in Software Industry as compared to Marketing"

select distinct(industry), count(job_id) as cnt_jobs from jobs_table natural join company_table group by industry





