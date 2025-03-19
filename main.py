from botcity.web import WebBot, Browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.botLogin import botLogin
from src.copyNameWorkspace import copyNameWorkspace

from src.selectFirstProcess import selectFirstProcess
from src.searchAdvancedButton import searchAdvancedButton
from src.handleForms import handleForms

from src.copyProcessID import copyProcessID

from src.searchProcessByID import searchProcessByID
from src.lastMovement import lastMovement
from src.moveProcess import moveProcess
from src.clickCitations import clickCitations
from src.typeDocument import typeDocument
from src.issueCitations import issueCitation

from src.changeWorkspace import changeWorkspace

# --- Principal Function --- #
def main():
    bot_web = WebBot()
    bot_web.headless = False

    bot_web.browser = Browser.EDGE
    bot_web.driver_path = EdgeChromiumDriverManager().install()

    bot_web.browse("http://10.47.76.126:8082/projudi/")
    bot_web.maximize_window()

    try:
        botLogin(bot=bot_web)

        listWorkspaces = copyNameWorkspace(bot=bot_web)
        listWorkspaces.pop(0)  # remove the first option already chosen

        selectFirstProcess(bot=bot_web)  # select only first 'Vara Civel'
        searchAdvancedButton(bot=bot_web)
        handleForms(bot=bot_web)

        listIDs = copyProcessID(bot=bot_web)

    except Exception as ex:
        print(ex)
        changeWorkspace(bot=bot_web, listWorkspace=listWorkspaces)
        listWorkspaces.pop(0)

    while len(listWorkspaces) > 0:
        while len(listIDs) > 0:
            searchProcessByID(bot=bot_web, listID=listIDs)
            listIDs.pop(0)

            lastMovement(bot=bot_web)
            moveProcess(bot=bot_web)
            clickCitations(bot=bot_web)
            typeDocument(bot=bot_web)
            issueCitation(bot=bot_web)

        changeWorkspace(bot=bot_web, listWorkspace=listWorkspaces)
        listWorkspaces.pop(0)

    print("Automação Encerrada!")

    bot_web.wait(2000)
    bot_web.stop_browser() # Finished process

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
