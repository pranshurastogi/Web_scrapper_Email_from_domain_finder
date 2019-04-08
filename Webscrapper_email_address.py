#!/usr/bin/env python
# coding: utf-8

# In[35]:


#!/usr/bin/env python
# coding: utf-8

# In[4]:

# Before running this project install all required libraries and create Mysql database and table

# Importing libraries
# To know more about this just go through README.md
import logging
import mysql.connector 
import urllib.request,re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search




# This is to authenticate with Mysql database
# I have created database with name "web_scraper_email_address" make sure to create one before running this code
mydb = mysql.connector.connect(host="localhost",                             # your host 
                               user="root",                                  # username
                               passwd="rastogi",                             # password
                               database="web_scraper_email_address")         # name of the database

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE web_scraper_email_address")


# If you get error in next line, just uncomment the previous line and run again and don't forget to comment it again
# Or just use your CLI skills and create database of same name or change name here;

mycursor.execute("USE web_scraper_email_address")                            # See how I am using this DB :(                   
# print(mydb)


# Now I have just created a table having name email_domain 


# Some print statements to make user comfortable with my words .....
print("\t WELCOME TO EMAIL ADDRESS FINDER -> DEVELOPED BY PRANSHU RASTOGI \n ")
print("\t ENTER THE DOMAIN NAME FOR EG -> tersesoft.com \n")
domain_name = str(input(" \t Ready to type domain name \t"))            # Took string input to take domain name

email_list = []


# This is our catalyst that will make response faster
# It will search emails from database and give faster response if you have searched it previously

# Searching just email from DB wrt domain name
sql = "SELECT email FROM email_domain WHERE domain_name = %s"
adr = (domain_name,)
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
length_cache = (len(myresult))
# print(length_cache,"length")
for x in myresult:
    print(x,"\t This result comes from one of your last search , fast isn't it.")


if (length_cache < 1):
    web_scrapper()
else:
    pass
    

# This function will fetch the relative url's with the matching domain_name string.
# I have used this function to use this as a pipeline , so that it just widen up the results
# For better understanding watch out the code below this function


def web_scrapper():
    try:
        def get_urls(tag, n, language):
            urls = [url for url in search(tag, stop=n, lang=language)][:n]
            return urls
        a =get_urls('https://www.'+domain_name+'/', 5 , 'en')
    except Exception as e:
        print("\t \t LIFE IS FULL OF UNPREDICTION AND HERE COMES ONE \t",e)
    try:
        
        for i in range(len(a)):
            f = urllib.request.urlopen(a[i])
            s = f.read().decode('utf-8')
            k =(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s))
            for i in range(len(k)):
                if(k[i] not in email_list):
                    email_list.append(k[i])
                    sql = "INSERT INTO email_domain (domain_name,email) VALUES (%s,%s)"
                    value = (domain_name,k[i])
                    mycursor.execute(sql, value)
                    mydb.commit()
#                     print(mycursor.rowcount, "record inserted.")
                else:
                    pass
        print("These are the emails",email_list)
    except Exception as e:
        print("These are the emails",email_list)
        pass
    






# In[5]:





# In[6]:


print(mydb) 


# In[3]:


mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")


# In[ ]:




