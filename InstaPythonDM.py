from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
from selenium.webdriver import ActionChains

import pandas as pd

chromedriver_path = 'C:/Users/Parimal/Downloads/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.maximize_window()

webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('parimalingle1805')
password = webdriver.find_element_by_name('password')
password.send_keys('lumia430ds')

button_login = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications



#hashtag_list = ['webdevelopment','webdeveloper']#,'frontend','webdevelopment','mern','fullstackdeveloper','nodejs','expressjs']

prev_user_list = [] # if it's the first time you run it, use this line and comment the two below
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0
followers = []
following = []

tag += 1
webdriver.get('https://www.instagram.com/parimalingle1805/')
sleep(2)
webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
sleep(3)

for i in range(1,50):
    followers.append(webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[2]/div[1]/div/div/span/a').text)
    recentList = webdriver.find_elements_by_xpath("/html/body/div[5]/div/div/div[2]")

    for list in recentList :
        webdriver.execute_script("arguments[0].scrollIntoView();", list)
print(followers)
#webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
#leep(3)

#for i in range(1,50):
 #   followers.append(webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[2]/div[1]/div/div/span/a').text)
  #  webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")






















for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))