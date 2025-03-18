from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

def copyProcessID(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    # Capture ID process
    processID = bot.find_element("em").text

    bot.find_element('//*[@id="processoBusca"]', By.XPATH).click()
    bot.wait(2000)

    bot.find_element('//*[@id="numeroProcesso"]', By.XPATH).send_keys(processID)
    bot.wait(2000)

    bot.find_element('//*[@id="pesquisar"]', By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe()
    bot.leave_iframe()