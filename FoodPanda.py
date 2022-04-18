# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:29:37 2021

@author: DSC-2019-007
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time 
import csv 

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome()
chrome.maximize_window()

# 網址、地址
url = "https://www.foodpanda.com.tw/"
df = pd.read_excel('北捷地址2.xlsx')


# 爬蟲Go
for add in df['地址']:
    
    times = 0
    
    # 建檔
    csvfile = open('FoodPanda_北捷_' + add[:7] + str(time.strftime('%Y%m%d%H%M')) + '.csv', 'a', newline='', encoding='utf_8_sig')
    writer = csv.writer(csvfile)
    writer.writerow(['廠商名稱', '廠商地址', '食品業者登錄字號'])

    chrome.get(url)
     
    time.sleep(1)
    
    # 熊貓輸入地址
    element1 = chrome.find_element_by_xpath("/html/body/div[13]/div[1]/main/div/div[2]/div[3]/form/div[1]/div[1]/input")
    element1.click()
    element1.send_keys(Keys.CONTROL+'a') # 全選刪除
    element1.send_keys(Keys.DELETE)
    element1.send_keys(add)
    time.sleep(0.5)
    
    button1 = chrome.find_element_by_xpath("/html/body/div[13]/div[1]/main/div/div[2]/div[3]/form/div[2]/button[1]")
    button1.click()
    time.sleep(1)
    
    # 看頁面 <1000筆:range(100)。 >1000筆:range(200)。 >3000筆:range(300)
    for roll in range(300): 
        chrome.execute_script("window.scrollTo({top: 1,behavior: 'smooth'})")
        chrome.execute_script("window.scrollTo({top: 999999,behavior: 'smooth'})")
        time.sleep(0.5)
    
    chrome.execute_script("window.scrollTo({top: 1,behavior: 'smooth'})")
    time.sleep(1)
    
    # 計算所有店家數量
    links = chrome.find_elements_by_css_selector("div[class^='infinite-scroller'] section ul li a")  # 獲取到所有li標籤數量
    length = len(links) # 產品數量
    print("商家數量 : ",length)
    
    time.sleep(0.5)
    
    # 記錄全網址
    soup = BeautifulSoup(chrome.page_source,"html.parser")
    u = soup.select('div.infinite-scroller section ul li a') 
    
    # 進入每一個網址抓店名、地址、登錄字號
    for k in range(0,length):

        time.sleep(0.5)
        
        firm_name = '無資料'   # 廠商名稱
        firm_add = '無資料'    # 廠商地址
        firm_id = '無資料'     # 食品業者登錄字號
        
        time.sleep(0.5)
        
        u_1 = "https://www.foodpanda.com.tw"+u[k]["href"]
        chrome.get(u_1)
        
        time.sleep(0.5)
        try: # 不需要按關閉選項
            chrome.find_element_by_xpath("/html/body/div[15]/div[1]/main/div[2]/section/div[1]/div[3]/div/div[4]/span").click()
            firm_name = chrome.find_element_by_xpath("/html/body/div[15]/div[1]/main/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/h1").text
            try: # 兩種存放路徑
                firm_add = chrome.find_element_by_xpath("/html/body/div[15]/div[1]/main/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div/div[1]/p").text
            except: # 兩種存放路徑
                firm_add = chrome.find_element_by_xpath("/html/body/div[15]/div[1]/main/div[2]/div[2]/div/div/div[1]/div[3]/p").text
        
            if '登錄字號' in firm_add:
                firm_id = firm_add[firm_add.find('字號')+2:]
                firm_add = firm_add[:firm_add.find('號')+1]
            
            print(firm_name,firm_add,firm_id)
            writer.writerow([firm_name, firm_add, firm_id])
        
            times += 1
        
            print("# 已完成",times,"/",length," #")
            time.sleep(0.5)
            
            pass
        
        except:# 按關閉按鈕
            try: 
                time.sleep(1)
                chrome.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/button").click()
            
                chrome.find_element_by_xpath("/html/body/div[15]/div[1]/main/div[2]/section/div[1]/div[3]/div/div[4]/span").click()
                firm_name = chrome.find_element_by_xpath("/html/body/div[15]/div[1]/main/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/h1").text
                firm_add = chrome.find_element_by_xpath("/html/body/div[15]/div[1]/main/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div/div[1]/p").text
        
                if '登錄字號' in firm_add:
                    firm_id = firm_add[firm_add.find('字號')+2:]
                    firm_add = firm_add[:firm_add.find('號')+1]
            
                print(firm_name,firm_add,firm_id)
                writer.writerow([firm_name, firm_add, firm_id])
        
                times += 1
        
                print("# 已完成",times,"/",length," #")
                time.sleep(0.5)
                
            except: # 選單頁面，無任何資訊
                times += 1

                print("# 已完成",times,"/",length," #")
                
                pass
            
            
            
    csvfile.close()
    
chrome.close()