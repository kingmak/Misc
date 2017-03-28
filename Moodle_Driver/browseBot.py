#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time, platform, getpass


'''
# = code comment
## = code description
### = ?


Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:	https://github.com/mozilla/geckodriver/releases | webdriver.Firefox()
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

- download all browsers
- design UI for browser choice, cred entering? [remove the cred from file stuff]
- display subjects in UI?
- make google events?
- Full Page Screen shots = [http://stackoverflow.com/questions/40647038/how-to-take-full-page-screenshot-in-chrome-and-safari-browser-using-java-seleniu
							http://stackoverflow.com/questions/3422262/take-a-screenshot-with-selenium-webdriver?rq=1
							http://stackoverflow.com/questions/6740467/taking-a-fullpage-screenshot-using-selenium-server-in-python?rq=1
							http://stackoverflow.com/questions/8918026/selenium-webdriver-python-side-by-side/9089673#9089673
							http://stackoverflow.com/questions/10947101/how-to-capture-screenshot-in-selenium-webdriver-using-java-without-window-being?rq=1
							http://stackoverflow.com/questions/13158083/take-a-full-page-screenshot-with-firefox?rq=1
							http://stackoverflow.com/questions/13832322/how-to-capture-the-screenshot-of-a-specific-element-rather-than-entire-page-usin?rq=1
							https://gist.github.com/elcamino/5f562564ecd2fb86f559]
'''

## Determine OS

## Determine Browser
#browser = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'chromedriver'))

## parse tex to get subject name, assignment name and assignment due date
def parseSubject(text):
	assign, name, due = text.split('\n')[:3]

	print 'Subject    : %s' % name
	print 'Assignment : %s' % assign
	print 'Due Date   : %s' % due

	if len(text.split('\n')) > 3:
		other = '\n'.join(text.split('\n')[3:])
		print 'Other:\n%s' % other

## get user credentials
#user, Pass = [line.strip() for line in open('creds').readlines()]
user = raw_input('Enter Your UMN Username: ')
Pass = getpass.getpass('Enter Your UMN Password: ')
print ''

## Tags, Links
userTag = 'username'
passTag = 'password'
home = 'http://moodle.umn.edu'
calendar = 'https://ay16.moodle.umn.edu/calendar/view.php'

browser = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'Linux/chromedriver'))
#browser = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'Win/chromedriver')) 
browser.get(home) # moodle homepage

elem = browser.find_element_by_id(userTag)
elem.send_keys(user) # enter username

elem = browser.find_element_by_id(passTag)
elem.send_keys(Pass) # enter password

time.sleep(1)
elem.send_keys(Keys.RETURN) # click Enter, submit

time.sleep(3)
browser.get(calendar) # navigate to moodle calendar page
#browser.save_screenshot('screenie.png') ## find a way TODO FULL PAGE SCREENSHOTS

time.sleep(1)
subjects = browser.find_element_by_class_name('eventlist')

for subject in subjects.find_elements_by_class_name('event'):
	parseSubject(subject.text)
	print '-------------------------------------\n'

time.sleep(1)
browser.close() # this closes the browser
print 'Done'
