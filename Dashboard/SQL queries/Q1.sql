How many job applicants have applied for each job posting, and
  what are the required skills for the jobs that received the highest number of applicants?
  
  
  "This question allows the business to identify which job postings are attracting the most applicants.
  Knowing the popular job postings can help the HR department tailor their recruitment strategies
  and allocate resources efficiently. Additionally, understanding the required skills 
  for these popular jobs provides insights into the skillsets in high demand,
which can guide the design of training programs or curricula to meet industry needs."

-- SQL Query
  SELECT 
    J."Job ID",
    J."Job Title",
    D."Required Skills",
    J."Job Location",
    D."Total Number of Job Applicants"
FROM 
    Jobs J
JOIN Details D ON J."Details ID" = D."Details ID"
WHERE 
    D."Total Number of Job Applicants" = (
        SELECT 
            MAX("Total Number of Job Applicants")
        FROM 
            Details
    );



