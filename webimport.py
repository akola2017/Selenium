from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.microsoft.com/pl-pl")
driver.find_element_by_id('l1_support').click()
driver.find_element_by_xpath("//img[@id='i-need-help-with-Office-img']").click()
driver.quit()
