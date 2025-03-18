from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

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