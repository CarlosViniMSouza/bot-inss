from botcity.web import By
# from copyProcessID import copyProcessID

def searchProcessByID(bot, listID):
   # Search the frame inside of frameset
   frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
   bot.enter_iframe(frame)

   iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
   bot.enter_iframe(iframe)

   while len(bot.find_elements('//*[@id="processoBusca"]', by=By.XPATH)) < 1:
      print("loading ...")

   bot.find_element('//*[@id="processoBusca"]', By.XPATH).click()

   while len(bot.find_elements('//*[@id="numeroProcesso"]', by=By.XPATH)) < 1:
      print("loading ...")

   bot.find_element('//*[@id="numeroProcesso"]', By.XPATH).send_keys(listID[0])

   while len(bot.find_elements('//*[@id="pesquisar"]', by=By.XPATH)) < 1:
      print("loading ...")

   bot.find_element('//*[@id="pesquisar"]', By.XPATH).click()

   bot.leave_iframe()
   bot.leave_iframe()
