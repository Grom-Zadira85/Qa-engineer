"""Задание: поиск сокровища с помощью get_attribute

В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex
у картинки с изображением сундука.

===============шаги-----------------------
1)Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
2)Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
3)Посчитать математическую функцию от x (сама функция остаётся неизменной).
4)Ввести ответ в текстовое поле.
5)Отметить checkbox "I'm the robot".
6)Выбрать radiobutton "Robots rule!".
7)Нажать на кнопку "Submit".
"""
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '[src="images/chest.png"]')
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[type = "checkbox"]').click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    browser.quit()
