"""Задание: загрузка файла
Напишите скрипт, который будет выполнять следующий сценарий:

-- Открыть страницу http://suninjuly.github.io/file_input.html
--Заполнить текстовые поля: имя, фамилия, email
--Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
--Нажать кнопку "Submit" """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"


def test():
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(3)
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("Vanya@gmail.com")

    # ищем путь к файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(5)
    browser.quit()
