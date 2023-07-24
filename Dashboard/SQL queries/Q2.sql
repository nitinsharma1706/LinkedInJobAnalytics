What are the top 5 job titles that have the highest number of job applicants, and which industries do these job titles belong to?

  "This question helps the business identify the most sought-after job titles in the job market. For an ed-tech startup, 
  this information can guide the development of relevant courses or programs to cater to popular job roles. College placement teams 
  can leverage this data to focus on assisting students in securing internships or jobs in high-demand fields. Similarly, for HR departments,
  understanding popular job titles in different industries aids in optimizing recruitment efforts to attract qualified candidates for specific roles."

SELECT 
    J."Job Title",
    C."Industry",
    SUM(D."Total Number of Job Applicants") AS "Total Applicants"
FROM 
    Jobs J
JOIN Company C ON J."Company ID" = C."Company ID"
JOIN Details D ON J."Details ID" = D."Details ID"
GROUP BY 
    J."Job Title",
    C."Industry"
ORDER BY 
    SUM(D."Total Number of Job Applicants") DESC
LIMIT 5;



