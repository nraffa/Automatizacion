from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver = r"C:\Users\Nico\Documents\PYTHON\Automatizacion/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http:sga.itba.edu.ar")
elem_user = driver.find_element_by_name("user")
elem_user.clear()
elem_user.send_keys("nraffa")
elem_pass = driver.find_element_by_name("password")
elem_pass.clear()
elem_pass.send_keys("bananaslocas123")
elem_pass.send_keys(Keys.RETURN)

legajo = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/div/div/ul/li[4]")
legajo.click()

mi_legajo = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div/ul/li[4]/ul/li/a")
mi_legajo.click()

datos = driver.find_element_by_xpath("//*[@id='content']/div[3]/div/div[1]/ul/li[4]/a/span")
datos.click()

#historia = driver.find_element_by_xpath("//*[@id='id49']/div/div/div[1]/ul/li[4]/a/span")
#historia = driver.find_element_by_link_text("Historia académica")
#historia.click()
analitico = driver.find_element_by_link_text("Analítico de notas")
analitico.click()


try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id159"))
    )
finally:
    driver.quit()


#table = driver.find_element_by_id("id207")
print(table.text)


driver.close()

#print(materia_sga2.text)


#materia = input("Introducir materia: ")
#materia_sga = driver.find_element_by_tag_name("10.09 - Formación para Emprendedores").text

#print(materia_sga)
#driver.find_element_by_xpath("").click()
#"Formación para Emprendedores"
#////// script para mandar mail////


