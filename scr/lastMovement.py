from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

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