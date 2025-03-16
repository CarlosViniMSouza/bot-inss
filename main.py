from botcity.web import WebBot, Browser, By
# from botcity.web.util import element_as_select

from webdriver_manager.microsoft import EdgeChromiumDriverManager

def botLogin(bot):
    username = "botCitacaoINSS"
    pwd = "admin123"

    bot.wait(1000)

    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)
    
    # element = bot.find_element(selector='element_selector', by=By.ID)
    # element.click()
        
    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(username)
    bot.wait(1000)

    bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(pwd)
    bot.wait(1000)

    bot.find_element('//*[@id="btEntrar"]', By.XPATH).click()
    bot.wait(1000)

    bot.leave_iframe() # leave to frame
    bot.wait(1000)

def selectProcess(bot):
    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)

    # //*[@id="listaAreaAtuacaovara"]/div/ul (list all content)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a (select first item)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[2]/a (select second item)
    # //*[@id="listaAreaAtuacaovara"]/div/ul/li[3]/a (select trird item)

    bot.find_element('//*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a', By.XPATH).click() # test case
    bot.leave_iframe()
    
    bot.wait(1000)

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
    bot.wait(1000)

def handleForms(bot):
    # Search the frame inside of frameset
    iframe = bot.find_element('mainFrame', by=By.CLASS_NAME)
    bot.enter_iframe(iframe)

    frame = bot.find_element('userMainFrame', by=By.CLASS_NAME)
    bot.enter_iframe(frame)

    # Searching for element 'first_select '
    if not bot.find("first_select", matching=0.97, waiting_time=10000):
        not_found("first_select")
    bot.click_relative(453, 15)
    
    bot.wait(1000)
    
    # Searching for element 'choose_unit '
    if not bot.find("choose_unit", matching=0.97, waiting_time=10000):
        not_found("choose_unit")
    bot.click_relative(241, 41)
    
    bot.wait(1000)

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
