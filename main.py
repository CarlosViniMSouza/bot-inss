from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

from webdriver_manager.microsoft import EdgeChromiumDriverManager

def botLogin(bot):
    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)
    
    username = "botCitacaoINSS"
    pwd = "admin123"
        
    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(username)
    bot.wait(1000)

    bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(pwd)
    bot.wait(1000)

    bot.find_element('//*[@id="btEntrar"]', By.XPATH).click()
    bot.wait(1000)

    bot.leave_iframe() # leave to frame

def selectProcess(bot):
    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)

    # //*[@id="listaAreaAtuacaovara"]/div/ul (list all content)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a (select first item)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[2]/a (select second item)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[3]/a (select trird item)

    bot.find_element('//*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a', By.XPATH).click() # test case
    bot.wait(1000)

    bot.leave_iframe()

def searchAdvancedButton(bot):
    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)

    bot.find_element('//*[@id="Stm0p0i1eTX"]', By.XPATH).click()
    bot.wait(1000)

    bot.find_element('//*[@id="Stm0p1i8TRR"]', By.XPATH).click()
    bot.wait(1000)

    bot.find_element('//*[@id="Stm0p3i1TRR"]', By.XPATH).click()
    bot.wait(1000)

    bot.leave_iframe()

def handleForms(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    # Searching for element 'first_select'
    first_select = bot.find_element(selector='codVara', by=By.ID)

    # Converting the element to a select element.
    first_select = element_as_select(first_select)

    # Select the option by index.
    first_select.select_by_index(index=1)

    bot.wait(1000)

    # Searching for element 'second_select'
    second_select = bot.find_element(selector='idLocalizador', by=By.ID)

    # Converting the element to a select element.
    second_select = element_as_select(second_select)

    # Select the option by index.
    second_select.select_by_index(index=23)
    
    bot.wait(1000)

    # click button 'Pesquisar'
    bot.find_element('//*[@id="pesquisar"]', By.XPATH).click()

    bot.leave_iframe()
    bot.leave_iframe()

def copyProcessID(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    processID = bot.find_element("em").text

    bot.find_element('//*[@id="processoBusca"]', By.XPATH).click()
    bot.wait(2000)

    bot.find_element('//*[@id="numeroProcesso"]', By.XPATH).send_keys(processID)
    bot.wait(2000)

    bot.find_element('//*[@id="pesquisar"]', By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe()
    bot.leave_iframe()

def lastMovement(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    bot.scroll_down(clicks=4)

    bot.find_element('//*[@id="LNKmov1Grau,SERVIDOR,,,,"]', By.XPATH).click()
    bot.wait(2000)

    bot.find_element('//*[@id="movimentarButton"]', By.XPATH).click()

    bot.leave_iframe()
    bot.leave_iframe()

def moveProcess(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    bot.find_element('//*[@id="movimentarProcessoForm"]/fieldset/table[2]/tbody/tr/td[1]/a[3]', By.XPATH).click() # citar partes
    bot.wait(1000)

    iframe2 = bot.find_element('/html/body/div[2]/table[2]/tbody/tr/td[2]/iframe', by=By.XPATH) # iframe from new forms
    bot.enter_iframe(iframe2) # //iframe[contains(@name,"window")]
    bot.wait(1000)

    checkbox = bot.find_element(selector='//*[@id="citacaoForm"]/fieldset/table[1]/tbody/tr[8]/td/h4/input', by=By.XPATH)
    checkbox.click()

    bot.wait(2000)

    number_days = 30
    bot.find_element('//*[@id="prazoPartesPassivas"]', By.XPATH).send_keys(number_days)
    bot.wait(2000)

    bot.find_element('//*[@id="citarButton"]', By.XPATH).click()
    bot.wait(1000)

    bot.leave_iframe() # exit iframe2
    bot.leave_iframe() # exit iframe
    bot.leave_iframe() # exit iframe

def clickCitations(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    bot.find_element('/html/body/div[1]/div[2]/form/fieldset/table[2]/tbody/tr/td[5]/fieldset[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/a', by=By.XPATH).click()
    bot.wait(2000)

    bot.find_element('//*[@id="expedirCitacaoForm"]/table[2]/tbody/tr/td[10]/a', by=By.XPATH).click()
    bot.wait(2000)

    model = "CITAÇÃO ONLINE INSS"
    bot.find_element('//*[@id="descricaoModeloDocumento"]', by=By.XPATH).send_keys(model)
    bot.wait(2000)
    bot.enter()

    bot.find_element('//*[@id="digitarButton"]', by=By.XPATH).click()

    bot.leave_iframe() # exit iframe
    bot.leave_iframe() # exit frame

def typeDocument(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    bot.find_element('//*[@id="submitButton"]', by=By.XPATH).click()
    bot.wait(2000)

    bot.find_element('//*[@id="submitButton"]', by=By.XPATH).click()
    bot.wait(2000)
    
    bot.find_element('//*[@id="finishButton"]', by=By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe() # exit iframe
    bot.leave_iframe() # exit frame

def issueCitation(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    password = "admin123"
    bot.find_element('//*[@id="senhaCertificado"]', by=By.XPATH).send_keys(password)

    bot.find_element('//*[@id="assinarButton"]', by=By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe() # exit iframe
    bot.leave_iframe() # exit frame

# --- Principal Function --- #
def main():
    bot_web = WebBot()
    bot_web.headless = False

    bot_web.browser = Browser.EDGE
    bot_web.driver_path = EdgeChromiumDriverManager().install()

    bot_web.browse("http://10.47.76.126:8082/projudi/")
    bot_web.maximize_window()

    botLogin(bot=bot_web)
    selectProcess(bot=bot_web)
    searchAdvancedButton(bot=bot_web)
    handleForms(bot=bot_web)
    copyProcessID(bot=bot_web)
    lastMovement(bot=bot_web)
    moveProcess(bot=bot_web)
    clickCitations(bot=bot_web)
    typeDocument(bot=bot_web)
    issueCitation(bot=bot_web)

    bot_web.wait(2000)
    bot_web.stop_browser() # Finished process

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
