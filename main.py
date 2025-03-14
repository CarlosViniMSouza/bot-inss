from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

from webdriver_manager.microsoft import EdgeChromiumDriverManager

def botLogin(bot):
    username = "botCitacaoINSS"
    pwd = "admin123"

    bot.wait(2000)

    # open the frameset
    # frameset = bot.find_element(selector='frameSetTeste', by=By.ID)

    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)
    
    # element = bot.find_element(selector='element_selector', by=By.ID)
    # element.click()
        
    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(username)
    bot.wait(2000)

    bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(pwd)
    bot.wait(2000)

    bot.find_element('//*[@id="btEntrar"]', By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe()

def selectProcess(bot):
    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)

    # //*[@id="listaAreaAtuacaovara"]/div/ul (list all content)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a (select first item)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[2]/a (select second item)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[3]/a (select trird item)

    bot.find_element('//*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a', By.XPATH).click() # test case
    bot.wait(2000)

    bot.leave_iframe()

def searchAdvancedButton(bot):
    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)

    bot.find_element('//*[@id="Stm0p0i1eTX"]', By.XPATH).click()
    bot.wait(2000)

    bot.find_element('//*[@id="Stm0p1i8TRR"]', By.XPATH).click()
    bot.wait(2000)

    bot.find_element('//*[@id="Stm0p3i1TRR"]', By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe()

def handleForms(bot):
    # Search the frame inside of frameset
    iframe = bot.find_element('frameSetTeste', by=By.CLASS_NAME)
    bot.enter_iframe(iframe)

    frame = bot.find_element('mainFrame', by=By.CLASS_NAME)
    bot.enter_iframe(frame)

    # Obtem o elemento.
    # bot.find_element('codVara', by=By.ID).click()
    elemento_select = bot.find_element(selector='codVara', by=By.CLASS_NAME)

    # Converte o elemento em um elemento 'selecionável'.
    elemento_select = element_as_select(elemento_select)

    # Seleciona opção por índice.
    elemento_select.select_by_index(index=1)

    # bot.find_element('codVara', by=By.ID).click()
    # bot.find_element('//*[@id="codVara"]/option[2]', By.XPATH).click()
    # bot.wait(2000)


    # label = bot.find_element('idLocalizador', by=By.ID)
    # selector = element_as_select(label)
    # selector.click()
    # selector.select_by_index(index=22)

    # while len(bot.find_elements('idLocalizador', by=By.ID)) < 1:
    #     bot.wait(2000)

    bot.find_element('idLocalizador', by=By.ID).click()
    bot.find_element('//*[@id="idLocalizador"]/optgroup/option[22]').click()
    bot.wait(2000)

    bot.find_element('//*[@id="pesquisar"]', By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe() # leave to frame
    bot.leave_iframe() # leave to iframe

# --- #
def main():
    bot = WebBot()
    
    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.EDGE

    # Uncomment to set the WebDriver path
    bot.driver_path = EdgeChromiumDriverManager().install()

    # Opens the BotCity website.
    bot.browse("http://10.47.76.126:8082/projudi/")

    botLogin(bot=bot)
    selectProcess(bot=bot)
    searchAdvancedButton(bot=bot)
    handleForms(bot=bot)

    # Wait 3 seconds before closing
    bot.wait(3000)
    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
