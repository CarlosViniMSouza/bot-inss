from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

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