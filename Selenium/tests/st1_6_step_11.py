"""Задание: уникальность селекторов
У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте.
Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной. Обновленная
страница доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли баг в форму регистрации.

Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. Если ваш тест упал с
ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг,
который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в
приложении которое вы тестируете, а не в вашем тесте.
Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг.
В этом случае попробуйте поменять селекторы, сделав их уникальными.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # ссылка к варианту_1  (до внесения бага разработчиками в форму регистрации )
    # link = "http://suninjuly.github.io/registration1.html"

    # ссылка к варианту_2 (после обновления формы регистрации - отсутствует поле last name )
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("Petrov@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    print("=========================================")
    print(welcome_text_elt)
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
