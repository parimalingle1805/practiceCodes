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



hashtag_list = ['webdevelopment','webdeveloper']#,'frontend','webdevelopment','mern','fullstackdeveloper','nodejs','expressjs']

prev_user_list = ['parimalingle1805'] # if it's the first time you run it, use this line and comment the two below
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for Hash in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ Hash + '/')
    sleep(3)
    thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a')
    thumbnail.click()
            
    for i in range(100):      
        try:        
            username = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
            #print(webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').get_attribute("fill"))    
            if username not in prev_user_list:
                    # If we already follow, do not unfollow
                if webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        
                    webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        
                    new_followed.append(username)
                    followed += 1
                    print("followed: ", followed)
                        
                        # Liking the picture
            source = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div')
                                                        
            action = ActionChains(webdriver)
            action.double_click(source).perform() 
            likes += 1
            print("liked: ",likes)
            sleep(2)
            
            
            #Next
            webdriver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
            sleep(2) 
                    
        except:
            continue
        sleep(5)

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))