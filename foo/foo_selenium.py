import os
import pandas as pd
import shutil

from datetime import date, datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


def join_datatables():
    tp_csv = pd.read_csv("C:/Users/mingus/Documents/treatment_due_dates.csv")
    pw_csv = pd.read_csv("C:/Users/mingus/Downloads/primary_workers.csv")

    tp_csv['name'] = tp_csv['name'].str.strip()
    pw_csv['name'] = pw_csv['name'].str.strip()

    merged = tp_csv.merge(pw_csv, on='name')
    merged.drop(['people_id', 'id_no', 'ssn_number', 'ssi_number', 'urn_no', 'dob',
                 'phone_day', 'phone_evening', 'aka', 'intake_date', 'discharge_date',
                 'client_status', 'ipd', 'service_track_id', 'gender', 'medicaid_number',
                 'current_location', 'program_enrollment_event_id', 'program_info_id',
                 'worker_assignment_id', 'worker_start', 'worker_end', 'staff_id',
                 'supervisor_id', 'supervisor_name_y', 'is_primary_worker', 'managing_office_id',
                 'managing_office', 'worker_number', 'unit_number', 'worker_unit', 'prg_days',
                 'last_date_serv', 'total_dist', 'grand_total_dist', 'worker_role', 'program_name'], axis=1,
                inplace=True)
    merged = merged.rename(columns={'worker_name': 'primary_worker'})
    merged['expiration_date'] = pd.to_datetime(merged.expiration_date)
    merged.sort_values(by=['primary_worker', 'expiration_date'], inplace=True, ascending=[True, True])
    merged.to_csv("C:/Users/mingus/Documents/" + str((date.today().replace(day=1) + timedelta(days=31)).month) + "-" +
                  str((date.today().replace(day=1) + timedelta(days=62)).month) + "-" +
                  str((date.today().replace(day=1) + timedelta(days=62)).year) + "_treatment_plan_due_dates.csv",
                  index=False)


def main():
    next_month = (date.today().replace(day=28) + timedelta(days=4)).replace(day=1).strftime('%m/%d/%Y')
    two_months = (datetime.strptime(next_month, '%m/%d/%Y').replace(day=28) + timedelta(days=4)).replace(day=1) \
        .strftime('%m/%d/%Y')

    driver = webdriver.Chrome(executable_path='C:\\Users\\mingus\\AppData\\Local\\chromedriver.exe')
    driver.get('https://myevolvacmhcxb.netsmartcloud.com/')
    driver.maximize_window()

    # login
    driver.find_element_by_id('MainContent_MainContent_userName').send_keys('khit')
    driver.find_element_by_id('MainContent_MainContent_password').send_keys('Ton8dot4$$')
    driver.find_element_by_id('MainContent_MainContent_btnLogin').click()

    # navigate to worker case loads (for clients' primary workers)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/ul/li[18]/span').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/div[5]/div/div[1]/ul/li[3]').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/div[5]/div/div[2]/ul[2]/li[25]').click()

    # navigate into the iframes and fill out the form
    iframe1 = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div/div[16]/div/div/div/div/iframe')
    driver.switch_to.frame(iframe1)
    iframe2 = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/iframe[24]')
    driver.switch_to.frame(iframe2)
    driver.implicitly_wait(15)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[2]/div[2]/div/input') \
        .send_keys(two_months)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[3]/div[2]/div/span').click()

    # switch back to default content for report selection
    sleep(3)  # TODO -- implicit wait sometimes causes ElementNotInteractable exception, fix later
    driver.switch_to.default_content()
    driver.switch_to.default_content()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/table/tbody/tr[3]/td[1]') \
        .click()

    # go back into iframe2 for checkbox
    driver.switch_to.frame(iframe1)
    driver.switch_to.frame(iframe2)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[4]/div[2]/span/input').click()

    # switch to parameters iframe
    iframe_params = driver \
        .find_element_by_xpath('/html/body/form/div[3]/div[2]/div[5]/div/div/div/div[4]/div[4]/div/div/iframe')
    driver.switch_to.frame(iframe_params)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/table/tbody/tr/td[2]/div/input')\
        .send_keys('Program' + Keys.TAB)
    sleep(2)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/table/tbody/tr[1]/td[4]/div/input')\
        .send_keys('Outpatient Mental Health' + Keys.TAB)
    sleep(2)

    # switch back to iframe1 for CSV button
    driver.switch_to.default_content()
    driver.switch_to.default_content()
    driver.switch_to.default_content()
    driver.switch_to.frame(iframe1)
    driver.switch_to.frame(iframe2)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/ul/li[17]/a').click()

    # rename the downloaded file
    sleep(5)
    path = 'C:\\Users\\mingus\\Downloads'
    filename = max([path + '\\' + f for f in os.listdir(path)], key=os.path.getctime)
    shutil.move(filename, os.path.join(path, r'primary_workers.csv'))

    # switch to default content to download the treatment plan custom report
    driver.switch_to.default_content()
    driver.switch_to.default_content()

    # navigate to custom reports
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/ul/li[18]/span').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/div[5]/div/div[1]/ul/li[2]').click()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[1]/div[1]/div[5]/div/div[2]/ul[1]/li[2]').click()

    # switch to appropriate iframe
    driver.implicitly_wait(15)
    cr_iframe1 = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div/div[16]/div/div/div/div/iframe')
    driver.switch_to.frame(cr_iframe1)
    cr_iframe2 = driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/iframe')
    driver.switch_to.frame(cr_iframe2)
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a').click()
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[2]/a').click()
    sleep(1)

    # new tab
    driver.switch_to.default_content()
    driver.switch_to.default_content()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath(
        '/html/body/form/span[2]/span[2]/mainbody/span/span/div/table/tbody/tr[1]/td/span/table/tbody/tr[1]/td[2]/'
        'span[1]/input[1]'
    ).send_keys(next_month)
    driver.find_element_by_xpath(
        '/html/body/form/span[2]/span[2]/mainbody/span/span/div/table/tbody/tr[1]/td/span/table/tbody/tr[1]/td[2]/'
        'span[2]/input[1]'
    ).send_keys(two_months)
    driver.find_element_by_xpath(
        '/html/body/form/span[2]/span[2]/mainbody/span/span/div/table/tbody/tr[2]/td/a[1]/input').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(
        '/html/body/form/span[2]/span[2]/span[1]/rdcondelement10/span/rdcondelement9/span/a/img').click()

    # rename the downloaded file
    sleep(2)  # wait for download
    filename = max([path + '\\' + f for f in os.listdir(path)], key=os.path.getctime)
    shutil.move(filename, os.path.join(path, r'treatment_due_dates.csv'))

    driver.close()


main()
