# SQL Injection

## What is SQL Injection?

SQL Injection (SQLi) is a type of injection attack that makes it possible to execute malicious SQL statements. These statements control a database server behind a web application. Attackers can use SQL Injection vulnerabilities to bypass application security measures. They can go around authentication and authorization of a web page or web application and retrieve the content of the entire SQL database. They can also use SQL Injection to add, modify, and delete records in the database.

## Example

A simple example of SQL injection is to enter `' OR '1'='1'` in a username or password field. If the application is vulnerable, this will cause the query to become:

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = ''
```

Since `'1'='1'` is always true, this will bypass the authentication.
