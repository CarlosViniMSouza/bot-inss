from botcity.web import By

def lastMovement(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    bot.scroll_down(clicks=4)

    while len(bot.find_elements('/html/body/div[1]/div[2]/form/fieldset/table[3]/tbody/tr[2]/td/div/div/div/table/tbody/tr[1]/td[4]/b/a', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('/html/body/div[1]/div[2]/form/fieldset/table[3]/tbody/tr[2]/td/div/div/div/table/tbody/tr[1]/td[4]/b/a', By.XPATH).click()
    bot.wait(2000)

    while len(bot.find_elements('//*[@id="movimentarButton"]', by=By.XPATH)) < 1:
       print("loading ...")

    bot.find_element('//*[@id="movimentarButton"]', By.XPATH).click()

    bot.leave_iframe()
    bot.leave_iframe()