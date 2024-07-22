"""---------------       2.4 Настройка ожиданий      ---------------

                                 Шаги:
1)Открыть страницу http://suninjuly.github.io/wait1.html
2)Нажать на кнопку "Verify"
3)Проверить, что появилась надпись "Verification was successful!"
4)Для открытия страницы мы используем метод get, затем находим нужную кнопку с помощью одного из методов
find_element_by_ и нажимаем на нее с помощью метода click. Далее находим новый элемент с текстом и проверяем
соответствие текста на странице ожидаемому тексту."""

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")
assert "successful" in message.text
