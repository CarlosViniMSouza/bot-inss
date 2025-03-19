from botcity.web import By
from botcity.web.util import element_as_select

def handleForms(bot):
    # Search the frame inside of frameset
    frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
    bot.enter_iframe(frame)

    iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
    bot.enter_iframe(iframe)

    while len(bot.find_elements('codVara', by=By.ID)) < 1:
        print("loading ...")

    # Searching for element 'first_select'
    first_select = bot.find_element(selector='codVara', by=By.ID)

    # Converting the element to a select element.
    first_select = element_as_select(first_select)

    # Select the option by index.
    first_select.select_by_index(index=1)

    while len(bot.find_elements('idLocalizador', by=By.ID)) < 1:
        print("loading ...")

    # Searching for element 'second_select'
    second_select = bot.find_element(selector='idLocalizador', by=By.ID)

    # Converting the element to a select element.
    second_select = element_as_select(second_select)

    # Select the option by index.
    # ROBÔ - Aguardando Trânsito em Julgado
    second_select.select_by_visible_text(text="ROBÔ - Aguardando Trânsito em Julgado")

    # second_select.select_by_index(index=22)
    # index 22 -> "Robo - Aguardando Transito em Julgado"
    # index 23 -> "Robo - Citacao Online"

    while len(bot.find_elements('//*[@id="pesquisar"]', by=By.XPATH)) < 1:
        print("loading ...")

    # click button 'Pesquisar'
    bot.find_element('//*[@id="pesquisar"]', By.XPATH).click()

    bot.leave_iframe()
    bot.leave_iframe()