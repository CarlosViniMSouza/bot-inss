from botcity.web import By

def copyNameWorkspace(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    # /html/body/div[1]/table/tbody/tr/td[1]/div[3]/a[2]/img
    while len(bot.find_elements('//*[@id="alterarAreaAtuacao"]/img', by=By.XPATH)) < 1:
        print("loading ...")

    bot.find_element('//*[@id="alterarAreaAtuacao"]/img', by=By.XPATH).click()

    iframe2 = bot.find_element('/html/body/div[2]/table[2]/tbody/tr/td[2]/iframe', by=By.XPATH)  # iframe from new forms
    bot.enter_iframe(iframe2)  # //iframe[contains(@name,"window")]

    while len(bot.find_elements('//*[@id="listaAreaAtuacaovara"]', by=By.XPATH)) < 1:
        print("loading ...") # find the 'Varas Civeis' for issue citations.

    bot.find_element('//*[@id="listaAreaAtuacaovara"]')

    # Caught all items listed
    workspaces = bot.find_elements("li")

    # Insert all IDs in a list
    ids = [element.text for element in workspaces]
    unique_workspaces = list(dict.fromkeys(ids))

    print(unique_workspaces)

    bot.leave_iframe() # leave iframe2
    bot.leave_iframe() # leave iframe
    bot.leave_iframe() # leave frame
