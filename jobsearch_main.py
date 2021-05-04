##Program to deal with job search, to show an overwiew of open roles and which requirements each role are asking for
##The idea is to be prepared for the most requested technologies and put in practice how to develop a full APi from scratch

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd 
from time import sleep

driver = webdriver.Chrome("JobsSearchAPI\chromedriver.exe")
city_search = "dublin"
job_role = "software-developer" #Insert a "-" between empty spaces
type_of_role = "contract" #fulltime/parttime/contract/internship/temporary/apprenticeship/entrylevel
type_of_role_dict = {
    "fulltime":"Full-time",
    "parttime":"Part-time",
    "contract":"Contract",
    "internship":"Intern/Trainee",
    "temporary":"Temporary",
    "apprenticeship":"Apprenticeship",
    "entrylevel":"Entry level"
}
driver.get("https://www.glassdoor.ie/Job/{}-{}-jobs-SRCH_IL.0,6_IC2739035_KO7,25.htm?jobType={}".format(city_search,job_role,type_of_role))
try:
    actual_open_roles = driver.find_element_by_xpath('.//*[@id="PrimaryDropdown"]/ul//label[text()={}]//following-sibling::*').text.format(type_of_role_dict[type_of_role])
    #.format(type_of_role_dict[type_of_role])
except NoSuchElementException:
    actual_open_roles = -1

try:
    number_open_roles = driver.find_element_by_xpath('.//*[@id="PrimaryDropdown"]/ul//label[text()={"css-18lin6p ew8xong1"}]//following-sibling::*').text
   
except NoSuchElementException:
    number_open_roles = -1

    #//*[@id="PrimaryDropdown"]/ul
    #//*[@id="PrimaryDropdown"]/ul/li[2]/span[1]/span







sleep(10)
driver.close()



