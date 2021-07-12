# Vaccine_crawler
made by `Kai Chuang`

## Project Structure

```
.
├── emailSender.py
├── README.md
├── vaccine_crawler.py
├── vaccine_for_cgh.log (will be create when running)
├── vaccine_for_mmh.log (will be create when running)
└── vaccine_for_mmh.py
```

* emailSender.py - Define the google email notification
* vaccine_crawler.py - Define the function of cgh
* vaccine_for_mmg.py - Define the function of mmh

## Install Chrome in Ubuntu (Optional if you have Chrome)
```bash=
# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome-stable_current_amd64.deb

# If run Chrome get error
sudo apt-get install -f

# I found the error "Unable to open X display"
# Hense additional Lib I install
sudo apt-get install -y xvfb

sudo apt-get -y install xorg xvfb gtk2-engines-pixbuf
sudo apt-get -y install dbus-x11 xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable

sudo apt-get -y install imagemagick x11-apps

# run the setting
Xvfb -ac :99 -screen 0 1280x1024x16 &
export DISPLAY=:99

# run and check it is run smoothly
google-chrome
```
> Reference from: https://stackoverflow.com/questions/60304251/unable-to-open-x-display-when-trying-to-run-google-chrome-on-centos-rhel-7-5


After that, we run the google chrome will be show like this:

![](https://i.imgur.com/LRfl0eh.png)

We can ignore these error code, and move on.

## Install Chromedriver
* Where to install: https://sites.google.com/a/chromium.org/chromedriver/downloads
* **Check the chrome version in your machine, install chromedriver with the corresponding version in Chrome.**
* After install, move chromedriver in specified path (where you want to store in)
```bash=
# in mac
mv chromedriver /usr/local/bin/

# in ubuntu
mv chromedriver /usr/bin
```
## Install selenium
```bash=
pip install selenium
```

If using Conda environment, we can choose to use `conda install selenium`


## Import the requirements
> import selenium in python and specify the position of webdriver

```python=
from selenium.webdriver import Chrome

# Specify the address of chromedriver
driver = Chrome("/usr/local/bin/chromedriver")
```

We can run the chromedriver and make sure it is available.

![](https://i.imgur.com/no1piMY.png)

## Run the python
After completed the py, we run it.

```bash=
python YOUR_PYTHON_FILE
```

It will show as below, and we complete all setting!

![](https://i.imgur.com/kOMj6Gu.png)

## Using Crontab to run batch
```bash=
# list the crontab
crontab -l
# edit the crontab
crontab -e

# After below command, you will enter the edit layout
*/15 * * * * [PYTHON_ABSOLUTE_PATH] [YOUR_CODE_ABSOLUTE_PATH] 

# for exmaple, run it every 15 min
*/15 * * * * /home/server/anaconda3/envs/crawler/bin/python /home/server/projects/selenium_crawler/vaccine_crawler.py
```

## python_dotenv
### Install the python_dotenv
```bash=
pip install python_dotenv
```

Use to store some sensitive data into .env, where will be found in emailSender.py

## Reference:
Python Mail

https://www.learncodewithmike.com/2020/02/python-email.html

Selenium Reference

https://medium.com/marketingdatascience/selenium教學-一-如何使用webdriver-send-keys-988816ce9bed

https://medium.com/seaniap/用python控制chrome瀏覽器-selenium初體驗-732929668ce3

Python Log

https://shengyu7697.github.io/python-logging/
