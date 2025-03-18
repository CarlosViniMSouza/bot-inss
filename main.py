from botcity.web import WebBot, Browser, By
from botcity.web.util import element_as_select

# Webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Import functions
from scr.botLogin import botLogin
from scr.selectProcess import selectProcess
from scr.searchAdvancedButton import searchAdvancedButton
from scr.handleForms import handleForms
from scr.copyProcessID import copyProcessID
from scr.lastMovement import lastMovement
from scr.moveProcess import moveProcess
from scr.clickCitations import clickCitations
from scr.typeDocument import typeDocument
from scr.issueCitation import issueCitation

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
    #copyAllProcessIDs(bot=bot_web)
    copyProcessID(bot=bot_web)
    lastMovement(bot=bot_web)
    moveProcess(bot=bot_web)
    clickCitations(bot=bot_web)
    typeDocument(bot=bot_web)
    issueCitation(bot=bot_web)

    bot_web.wait(2000)
    bot_web.stop_browser() # Finished process

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
