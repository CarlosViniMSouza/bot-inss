from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

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