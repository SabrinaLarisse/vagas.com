from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3
conn = sqlite3.connect("C:\\Users\\bruno\\Desktop\\vagas.com\\vagas.db")

conn.execute('''CREATE TABLE IF NOT EXISTS vagas
             (link Hyperlink UNIQUE)''')

def candidatura(end):
    try:
        endereço = "https://www.vagas.com.br" + end
        
        
        conn.execute("INSERT INTO vagas VALUES ('%s')" % endereço)
        conn.commit()
        #Para pesquisar no banco de dados:
        #SELECT * FROM nome_da_tabela
        #ou SELECT COLUNA1,COLUNA2, COLUNA3 FROM nome_da_tabela
        #vetor = [1,2,3,4]
        
        driver.get(endereço)
        bsObj  = BeautifulSoup(driver.page_source, "html.parser")
        #for i in bsObj.find_all("li"):
        #if ("Excel" in i.text):
        #    print("excel")
        e = driver.find_element_by_id("bt-candidatura")
        e.submit()
        time.sleep(5)
        try:
            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(5)
            try:
                g = driver.find_element_by_name("VeT1")
                g.click()
            except:
                _=""
            f = driver.find_element_by_name("botInfConfirma")
            f.click()
            time.sleep(5)
            
        except:
            try:
                g = driver.find_element_by_name("VeT1")
                g.click()
            except:
                _=""
            f = driver.find_element_by_name("botInfConfirma")
            f.click()
            time.sleep(5)
 
    except:
        _ = ""
        
#for texto in ['Estagio em economia em São Paulo' , "Estagio em finanças em São Paulo", "Estagio em business intelligence em São Paulo", "Estagio em macroeconomia em São Paulo", "Estagio em microeconomia em São Paulo", "Estagio em analise economica em São Paulo", "Estagio em analytics em São Paulo", "pesquisa economia em São Paulo", "estágio em backoffice em São Paulo", "estágio em middle office em São Paulo", "estágio em front office em São Paulo"]:
driver = webdriver.Chrome("C:\\Users\\bruno\\Desktop\\chromedriver.exe")
driver.get("https://www.vagas.com.br/")
a = driver.find_element_by_id("btLogin")
a.click()
b = driver.find_element_by_id("login_candidatos_form_usuario")
c = driver.find_element_by_id("login_candidatos_form_senha")
b.click()
b.send_keys("coloque aqui o login")
c.click()
c.send_keys("coloque aqui a senha")
c.submit()
    #logou
for texto in ['Estagio em economia em São Paulo' , "Estagio em finanças em São Paulo", "Estagio em business intelligence em São Paulo", "Estagio em macroeconomia em São Paulo", "Estagio em microeconomia em São Paulo", "Estagio em analise economica em São Paulo", "Estagio em analytics em São Paulo", "estágio em pesquisa economia em São Paulo", "estágio em backoffice em São Paulo", "estágio em middle office em São Paulo", "estágio em front office em São Paulo", "estágio em mercado financeiro em São Paulo"]:
    driver.get("https://www.vagas.com.br/")
    c = driver.find_element_by_class_name("campoPesquisaVaga")
    c.click()
    #c.send_keys("Estagio em Economia em São Paulo")
    c.send_keys(texto)
    c.submit()


    try:
        while True:
            d = driver.find_element_by_class_name("btMaisVagas")
            d.click()
    except:
        code = driver.page_source

        bsObj  = BeautifulSoup(code, "html.parser")
        for i in bsObj.find_all("h2"):
            try:
                candidatura(i.a.get('href'))
            except:
                next


driver.close()


conn.close()
    
