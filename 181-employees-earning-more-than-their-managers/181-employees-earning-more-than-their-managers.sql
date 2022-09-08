# Write your MySQL query statement below
# select E1.name as Employee
# from Employee as E1, Employee as E2
# where E1.managerId = E2.id and E1.salary > E2.salary
# 셀프 조인이 더 느리다
select E1.name as Employee
from Employee as E1
join Employee as E2 on E1.managerId = E2.Id
where E1.salary > E2.salary