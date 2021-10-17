# [CODEWARS] SQL Bug Fixing: Fix the JOIN

> Oh no! Timmys been moved into the database divison of his software company but as we know Timmy loves making mistakes. Help Timmy keep his job by fixing his query...
>
> Timmy works for a statistical analysis company and has been given a task of calculating the highest average salary for a given job, the sample is compiled of 100 applicants each with a job and a salary. Timmy must display each unique job, the total average salary, the total people and the total salary and order by highest average salary. Timmy has some bugs in his query, help Timmy fix his query so he can keep his job!
>
> ### people table schema
>
> - id
> - name
>
> ### job table schema
>
> - id
> - people_id
> - job_title
> - salary
>
> ### resultant table schema
>
> - job_title (unique)
> - average_salary (float, 2 dp)
> - total_people (int)
> - total_salary (float, 2 dp)

## 풀이

- ::NUMERIC 과 ::FLOAT는  CAST 명령의 축약형이다.
- ROUND 함수를 사용하기 위해서는 NUMERIC으로 변경이 필요하여 형변환을 두 번 사용했다.
- JOIN의 조건인 ON을 적어주어야 GROUP BY를 실행 할 수 있다.

```sql
SELECT 
  j.job_title,
  ROUND( (SUM(j.salary)::NUMERIC / COUNT(p)), 2)::FLOAT as average_salary,
  COUNT(p.id) as total_people,
  ROUND(SUM(j.salary),2)::FLOAT as total_salary
  FROM people p
    JOIN job j
    ON p.id=j.id
  GROUP BY j.job_title
  ORDER BY average_salary DESC;
```

