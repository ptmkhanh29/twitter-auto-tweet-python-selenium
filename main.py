import time
import pyautogui
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import threading
import sys
from logger import Logger

url_twitter_login = 'https://twitter.com/i/flow/login'

class TwitterBot():
    def __init__(self, user_name, password, start, end, phone_number):
        self.user_name = user_name
        self.password = password
        self.start = start
        self.end = end
        self.phone_number = phone_number
        self.verify_tweet_content()

        # Configure ChromeOptions
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"],
        )
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)

        # Open Chrome
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url_twitter_login)
        self.wait = WebDriverWait(self.driver, 60)
        self.login()

    def login(self):
        """
            Method for signing in the user with the provided username and password.
            Flow login:
                1. Send username -> click button Next
                2. Wait for the password input to appear, then send password -> click button Login
            Please update login methods accordingly as the HTML and CSS of the website may change.
        """
        username = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
        )
        username.send_keys(self.user_name)

        login_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
        )
        login_button.click()
        time.sleep(5)

        password_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=current-password]'))
        )
        password_input.send_keys(self.password)

        login_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
        )
        login_button.click()

        #! Handle the case where phone number verification is required
        logger = Logger(f"Login Verify Number")
        try:
            self.verify_phone_number()
            print(f"Phone number verified for account {self.user_name}")
        except TimeoutException:
            print(f"No phone number verification needed account {self.user_name}")

        wait_login_success = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0"]')))
        
        logger = Logger(f"Login")
        print(f"Tweet text area is visible now. Login sucess for account {self.user_name}")
        
        time.sleep(5)
        self.auto_tweet()

    def verify_phone_number(self):
        # Wait for the phone number input to appear and enter the phone number
        phone_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]'))
        )
        phone_input.send_keys(self.phone_number)

        # Click the 'Next' or 'Verify' button
        verify_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="ocfEnterTextNextButton"]'))
        )
        verify_button.click()

    def logger(self, number, content_tweet):
        green = '\033[92m'
        orange = '\033[93m'
        light_cyan = '\033[96m'
        reset = '\033[0m'

        print('*' * 100)
        print(f"***     Tweet {number} has been posted successfully.")
        for line in content_tweet.split('\n'):
            print(f"***     {line}")
        print(f'*' * 100)

    def verify_tweet_content(self):
        logger = Logger(f"Check Content Tweet")
        with open("tweet_content.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace("%number%", str(self.end))
        
        if len(content)> 280:
            print(f"Nội dung tweet đang vượt quá 280 kí tự ({len(content)} kí tự), vui lòng sửa lại content")
            print(content)
            sys.exit(1)

    def read_content(self, number):
        with open("tweet_content.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace("%number%", str(number))
        return content

    def auto_tweet(self):
        logger = Logger(f"Automation Tweet Account {self.user_name}")
        start_time = time.time()
        for number in range(self.start, self.end):
            try:
                tweet_box = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0"]'))
                )
                tweet_content = self.read_content(number)
                tweet_box.send_keys(tweet_content)
                time.sleep(1)
                try:
                    tweet_button = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="tweetButtonInline"]'))
                    )
                    tweet_button.click()
                    self.logger(number, tweet_content)
                except TimeoutException:
                    print(f"Post Tweet button was not visible after 20 seconds. The bot will skip post number {number} and tweet the next post")
                except NoSuchElementException:
                    print(f"Post Tweet button could not be found. The bot will skip post number {number} and tweet the next post")
                time.sleep(2)
            except TimeoutException:
                print(f"Tweet box was not visible after 20 seconds. The bot will skip post number {number} and tweet the next post")
            except NoSuchElementException:
                print(f"Tweet box could not be found. The bot will skip post number {number} and tweet the next post")

        end_time = time.time()  # End timing after the loop finishes
        total_time = end_time - start_time  # Calculate total time taken
        total = self.end - self.start
        print(f"Total time to auto tweet {total} rep: {total_time:.2f} seconds")

def process_account(account):
    username = account['username']
    password = account['password']
    start = account['start']
    end = account['end']
    phone_number = account['verify_phone_number']
    TwitterBot(user_name=username, password=password, start=start, end=end, phone_number=phone_number)

def main():
    """
    with open("accounts_info.json") as file:
        database = json.load(file)
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <json_data>")
        sys.exit(1)
    json_data = sys.argv[1]
    account_data = json.loads(json_data)

    threads = []
    for account in account_data["Account"]:
        if account["status"] == "Free":
            thread = threading.Thread(target=process_account, args=(account,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()