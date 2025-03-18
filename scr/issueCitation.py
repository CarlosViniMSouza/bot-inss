def issueCitation(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    password = "admin123"
    bot.find_element('//*[@id="senhaCertificado"]', by=By.XPATH).send_keys(password)

    bot.find_element('//*[@id="assinarButton"]', by=By.XPATH).click()
    bot.wait(2000)

    bot.leave_iframe() # exit iframe
    bot.leave_iframe() # exit frame