from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение для еремнной x
    x_element = browser.find_element_by_css_selector("img#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(str(y))
    check1 = browser.find_element_by_css_selector('input#robotCheckbox')
    check1.click()
    check2 = browser.find_element_by_css_selector('input#robotsRule')
    check2.click()

    # Нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
