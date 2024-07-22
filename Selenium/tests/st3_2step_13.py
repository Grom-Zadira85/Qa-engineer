import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""Задание: оформляем тесты в стиле unittest 
Попробуйте оформить тесты из первого модуля в стиле unittest.

Шаги:
1)Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
2)Создайте новый файл
3)Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
4)Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
5)Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
6)Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
7)Запустите получившиеся тесты из файла 
8)Просмотрите отчёт о запуске и найдите последнюю строчку 
9)Отправьте эту строчку в качестве ответа на это задание 
10)Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. 
"""


class TestAbs(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration_page_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")

        input2 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")

        input3 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("Petrov@gmail.com")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")

        print(welcome_text_elt)
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        print(welcome_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, " текст не совпал ")

    def test_registration_page_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")

        input2 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")

        input3 = self.browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("Petrov@gmail.com")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")

        print(welcome_text_elt)
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        print(welcome_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, " текст не совпал")


if __name__ == "__main__":
    unittest.main()


# Запустить тест через терминал (предварительно перейти в нужную папку) python -m unittest .\st3_2step_13.py

"""     Тест 2 падает согласно требованиям задания 1.6 Поиск элементов с помощью Selenium WebDriver шаг 11
Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. 
Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли 
обнаружить баг, который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, 
здесь ошибка в приложении которое вы тестируете, а не в вашем тесте. """
