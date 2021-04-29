from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение для еремнной x
    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text
    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text

    y = int(x1)+int(x2)
    print(y)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(y))

    # Нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
