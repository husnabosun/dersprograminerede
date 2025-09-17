import os
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from dotenv import load_dotenv

load_dotenv()
password = os.getenv("PASSWORD")


URL = 'https://ceng.iyte.edu.tr/tr/anasayfa/haftalik-ders-programi/#second-year'

def get_chrome_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-software-rasterizer")

    return options

def login_site():
    options = get_chrome_options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    
    try:
        print('Waiting for the login...')
        driver.get(URL)

        print('Waiting for the title...')
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "stm-title"))
        )

        title_text = driver.find_element(By.CLASS_NAME, "stm-title").text
        print(f"Sayfa başlığı: {title_text}")

        if title_text != "2024-2025 Bahar Haftalık Ders Programı":
            sender = "bosunhusna@gmail.com"
            receiver = "bosunhusna@gmail.com"

            message = """\
            Subject: DERS PROGRAMI ACIKLANDIIIG !!!
            
            OLLEYYY!!!!
            """

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message)

            print("Mail gönderildi!")

    except Exception as e:
        print(f"An error occured during login: {e}")

    finally:
        driver.quit()
login_site()
