from botcity.web import By

def searchAdvancedButton(bot):
   # Search the frame inside of frameset
   frame = bot.find_element(selector='mainFrame', by=By.ID)
   bot.enter_iframe(frame)

   while len(bot.find_elements('//*[@id="Stm0p0i1eTX"]', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="Stm0p0i1eTX"]', By.XPATH).click()
   
   while len(bot.find_elements('//*[@id="Stm0p1i8TRR"]', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="Stm0p1i8TRR"]', By.XPATH).click()
   
   while len(bot.find_elements('//*[@id="Stm0p3i1TRR"]', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="Stm0p3i1TRR"]', By.XPATH).click()
   
   bot.leave_iframe()