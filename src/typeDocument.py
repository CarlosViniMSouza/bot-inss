from botcity.web import By

def typeDocument(bot):
   # Search the frame inside of frameset
   frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
   bot.enter_iframe(frame)

   iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
   bot.enter_iframe(iframe)
   
   while len(bot.find_elements('/html/body/div[1]/div[2]/form/table[3]/tbody/tr/td[2]/input[2]', by=By.XPATH)) < 1:
     print("loading ...")
   
   bot.find_element('/html/body/div[1]/div[2]/form/table[3]/tbody/tr/td[2]/input[2]', by=By.XPATH).click()

   bot.wait(1000) # time to load page PDF
   
   while len(bot.find_elements('/html/body/div[1]/div[2]/form/table[2]/tbody/tr/td/input[1]', by=By.XPATH)) < 1:
     print("loading ...")
   
   bot.find_element('/html/body/div[1]/div[2]/form/table[2]/tbody/tr/td/input[1]', by=By.XPATH).click()
   
   while len(bot.find_elements('/html/body/div[1]/div[2]/table/tbody/tr[2]/td/div[1]/form/table[5]/tbody/tr/td[2]/input[2]', by=By.XPATH)) < 1:
     print("loading ...")
   
   bot.find_element('/html/body/div[1]/div[2]/table/tbody/tr[2]/td/div[1]/form/table[5]/tbody/tr/td[2]/input[2]', by=By.XPATH).click()
   
   bot.leave_iframe() # exit iframe
   bot.leave_iframe() # exit frame