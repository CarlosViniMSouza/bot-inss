from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

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
