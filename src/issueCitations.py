from botcity.web import By

def issueCitation(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    while len(bot.find_elements('//*[@id="senhaCertificado"]', by=By.XPATH)) < 1:
        print("loading ...")

    password = "admin123"
    bot.find_element('//*[@id="senhaCertificado"]', by=By.XPATH).send_keys(password)

    while len(bot.find_elements('//*[@id="assinarButton"]', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('//*[@id="assinarButton"]', by=By.XPATH).click()

    bot.leave_iframe() # exit iframe
    bot.leave_iframe() # exit frame