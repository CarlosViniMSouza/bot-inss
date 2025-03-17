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

    # cnpj = "000.0000.000-00"
    # bot.find_element(selector='//*[@id="cpfCnpj"]', by=By.XPATH).send_keys(cnpj)

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
    second_select.select_by_index(index=22)
    
    bot.wait(1000)

    # click button 'Pesquisar'
    bot.find_element('//*[@id="pesquisar"]', By.XPATH).click()

    bot.leave_iframe()
    bot.leave_iframe()

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
    bot.maximize_window()

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
