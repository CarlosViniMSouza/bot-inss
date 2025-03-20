from botcity.web import By

def copyProcessID(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)
    
    # Caught all items inside <em> tags inside of <td> inside of <tr>
    elements = bot.find_elements("em")

    # Insert all IDs in a list
    ids = [element.text for element in elements]
    
    while True:
        next_page = bot.find_element(selector='arrowNextOn', by=By.CLASS_NAME)

        if not next_page:
            break
        else:
            next_page.click()

            bot.wait(3000)

            new_elements = bot.find_elements("em")
            new_ids = [new_element.text for new_element in new_elements]

            # Insert all IDs in a list
            ids.extend(new_ids)
    
    bot.leave_iframe()
    bot.leave_iframe()
    
    return ids