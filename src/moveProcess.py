from botcity.web import By

def moveProcess(bot):
   number_days = 30
   
   # Search the frame inside of frameset
   frame = bot.find_element('//*[@id="mainFrame"]', by=By.XPATH)
   bot.enter_iframe(frame)

   iframe = bot.find_element('/html/body/div[2]/iframe', by=By.XPATH)
   bot.enter_iframe(iframe)
   
   while len(bot.find_elements('//*[@id="movimentarProcessoForm"]/fieldset/table[2]/tbody/tr/td[1]/a[3]', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="movimentarProcessoForm"]/fieldset/table[2]/tbody/tr/td[1]/a[3]', By.XPATH).click() # citar partes
   
   iframe2 = bot.find_element('/html/body/div[2]/table[2]/tbody/tr/td[2]/iframe', by=By.XPATH) # iframe from new forms
   bot.enter_iframe(iframe2) # //iframe[contains(@name,"window")]
   
   while len(bot.find_elements('//*[@id="citacaoForm"]/fieldset/table[1]/tbody/tr[8]/td/h4/input', by=By.XPATH)) < 1:
      print("loading ...")
   
   checkbox = bot.find_element(selector='//*[@id="citacaoForm"]/fieldset/table[1]/tbody/tr[8]/td/h4/input', by=By.XPATH)
   checkbox.click()
   
   while len(bot.find_elements('//*[@id="prazoPartesPassivas"]', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="prazoPartesPassivas"]', By.XPATH).send_keys(number_days)
   
   while len(bot.find_elements('//*[@id="citarButton"]', by=By.XPATH)) < 1:
      print("loading ...")
   
   bot.find_element('//*[@id="citarButton"]', By.XPATH).click()
   
   bot.leave_iframe() # exit iframe2
   bot.leave_iframe() # exit iframe
   bot.leave_iframe() # exit iframe