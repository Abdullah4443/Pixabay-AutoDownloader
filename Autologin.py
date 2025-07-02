from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import urllib.request
import time

driver = webdriver.Chrome()
driver.get('https://pixabay.com/')
time.sleep(2)
btn_login=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/header/div/div[2]/div[2]/button')
btn_login.click()
time.sleep(2)
input_field1 = driver.find_element(By.NAME, 'login_user')
input_field2 = driver.find_element(By.NAME, 'login_pass')
time.sleep(2)
input_field1.send_keys('Abdullah323862@gmail.com')
time.sleep(2)
input_field2.send_keys('Abdullah3238')
time.sleep(2)
btn_login=driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/div[2]/div/div/div/div[2]/form/div[5]/button')
time.sleep(2)
btn_login.click()
time.sleep(2)

driver.get("https://pixabay.com/photos/duck-water-bird-swim-flying-9536937/")
time.sleep(2)
# Download image with headers using urllib
image_url = "https://cdn.pixabay.com/photo/2025/04/16/06/25/duck-9536937_1280.jpg"

req = urllib.request.Request(
    image_url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://pixabay.com/'
    }
)

with urllib.request.urlopen(req) as response, open("duck_image.jpg", 'wb') as out_file:
    data = response.read()
    out_file.write(data)

print("✅ Image downloaded using urllib with headers!")

time.sleep(5)

driver.get("https://pixabay.com/photos/nature-landscape-flower-plant-9659850/")
time.sleep(2)
image_url = "https://cdn.pixabay.com/photo/2025/06/14/17/27/nature-9659850_1280.jpg"
req = urllib.request.Request(
    image_url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://pixabay.com/'
    }
)
with urllib.request.urlopen(req) as response, open("flower_image.jpg", 'wb') as out_file:
    data = response.read()
    out_file.write(data)

print("✅ Image downloaded using urllib with headers!")

time.sleep(5)



driver.get("https://pixabay.com/photos/lavender-field-landscape-field-9659072/")
time.sleep(2)
image_url = "https://cdn.pixabay.com/photo/2025/06/14/06/23/lavender-field-9659072_1280.jpg"
req = urllib.request.Request(
    image_url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://pixabay.com/'
    }
)
with urllib.request.urlopen(req) as response, open("field_image.jpg", 'wb') as out_file:
    data = response.read()
    out_file.write(data)

print("✅ Image downloaded using urllib with headers!")

time.sleep(5)
driver.quit()

