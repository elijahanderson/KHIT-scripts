from datetime import date, datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


def main():
    next_month = (date.today().replace(day=28) + timedelta(days=4)).replace(day=1).strftime('%m/%d/%Y')
    two_months = (datetime.strptime(next_month, '%m/%d/%Y').replace(day=28) + timedelta(days=4)).replace(day=1)\
        .strftime('%m/%d/%Y')

    driver = webdriver.Chrome(executable_path='C:\\Users\\mingus\\AppData\\Local\\chromedriver.exe')
    driver.get('https://myevolvacmhcxb.netsmartcloud.com/')
    driver.find_element_by_id('MainContent_MainContent_userName').send_keys('khit')
    driver.find_element_by_id('MainContent_MainContent_password').send_keys('Ton8dot4$$')
    driver.find_element_by_id('MainContent_MainContent_btnLogin').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/ul/li[18]/span').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/div[5]/div/div[1]/ul/li[3]').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/div[5]/div/div[2]/ul[2]/li[25]').click()
    driver.switch_to.frame(driver.find_element_by_xpath
                           ('/html/body/form/div[3]/div[2]/div[2]/div/div[16]/div/div/div/div/iframe'))
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/iframe[24]'))
    driver.implicitly_wait(15)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[2]/div[2]/div/input')\
        .send_keys(two_months)
    sleep(5)
    # driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[3]/div[2]/div/span').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[3]/div[2]/div') \
        .send_keys('Order by: Worker Name')
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[4]/div[2]/span/input').click()

    sleep(20)


main()
