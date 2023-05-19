" 1.Comparison of number of jobs across different cities for different level"

select location, level, count(job_id) as cnt_job from jobs_table natural join detail_table group by location, level