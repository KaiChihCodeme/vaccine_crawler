from selenium.webdriver import Chrome
from selenium import webdriver
import emailSender as es
import time
import logging
import os
from dotenv import load_dotenv

def main(driver, to):
    mmh_url = "https://mcloud.mmh.org.tw/DMZWEBHEALTHNUMA651/EMWAITdefault_N.aspx?HOSP=1WAIT"
    driver.get(mmh_url)

    if (driver.find_element_by_id('LblNotOpenInf').text != '預約取號已額滿，依施打進度再公布下一階段開放預約取號時間。'):
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

    driver = Chrome(options=options, executable_path="/usr/bin/chromedriver") # change if path changed

    # Logging set up
    # setting the logging
    logname = '/home/kai_server/projects/selenium_crawler/vaccine_for_mmh.log'
    logging.basicConfig(filename=logname,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        level=logging.INFO)

    # Load dotenv
    load_dotenv()
    to = os.getenv("RECEIVER_EMAIL")

    try:
        main(driver, to)
    except Exception as e:
        # write in log
        print(e)
        logging.error(e)

        # quit the chromedriver
        driver.quit()

        # notify
        title = "馬偕殘劑預約程式錯誤"
        receiver = to
        body = "馬偕殘劑程式發生錯誤\n 錯誤原因：%s" % e
        es.emailConfig(title, receiver, body)
