from selenium.webdriver import Chrome
from selenium import webdriver
import emailSender as es
import time
import logging
import os
from dotenv import load_dotenv

def main(driver):
    # Load dotenv
    load_dotenv()

    to = os.getenv("RECEIVER_EMAIL")

    mmh_url = "https://mcloud.mmh.org.tw/DMZWEBHEALTHNUMA651/EMWAITdefault_N.aspx?HOSP=1WAIT"
    driver.get(mmh_url)

    if (driver.find_element_by_id('LblFull').text != '預約取號已額滿，依施打進度再公布下一階段開放預約取號時間。'):
        # Send the Notification
        title = "馬偕殘劑預約變動"
        receiver = to
        body = "爬蟲偵測程式發現，馬偕殘劑網頁已發生變動\n 趕快去看: https://wapps.mmh.org.tw/webhealthnumber/EMWAITdefault.aspx?HOSP=1WAIT"
        es.emailConfig(title, receiver, body)

        # Logging
        logging.info('Found Changed')
    else:
        # Show the time and msg
        localtime = time.localtime()
        result_t = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        print("No Change in %s" % result_t)

        # Logging
        logging.info('No Change')

    # close the chrome
    driver.quit()

if __name__ == '__main__':
    # run in background
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')

    driver = Chrome(options=options, executable_path="/usr/local/bin/chromedriver") # 暫時換掉位置，linux沒有local

    # Logging set up
    # setting the logging
    logname = '/home/kai_server/projects/selenium_crawler/vaccine_for_mmh.log'
    logging.basicConfig(filename=logname,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        level=logging.INFO)

    try:
        main(driver)
    except Exception as e:
        print(e)
        logging.error(e)
        driver.quit()
