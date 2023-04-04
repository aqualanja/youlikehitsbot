from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule
import sys

sys.setrecursionlimit(9999)
# the class for manage bot's features
class YLH:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.options = Options()
        self.options.add_argument("--lang=en")
        self.options.add_argument("no-sandbox")
        self.options.add_argument("--headless")
        self.bot_ylh = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options = self.options)

    # this method open the login link, fill the form and click login button
    def open_link(self):
        bot_ylh = self.bot_ylh
        bot_ylh.get("https://www.youlikehits.com/login.php")
        username = bot_ylh.find_element(By.NAME, "username")
        username.send_keys(self.username)
        password = bot_ylh.find_element(By.NAME, "pass")
        password.send_keys(self.password)
        button = bot_ylh.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input").click()
        time.sleep(2)
        testBOT.ylh_loop()
        
    # this method loop the actions for earn point
    def ylh_loop(self):
        bot_ylh = self.bot_ylh
        bot_ylh.get("https://www.youlikehits.com/youtubenew2.php")
        time.sleep(2)

        try:
            time.sleep(2)
            bot_ylh.find_element(By.CLASS_NAME, "followbutton").click()
            time.sleep(2)
            
    # Break
        except:
            time.sleep(2)
            bot_ylh.get("https://www.youlikehits.com/stats.php")
            print("15 mins break")
            time.sleep(960)
            

        while len(bot_ylh.window_handles) > 1:
            time.sleep(1)
            print("By GiotWallet")

            time.sleep(135)
            bot_ylh.get("https://www.youlikehits.com/bonuspoints.php")
            time.sleep(2)

        try:
            time.sleep(2)
            bot_ylh.find_element(By.CLASS_NAME, "buybutton").click()
            print("Bonus collected!")

        except:
            time.sleep(2)
            bot_ylh.get("https://www.youlikehits.com/stats.php")
            print("Not enough clicks")
            time.sleep(2)
        
        testBOT.ylh_loop()


        

# here we start. Fill the line below with your Youlikehits username and your password
testBOT = YLH("username", "password")
testBOT.open_link()
