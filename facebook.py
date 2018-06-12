from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.find_element_by_id('u_0_n').send_keys('Agnieszka')
driver.find_element_by_id('u_0_p').send_keys('Kowalska')
driver.find_element_by_id('u_0_s').send_keys('aaa@wp.pl')
driver.find_element_by_id('u_0_z').send_keys('Alamakota!2018')
driver.find_element_by_id('u_0_v').send_keys('aaa@wp.pl')

dzien = Select (
                driver.find_element_by_name('birthday_day')
    )
dzien.select_by_value('12')
miesiac = Select (
            driver.find_element_by_name('birthday_month')
    )
miesiac.select_by_value('10')
rok = Select (
            driver.find_element_by_name('birthday_year')
    )
rok.select_by_value('1979')
driver.find_element_by_id('u_0_b').click()
driver.find_element_by_id('u_0_15').submit()
