
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "https://victoretc.github.io/selenium_waits/"


def test_registration():
    browser = webdriver.Chrome()
    waitt = WebDriverWait(browser, timeout=15)
    browser.implicitly_wait(10)
    browser.get(link)
    words = browser.find_element(By.XPATH, "/html/body/h1").text
    # print(words)
    assert words == "Практика с ожиданиями в Selenium", "заголовок не соответствует требованию"
    browser.find_element(By.ID, "startTest").click()
    browser.find_element(By.ID, "login").send_keys('Grom')
    browser.find_element(By.ID, "password").send_keys('Zadira')
    browser.find_element(By.ID, "agree").click()
    browser.find_element(By.ID, "register").click()
    """ проверка  появления  элемента - "Загрузка" """
    loader = waitt.until(EC.visibility_of_element_located((By.ID, "loader")))
    assert loader.is_displayed(), "элемент загрузки не визуализируется"
    success = waitt.until(EC.visibility_of_element_located((By.ID, "successMessage"))).text
    print(success)
    assert success == "Вы успешно зарегистрированы!", " регистрация не успешна "
    browser.quit()


def test_tools():
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/dynamic-properties")
    browser.implicitly_wait(10)
    button = browser.find_element(By.ID, "enableAfter")
    assert button.is_enabled(), " кнопка не активна"
    visible_button3 = browser.find_element(By.ID, "visibleAfter")
    assert visible_button3.is_displayed(), "элемент не визуализируется"
    browser.quit()


""" -------------------------Проверка создания нового элемента  -------------------------------"""


def test_hero():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1)
    '--------------------------создали элемент------------------------------------------------------'
    browser.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()
    new_element = browser.find_element(By.CSS_SELECTOR, '[ onclick = "deleteElement()"]')
    assert new_element.is_displayed(), "Новый элемент не создан"
    time.sleep(1)
    '-----------------------------удалим элемент----------------------------------------------------------------'
    browser.find_element(By.CSS_SELECTOR, '[ onclick = "deleteElement()"]').click()
    del_new_element = browser.find_elements(By.CSS_SELECTOR, '[ onclick = "deleteElement()"]')
    assert len(del_new_element) == 0, "элемент не удален"
    time.sleep(1)
    browser.quit()


"""--------------------------- Поиск сломанных изображений--------------------------------------------------"""
from selenium import webdriver
import requests


def test_img():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/broken_images")
    # ------------------------Поиск всех элементов <img>------------------------------------------
    images = browser.find_elements(By.TAG_NAME, "img")
    broken_images = []

    # ---------------------------Проверка каждой ссылки на изображение-------------------------------------------
    for image in images:
        src = image.get_attribute("src")
        print(src)
        print(image.get_attribute(("naturalWidth")))
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print("\n", broken_images)

    assert len(broken_images) == 0, "Нет сломанных изображений"
    browser.quit()


# """ assert 2 == 0 тест падает, найдено 2 битые картинки"""


" ----------------------------проверка галочки в чек боксе (нажался или нет) ниже ---------------------"


def test_checked():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    check2 = browser.find_element(By.CSS_SELECTOR,
                                  '#checkboxes > input[type=checkbox]:nth-child(3)')  # чека бокс 2 нажат
    box2 = check2.get_attribute("checked")
    print(box2)
    assert box2 == 'true', " чек бокс не нажат"
    time.sleep(3)
    browser.quit()


"--------------------------------------сравнение размеров элементов ниже------------------------------------------ "


def test_position():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    element = browser.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)')
    element.size
    print("элемент", element.size)
    print("элемент", element.rect)
    print("элемент", element.location)
    print("элемент", element.aria_role)
    element2 = browser.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')
    element2.size
    print("элемент2", element2.size)
    print("элемент2", element2.rect)
    print("элемент2", element2.location)
    print("элемент2", element2.aria_role)


"-------------------Элементы меняются местами --------------------"


def test_drag_and_drop():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/drag_and_drop")
    a = browser.find_element(By.ID, 'column-a')
    b = browser.find_element(By.ID, 'column-b')
    a_before = a.location['y']
    b_before = b.location['y']
    ActionChains(browser).drag_and_drop(a, b).perform()
    a_after = a.location['y']
    b_after = b.location['y']
    assert a_before == b_after, 'Элементы не перемещены'
