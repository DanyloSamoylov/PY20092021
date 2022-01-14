--task 1
SELECT first_name,
    last_name,
    department_id,
    department_name
FROM employees emp
JOIN department dep
ON emp.department_id=dep.department_id;
--task 2
SELECT first_name,
    last_name,
    department_name,
    city,
    state_province
FROM employees emp
JOIN department dep
ON emp.department_id=dep.department_id
JOIN locations loc
ON dep.location_id=loc.location_id;
--task 3
SELECT first_name,
    last_name,
    department_id,
    department_name
FROM employees emp
JOIN department dep
ON emp.department_id = dep.department_id
WHERE dep.department_id = '40';
--task 4
SELECT department_name FROM department;
--task 5
SELECT first_name,
    department_id
FROM employees;
--task 6
SELECT jobs.job_title,
    emp.first_name || ' ' || emp.last_name as full_name,
    jobs.max_salary - emp.salary as defference_salary
FROM employees emp
JOIN jobs
ON emp.job_id = jobs.job_id;
--task7
SELECT jobs.job_title,
    AVG(emp.salary)
FROM employees emp
JOIN jobs
ON emp.job_id = jobs.job_id;
--tast 8
SELECT emp.first_name || ' ' || emp.last_name as full_name,
    emp.salary,
    loc.city
FROM employees emp
JOIN department dep
ON emp.department_id = dep.department_id
JOIN locations loc
ON dep.location_id = loc.location_id
WHERE loc.city = 'London';
--task 9
SELECT dep.department_name,
    COUNT(emp.department_id) as number_of_workers
FROM employees emp
JOIN department dep
ON emp.department_id = dep.department_id
GROUP BY emp.department_id;

