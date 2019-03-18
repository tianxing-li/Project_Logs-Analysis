# Project: Logs Analysis
This is a project from udacity full stack nano degree.
Project for database with SQL and Python.

## Environment
Run under the a vagrant virtual machine from Udacity.
see more from [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)

## How to Run
1. connect the database newsdata.sql
2. install the python package `psycopg2` and `datetime`.
3. locate the file directory
4. using this command in the command line under the virtual machine mentioned above.
```
python Proj_LogsAnalysis.py
```
5. see the result in [result](https://github.com/tianxing-li/Project_Logs-Analysis/blob/master/result)

## About the view in the code
1. view `mostreads`
This view listed **most popular articles with slug name**, and how popular they are.
2. view `errorReport`
This view listed **the statistics from requests** leads to errors group by date.
3. view `connReport`
This view listed **the statistics from all requests** group by date.
4. view `mostreadarticle`
This view listed **most popular articles with title** and views.
5. view `errrate`
This view listed **requests error rate** group by date order from high to low.