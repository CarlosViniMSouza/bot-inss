from botcity.web import By

def clickCitations(bot):
    model = "CITAÇÃO ONLINE INSS"
    # model = "CITAÇÃO"

    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    while len(bot.find_elements('//*[@id="quadroPendencias"]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/a', by=By.XPATH)) < 1:
        print("loading ...")
        
    # bot.find_element('/html/body/div[1]/div[2]/form/fieldset/table[2]/tbody/tr/td[5]/fieldset[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/a', by=By.XPATH).click()
    bot.find_element('//*[@id="quadroPendencias"]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/a', by=By.XPATH).click()

    while len(bot.find_elements('//*[@id="expedirCitacaoForm"]/table[2]/tbody/tr/td[10]/a', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('//*[@id="expedirCitacaoForm"]/table[2]/tbody/tr/td[10]/a', by=By.XPATH).click()

    while len(bot.find_elements('//*[@id="descricaoModeloDocumento"]', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('//*[@id="descricaoModeloDocumento"]', by=By.XPATH).send_keys(model)
    # bot.enter()

    bot.wait(2000)

    while len(bot.find_elements('//*[@id="5765201"]', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('//*[@id="5765201"]', by=By.XPATH).click()

    while len(bot.find_elements('//*[@id="digitarButton"]', by=By.XPATH)) < 1:
        print("loading ...")
        
    bot.find_element('//*[@id="digitarButton"]', by=By.XPATH).click()

    bot.leave_iframe() # exit iframe
    bot.leave_iframe() # exit frame