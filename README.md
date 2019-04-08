# Web_scrapper_Email_from_domain_finder
This is a web scrapper that will find all the related emails with respect tot the domain name.

## Pre - requisite to install

* Open command prompt or terminal
* Hopefully you have **Python** and **PIP** installed
* pip install scrapy
* pip install google

Install MySQL and other libraries to if required.

## Steps to create a database with python
NOTE - You have MySQL pre installed before running this command to check run the next command

``` import mysql.connector ```

Get connected with DB
``` 
  mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword") 
```

Now first of all we should create a database

```
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE web_scraper_email_address")
```

To check DB -> You can run this command and after that you can use that command

```
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x) 
  
  mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="web_scraper_email_address"
)
mycursor.execute("USE web_scraper_email_address")

```

Now we have to create Table to store the domain name and email

```

mycursor.execute("CREATE TABLE email_domain  (domain_name VARCHAR(255), email VARCHAR(255))")

```


Just a schema of DB
```
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| domain_name | varchar(255) | YES  |     | NULL    |       |
| email       | varchar(255) | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
```

## How I improved the search of emails

I am not directly searching for emails from that particular URL to find emails, instead I firstly scrapping all the similar URL's and then searching for emails in that.
