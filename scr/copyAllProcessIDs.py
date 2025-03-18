from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

def copyAllProcessIDs(bot): # special function #
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    bot.wait(5000)
    
    # Caught all items inside <em> tags inside of <td> inside of <tr>
    elements = bot.find_elements("em")

    # Insert all IDs in a list
    ids = [element.text for element in elements]

    # Show the all IDs
    print(ids)

    bot.leave_iframe()
    bot.leave_iframe()