from botcity.web import By

def selectProcess(bot):
   # Search the frame inside of frameset
   frame = bot.find_element(selector='mainFrame', by=By.ID)
   bot.enter_iframe(frame)

   # //*[@id="listaAreaAtuacaovara"]/div/ul (list all content)
   # //*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a (select first item)
   # //*[@id="listaAreaAtuacaovara"]/div/ul/li[2]/a (select second item)
   # //*[@id="listaAreaAtuacaovara"]/div/ul/li[3]/a (select trird item)
   
   while len(bot.find_elements('//*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="listaAreaAtuacaovara"]/div/ul/li[1]/a', By.XPATH).click() # test case
   bot.leave_iframe()