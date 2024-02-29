# Generated by Selenium IDE
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pymongo import MongoClient 
import sys
import streamlitform

#mongo_url="mongodb://localhost:27017"
mongo_url="mongodb+srv://ShreeshaShetty:Shreesha7%40@cluster0.ldusz7x.mongodb.net/"
mongo_db=MongoClient(mongo_url)
print(mongo_db.list_databases)

#create db
db=mongo_db["TestLogs"]

driver = webdriver.Chrome()
  
#driver.get("http://localhost/testweb1/index.php")
driver.get("http://dummymensapparel.great-site.net/itemcategory.php?catid=1")
driver.set_window_size(1552, 832)
#driver.find_element(By.CSS_SELECTOR, ".catg:nth-child(3) img").click()
with open("testcaseoptions.txt", "r") as file:
    arr = file.read()
#arr=streamlitform.selected_options
for i in range(0,len(arr)):
    if i==len(arr)-1:
        driver.find_element(By.CSS_SELECTOR, ".brands:nth-child("+str(int(arr[i])+2)+") img").click()
        driver.find_element(By.LINK_TEXT, "Add To Bag").click()
        driver.find_element(By.CSS_SELECTOR, "h4").click()
    else:
        driver.find_element(By.CSS_SELECTOR, ".brands:nth-child("+str(int(arr[i])+2)+") img").click()
        driver.find_element(By.LINK_TEXT, "Add To Bag").click()
        driver.find_element(By.CSS_SELECTOR, "h4").click()
        driver.back()
        driver.back()

get_text=driver.find_element(By.ID, "cartcount").text
print(get_text)
print("Items in Cart:",len(arr))
if str(len(arr)) in get_text:
#if get_text == "Items in Cart: "+str(len(arr)):
    t1="Item added to cart Succesfully!!"
    stat="Pass"
else:
    t1="Add to Cart Unsuccesfull :("
    stat="Fail"
    
#delete items added by test case
for z in range(len(arr)):
    driver.find_element(By.ID, "removeitem").click()
driver.close() 

ts=datetime.datetime.now()
date_time=ts.strftime("%d-%m-%Y, %H:%M:%S")
f = open("file2.txt", "a")
f.write("\nTest Case on Add to Cart")
f.write("\n"+date_time+"   Run 1:"+"\t"+t1)
f.close()

db = mongo_db.TestLogs
coll = db.TestColl
cursor = coll.find({"TestName": "Add Item to Cart"}).sort('id', -1).limit(1)[0]
print(cursor)
data=dict()

data["id"]=int(cursor["id"]) + 1
data["TestName"]="Add Item to Cart"
data["time"]=datetime.datetime.now()
data["Output"]=t1
data["status"]=stat
x=coll.insert_one(data)