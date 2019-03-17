## News Log DB Analysis
This module is written to answer three questions using a news log database. 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

When run, it will run queries on the news database and will print out the answers in the console.

#### Requirements 

You will need to have postgres sql and python installed in order to ran it. 

#### Data

You can download the data in this folder, newsdata.txt, and load it using command `psql -d news -f newsdata.sql`.

#### How to ran

The module is named log_analysis.py. Ran `python log_analysis.py` from the command line after loading the data to see the results. 

#### Results
Results will change if the database is updated, but below is the output as of March 17, 2019.
```
Q1: What are the three most popular articles of all time?

"Candidate is jerk, alleges rival" -- 338,647 views
"Bears love berries, alleges bear" -- 253,801 views
"Bad things gone, say good people" -- 170,098 views


Q2: Who are the most popular article authors of all time?

1. Ursula La Multa -- 507,594 views
2. Rudolf von Treppenwitz -- 423,457 views
3. Anonymous Contributor -- 170,098 views
4. Markoff Chaney -- 84,557 views


Q3: On which days did more than 1% of requests lead to errors?

July 17, 2016 -- 2.26% errors
```

