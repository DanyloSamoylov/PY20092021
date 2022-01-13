SELECT first_name, last_name FROM employees;

SELECT DISTINCT department_id FROM employees;

SELECT * FROM employees ORDER BY first_name ASC;

SELECT * FROM employees ORDER BY first_name DESC;

SELECT first_name, last_name, salary/100*12 FROM employees;

SELECT MAX(salary) FROM employees;

SELECT MIN(salary) FROM employees;

SELECT first_name, ROUND(salary, 2), salary FROM employees;