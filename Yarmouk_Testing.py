from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
def last_page_rounting():
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[3]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[4]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[5]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[6]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[7]/td[1]/a/img').click()
def Page_rounting():
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[3]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[4]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[5]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[6]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[7]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[8]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[9]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[10]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[11]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[12]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[13]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[14]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[15]/td[1]/a/img').click()
    #time.sleep(2)
    driver.back()
    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[3]/td/table/tbody/tr[16]/td[1]/a/img').click()
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
def test_login():
    driver.get("https://sis.yu.edu.jo/pls/yuapps/f?p=134:101:134314919725436:::::")
    driver.find_element(By.ID,'P101_USERNAME').send_keys('Write your id here')
    driver.find_element(By.ID, 'P101_PASSWORD').send_keys('Write your password here')
    driver.find_element(By.XPATH, '//*[@id="apex_layout_174514236607584703"]/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/a').click()
    driver.switch_to.alert.accept()
    driver.find_element(By.XPATH,'//*[@id="wwvFlowForm"]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/a').click()
    driver.find_element(By.XPATH,'//*[@id="wwvFlowForm"]/table/tbody/tr[4]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td[3]/a[2]').click()
    x=Select(driver.find_element(By.XPATH,'//*[@id="P2_FCY"]'))
    x.select_by_visible_text('الحجاوي للهندسه التكنولوجيه')
    y=Select(driver.find_element(By.XPATH,'//*[@id="P2_DPT"]'))
    y.select_by_visible_text('هندسة الحاسوب')
    driver.find_element(By.XPATH,'//*[@id="R174811322298472984"]/tbody/tr[3]/td[2]/table[2]/tbody/tr/td/table[1]/tbody/tr/td[2]/a').click()
    #First page
    Page_rounting()

    driver.back()
    # Second page

    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[4]/td/table/tbody/tr/td[3]/span/a[1]').click()
    time.sleep(4)
    Page_rounting()
    # -----------------------------------------------------

    # back to main page
    driver.back()
    # Thired page

    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[4]/td/table/tbody/tr/td[3]/span/a[2]').click()
    time.sleep(4)
    Page_rounting()
    # back to main page
    driver.back()
    #fourth gage

    driver.find_element(By.XPATH,'//*[@id="report_R174780519416263975"]/tbody/tr[4]/td/table/tbody/tr/td[3]/span/a[3]').click()
    time.sleep(4)
    last_page_rounting()
    driver.find_element(By.XPATH,'//*[@id="wwvFlowForm"]/table/tbody/tr[5]/td/a[2]').click()

def close_test():
    driver.close()
    driver.quit()
    print("done")
