from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

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