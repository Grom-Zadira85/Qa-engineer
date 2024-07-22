#  Задание: поиск элемента по тексту в ссылке
"""
1)На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
2)Добавьте в самый верх своего кода import math
3)Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
4)Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
5)str(math.ceil(math.pow(math.pi, math.e)*10000))
(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат
и уже его использовать в вашем коде)
6)Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
7)Заполните скриптом форму так же как вы делали в предыдущем шаге урока
8)После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание.  """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

new_link = "http://suninjuly.github.io/find_link_text"
result = str(math.ceil(math.pow(math.pi, math.e) * 10000))
print(result)

try:
    browser = webdriver.Chrome()
    browser.get(new_link)
    link_find_link = browser.find_element(By.LINK_TEXT, result)
    link_find_link.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
