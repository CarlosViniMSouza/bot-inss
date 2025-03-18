from botcity.web import By

def botLogin(bot):
    # Search the frame inside of frameset
    frame = bot.find_element(selector='mainFrame', by=By.ID)
    bot.enter_iframe(frame)
    
    username = "botCitacaoINSS"
    pwd = "admin123"
    
    while len(bot.find_elements('//*[@id="login"]', by=By.XPATH)) < 1:
        print("loading ...")
    
    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(username)

    while len(bot.find_elements('//*[@id="senha"]', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(pwd)

    while len(bot.find_elements('//*[@id="btEntrar"]', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('//*[@id="btEntrar"]', By.XPATH).click()

    bot.leave_iframe() # leave to frame