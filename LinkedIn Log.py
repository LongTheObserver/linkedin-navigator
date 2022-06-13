import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pyautogui
from concurrent.futures import ThreadPoolExecutor


def get_info():
    serv = Service(".//chromedriver.exe")
    driver = webdriver.Chrome(service=serv)
    driver.get("https://linkedin.com")
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='session_key']")))
    email.send_keys("hard code")
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='session_password']")))
    password.send_keys("hard code")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='sign-in-form__submit-button']"))).click()
    time.sleep(3)
    links = []
    driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B%22784652%22%5D&network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=G%3A6")
    driver.maximize_window()
    page = 1
    while page < 10:
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var "
                                          "lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while not match:
            lastCount = lenOfPage
            time.sleep(2)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var "
                                              "lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True
                break
        urls = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='entity-result__title-text t-16'] //a[@class='app-aware-link']")))
        for url in urls:
            link = url.get_attribute("href")
            links.append(link)
        page += 1
        next_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label= 'Page " + str(page) + "']")))
        actions = ActionChains(driver)
        actions.move_to_element(next_page)
        actions.click(on_element=next_page)
        actions.perform()
        time.sleep(2)
        driver.close()
    return links
    # page = 1
    # while page <= 10:"""


def send_message(client):
    serv = Service(".//chromedriver.exe")
    driver = webdriver.Chrome(service=serv)
    driver.get("https://linkedin.com")
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='session_key']")))
    email.send_keys("fbek49@gmail.com")
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='session_password']")))
    password.send_keys("ngomailinh93")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='sign-in-form__submit-button']"))).click()
    time.sleep(3)
    driver.get(client)
    name = WebDriverWait(driver, 6).until(EC.presence_of_element_located(
        (By.XPATH, "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']"))).text
    try:
        messenger = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//a[@class='message-anywhere-button pvs-profile-actions__action artdeco-button artdeco-button--secondary artdeco-button--muted ']")))
        messenger.click()
        subject = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//input[@name='subject']")))
        subject.send_keys("Hello " + name)
        text_box = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']")))
        text_box.send_keys("Sorry for my annoyance, this is a message from one of my marketing bot")
        time.sleep(2)
        send = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//div //button[@type='submit']")))
        send.click()
        time.sleep(3)
    except TimeoutException:
        print("Fail to send message to " + name)


get_info()