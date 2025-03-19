from botcity.web import WebBot, Browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.botLogin import botLogin
from src.selectProcess import selectProcess
from src.searchAdvancedButton import searchAdvancedButton
from src.handleForms import handleForms
# from src.copyProcessID import copyProcessID
# from src.lastMovement import lastMovement
 #from src.moveProcess import moveProcess
# from src.clickCitations import clickCitations
# from src.typeDocument import typeDocument
# from src.issueCitations import issueCitation
# from src.searchProcessByID import searchProcessByID
from src.changeWorkspace import changeWorkspace

# --- Principal Function --- #
def main():
    bot_web = WebBot()
    bot_web.headless = False

    bot_web.browser = Browser.EDGE
    bot_web.driver_path = EdgeChromiumDriverManager().install()

    bot_web.browse("http://10.47.76.126:8082/projudi/")
    bot_web.maximize_window()

    botLogin(bot=bot_web)
    selectProcess(bot=bot_web)
    searchAdvancedButton(bot=bot_web)
    handleForms(bot=bot_web)
    changeWorkspace(bot=bot_web)

    """
    listIDs = copyProcessID(bot=bot_web)
    
    while len(listIDs) > 0:
        searchProcessByID(bot=bot_web, listID=listIDs)
        lastMovement(bot=bot_web)
        moveProcess(bot=bot_web)
        clickCitations(bot=bot_web)
        typeDocument(bot=bot_web)
        issueCitation(bot=bot_web)

        listIDs.pop(0)
    """

    print("Automação Encerrada!")

    bot_web.wait(2000)
    bot_web.stop_browser() # Finished process

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
