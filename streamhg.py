# streamhg.py
import time
import threading
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
link_list = [
    "https://gradehgplus.com/nqtgnz8x2dx9",
    "https://gradehgplus.com/hfip1hmdbutz",
    "https://gradehgplus.com/gd466mm36ade",
    "https://gradehgplus.com/86pbb3fb14i2",
    "https://gradehgplus.com/j8edjxkcfz7y",
    "https://gradehgplus.com/f0bm2v25r7jl",
    "https://gradehgplus.com/gd7t22p8s8jb",
]
selected_links = random.sample(link_list, 3)

def run_browser(thread_id, url):
    while True:
        print(f"Thread-{thread_id}: Starting session for {url}")
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            ua = UserAgent()
            options.add_argument(f"user-agent={ua.random}")
            options.add_argument('--start-maximized')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')

            driver = uc.Chrome(options=options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.get(url)
            time.sleep(5)

            start_time = time.time()
            while time.time() - start_time < 420:
                try:
                    play_button_xpath = '//div[@aria-label="Play"]'
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, play_button_xpath)))
                    play_button = driver.find_element(By.XPATH, play_button_xpath)
                    play_button.click()
                    time.sleep(5)
                except Exception as e:
                    print(f"Thread-{thread_id}: Play error: {e}")
                time.sleep(random.randint(10, 30))

            driver.quit()
        except Exception as e:
            print(f"Thread-{thread_id}: Unexpected error: {e}")
            time.sleep(10)

def run_streamhg_parallel():
    threads = []
    for i, link in enumerate(selected_links):
        t = threading.Thread(target=run_browser, args=(i, link))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
