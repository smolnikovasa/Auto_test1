from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #input1 = browser.find_elements_by_xpath('//input[@type="text"]')
    elements = browser.find_elements_by_xpath('//input[@type="text"]')
    #input1.send_keys("I")
    #input2 = browser.find_element_by_xpath('//input[@name="last_name" and @type="text"]')
    #input2.send_keys("P")
    #input3 = browser.find_element_by_xpath('//input[@name="firstname" and @class="form-control city"]')
    #input3.send_keys("S")
    #input4 = browser.find_element_by_xpath('//input[@name="firstname" and @id="country"]')
    #input4.send_keys("R")
    for i in range(len(elements)):
        browser.execute_script(f'document.getElementsByTagName("input")[{i}].value = "Мой ответ"')
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
