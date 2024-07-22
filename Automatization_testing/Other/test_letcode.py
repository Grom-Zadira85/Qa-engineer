
# шаги :
#On completion of this exercise, you can learn the following concepts.
#sendKeys()  добавить в поле имя
#Keyboard TAB добавить ТАБ
#getAttribute()
#clear() очистить поле
#isEnabled() Проверить, что поле отключено, disable
#Confirm text is readonly проверить что поле не редактируется


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

link = "https://letcode.in/edit"


def test_input_form():
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, "fullName").send_keys('Grom')

    """ Пробуем  метод .text , т.к наше поле на сайте пустое, .текст вернет пустую строку"""

    print("\n есть вопрос ", browser.find_element(By.ID, "fullName").text)
    print("\n есть вопрос ", browser.find_element(By.ID, "join").text)

    browser.find_element(By.ID, "join").send_keys('_Qa ' + Keys.TAB) # \t это тоже TAB
    assert browser.find_element(By.ID, "getMe").get_attribute("value") == "ortonikc", "поле пустое"

    browser.find_element(By.ID, "clearMe").clear()
    assert browser.find_element(By.ID, "clearMe").get_attribute("value") == "", "поле не пустое"
    assert browser.find_element(By.ID, "noEdit").get_attribute("disabled") == "true", "Поле не доступно для запаси"
    assert browser.find_element(By.ID, "dontwrite").is_enabled(), "поле редактируется"

    """Разблокировать поле и ввести слово """
    # browser.find_element(By.XPATH, "//*[text()= 'Confirm edit field is disabled']")
    # var = browser.find_element(By.ID, "noEdit").get_attribute("value") == "disabled"
    var = browser.find_element(By.ID, "noEdit")
    browser.execute_script("arguments[0].removeAttribute('disabled')", var)
    browser.find_element(By.ID, "noEdit").send_keys("Field is working")
    assert browser.find_element(By.ID, "noEdit").get_attribute("value") == "Field is working", "поле  не активно"
    browser.quit()

