from botcity.web import By

def copyNameWorkspace(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    while len(bot.find_elements('//*[@id="listaAreaAtuacaovara"]', by=By.XPATH)) < 1:
        print("loading ...") # find the 'Varas Civeis' for issue citations.

    bot.find_element('//*[@id="listaAreaAtuacaovara"]')

    # Caught all items listed
    workspaces = bot.find_elements("li")

    # Insert all IDs in a list
    ids = [element.text for element in workspaces]
    unique_workspaces = list(dict.fromkeys(ids))

    bot.leave_iframe() # leave frame

    return unique_workspaces
