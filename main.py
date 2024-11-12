from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере
driver_chrome.get(base_url)

# команда для открытия окна в максимальном для монитора разрешении
driver_chrome.maximize_window()

# найти на странице элемент "user-name" через id
# user_name = driver_chrome.find_element(By.ID, "user-name")

# найти на странице элемент "user-name" через NAME
# user_name = driver_chrome.find_element(By.NAME, "user-name")

# найти на странице элемент "user-name" через кастомный локатор XPATH
# user_name = driver_chrome.find_element(By.XPATH, "//*[@id='user-name']")

# найти на странице элемент "user-name" через копирование XPATH
# user_name = driver_chrome.find_element(By.XPATH, "//*[@id='user-name']")

# найти на странице элемент "user-name" через копирование full XPATH
# user_name = driver_chrome.find_element(
#     By.XPATH,
#     "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input"
# )

# найти на странице элемент "user-name" через кастомный локатор XPATH
# с применением тега input
user_name = driver_chrome.find_element(
    By.XPATH,
    # "//input[@id='user-name']"
    # "//input[@placeholder='Username']"
    "//input[@data-test='username']"
)


# поиск локатора по индексу
# (//div[@class="form_group"])[1]

# поиск локатора по тексту, точное значение
# //h4[text()='Password for all users:']

# поиск локатора по тексту, частичное значение
# //h4[contains(text()='Password for all users:')]


# установить в поле значение "standard_user"
user_name.send_keys("standard_user")

sleep(5)
driver_chrome.close()
