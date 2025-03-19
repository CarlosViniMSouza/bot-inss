from botcity.web import By

def copyProcessID(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    # processID = bot.find_element("em").text

    # Caught all items inside <em> tags inside of <td> inside of <tr>
    elements = bot.find_elements("em")

    # Insert all IDs in a list
    ids = [element.text for element in elements]

    bot.leave_iframe()
    bot.leave_iframe()

    return ids