from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver = r"C:\Users\Nico\Documents\PYTHON\Automatizacion/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http:google.com")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("tabla de punto de ebullicion wikipedia")
elem.send_keys(Keys.RETURN)

wiki = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div/div[1]/a/h3")
wiki.click()

table = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div/table[3]")
print(table.text[0])
'''
try:
    table = WebDriverWait(driver, 6).until(
        EC.presence_of_element_located((By.CLASS, "wikitable"))
    )
finally:
    driver.quit()

'''
#table = driver.find_element_by_id("id207")
print(table.text)


driver.close()

#print(materia_sga2.text)


#materia = input("Introducir materia: ")
#materia_sga = driver.find_element_by_tag_name("10.09 - Formación para Emprendedores").text

#print(materia_sga)
#driver.find_element_by_xpath("").click()
#"Formación para Emprendedores"
