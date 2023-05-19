"3.Generate insights into number of opening with respect to the current employee count - Number of opening in a company with more than 1000 employees in comparison to
 number of openings in a company with 100 employees"
 
with cte1 as
(select count(job_id)  as "employees >= 1000" from jobs_table j natural join company_table c where (employees >= 1000)),
cte2 as 
(select count(job_id) as "employees <= 100" from jobs_table j natural join company_table c where (employees <= 100))
select * from cte1, cte2
