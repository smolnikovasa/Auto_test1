from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input4 = browser.find_element_by_css_selector('div.second_block input.form-control.first')
    input4.send_keys("89234445533")
    input5 = browser.find_element_by_css_selector('div.second_block input.form-control.second')
    input5.send_keys("г. Томск")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")

    assert not button.is_enabled()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
