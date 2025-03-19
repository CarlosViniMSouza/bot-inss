from botcity.web import By

def selectFirstProcess(bot):
   # Search the frame inside of frameset
   frame = bot.find_element(selector='mainFrame', by=By.ID)
   bot.enter_iframe(frame)
   
   while len(bot.find_elements('//*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a', By.XPATH).click() # test case

   bot.leave_iframe()