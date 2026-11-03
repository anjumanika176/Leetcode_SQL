# LeetCode_SQL
My Solution for LeetCode SQL Design in Python

#LeetCode 2408 : Design SQL
## Problem
Design a class that manages many tables. Each table has a name and a fixed number of columns. The class supports four operations : 
- `ins`: insert a row with an auto-increment Id
- `rmv`: remove a row(Id's are never reused)
- `sel`: get the value of one cell, or "null" if invalid
- `exp`: export all rows as csv strings

##Approach
- A dictionary stores the column count of each table
- A dictionary stores the next Id of each table. It only goes up, so a removed Id is never reused
- A dictionary stores the rows of each table as `[Id,[values]]`.

##Language
Python3

##Link
https://leetcode.com/problems/design-sql
