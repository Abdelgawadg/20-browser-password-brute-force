#### Stucknet ####
Code is used for the brute forcing of passwords of raypec tyler sis users who are in the classes of 2021 and 2023.

This is done through a few small oversights.
The idea is that if you were to brute force you would need both the username and password, but this does not work.
The first is that you can find usernames though gmail's auto filling of emails. This eliminates the need for the username to be guessed.
The second is that there is a simple password protocol that is (mostly) consistent.
The password protocol is somewhat different though different years but they all follow the same scheme.
The protocol for the class of 21 is "rp21" + 4 random characters, and the freshman class is the same but with "bike" instead.
This reduces the amount of password possibilities to 10,000, and that isn't too hard to guess all of those.
The last big issue is the security from Tyler SIS. They do not have a captcha or anything to stop someone from guessing 10,000 different passwords (if this changes it would still be possible to exploit with software like linkens sphere).
All of these combined makes it easy to get the password for students and then later use it to get access to any school account they have.

Run this with the most recent version of python and windows (works with different OS but is done differently).
You need the selenium library installed (use "pip install selenium" in the windows command prompt).
Additionally a chrome webdriver is needed (https://chromedriver.chromium.org/downloads) and google chrome installed.
The code is created for google chrome but can be used with other browsers with some small code changes.
If you want to gives changes/ideas feel free to add them to current_version with comments to explain the code, I would love to learn.

I recommend reading the base_code first for getting an understanding of the code used.
The base_code is the first working version of the code that could be used to brute force.
The base_code is reused in later versions with some changes to how it works and bigger changes to how its used.


current_version can be a little confusing but is mostly just the same thing copy and pasted 20 times.
This is the version of the code that works best and has all the latest features. 
The goal for this project is to get every/most passwords cracked in less than 30 minutes.
This is done through the use of 20 browsers to cycle the loading times and increase the speed of the program.
I understand that the project is a bit unpolished and could be optimized, I am still fairly new to programming.

For contact send an email to abdelgawadg@att.net
