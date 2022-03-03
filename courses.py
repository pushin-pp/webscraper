from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import csv

#open and write csv files
filename = "CS_Classes.csv"
f = open(filename, "w", encoding="utf-8")

#excel headers
headers = "Class Code, Class Title, Credit Hours, Times, Professors"
f.write(headers)

#selenium webscraping driver
path = r"C:\Users\EP\Desktop\College\Sophomore\CS 370\Webscraper\chromedriver.exe"
driver = webdriver.Chrome(path)

#website
driver.get("https://atlas.emory.edu/")
print(driver.title)

#change term to specific semester/year
term = Select(driver.find_element_by_id("crit-srcdb"))
term.select_by_visible_text("Spring 2022")

#search for cs classes
search = driver.find_element_by_id("crit-keyword")
search.send_keys("cs")
search.send_keys(Keys.RETURN)

#add delay to wait for searches to load
time.sleep(1)

courses = driver.find_elements_by_class_name("result__link")

for course in courses:
    course.click()  #automate clicking through cs courses

    time.sleep(0.5)

    courseCode = driver.find_element_by_class_name("dtl-course-code")
    courseTitle = driver.find_element_by_css_selector(".col-8")
    courseHours = driver.find_element_by_css_selector(".detail-hours_html")
    print(courseCode.text + ' ' + courseTitle.text + ' | Credit Hours: ' + courseHours.text.split()[2])

    sections = driver.find_elements_by_class_name("course-section-mp")
    professors = driver.find_elements_by_class_name("course-section-instr")
    
    for i in range(len(sections)):
        print(sections[i].text + " " + professors[i].text)

        #write scraped data into CSV file
        f.write(
            courseCode.text + "," +
            courseTitle.text + "," +
            courseHours.text.split()[2] + "," +
            sections[i].text + "," +
            professors[i].text +
            '\n'
        )


    
f.close()
time.sleep(5)
driver.quit()