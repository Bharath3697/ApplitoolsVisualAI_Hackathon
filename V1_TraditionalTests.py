from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
url1 = "https://demo.applitools.com/hackathon.html"
url2= "https://demo.applitools.com/hackathonV2.html"
urls=url1
login_after=["https://demo.applitools.com/hackathonApp.html","https://demo.applitools.com/hackathonAppV2.html"]
driver = webdriver.Chrome(chrome_options=options)
driver.get(urls)
class Test(unittest.TestCase):
    
    def test1(self):
     
      pas=True
      print("Test 1: Login Page UI Elements Test")
      try:
            logo0 = driver.find_element_by_xpath("//img[@src='img/logo-big.png']")
            self.assertTrue(logo0.is_displayed())
      except (AssertionError) as x:
            pas=False
            print("Failed:",x)
            
            
      try:
       element1 = driver.find_element_by_class_name("auth-header").text
       self.assertEqual(element1,"Login Form")
      except (AssertionError) as x:
            pas=False
            print("Error:",x)
      try:
       element2=driver.find_element_by_class_name("form-group").text
       self.assertEqual(element2,"Username")
      except (AssertionError) as x:
            pas=False
            print("Error:",x)

      try:
       element3=driver.find_element_by_xpath("/html/body/div/div/form/div[2]").text
       self.assertEqual(element3,"Password")
      except (AssertionError) as x:
            pas=False
            print("Error:",x)
            
      try:
           logo1 = driver.find_element_by_xpath("/html/body/div/div/form/div[1]/div")
           self.assertTrue(logo1.is_displayed())
      except (AssertionError,Exception) as x:

            pas=False
            print("Error:",x)


      try:
           logo2 = driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div")
           self.assertTrue(logo2.is_displayed())
      except (AssertionError,Exception) as x:
            pas=False
            print("Error:",x)



      try:
       element4 = driver.find_element_by_xpath('//*[@id="username"]').get_attribute("placeholder")
       self.assertEqual(element4,"Enter your username")
      except (AssertionError) as x:
            pas=False
            print("Error:",x)

      try:
       element5 = driver.find_element_by_xpath('//*[@id="password"]').get_attribute("placeholder")
       self.assertEqual(element5,"Enter your password")
      except (AssertionError) as x:
            pas=False
            print("Error:",x)


      try:
       element6=driver.find_element_by_xpath('//*[@id="log-in"]').text
       self.assertEqual(element6,"Log In")
      except (AssertionError) as x:
            pas=False
            print("Error:",x)

      try:
       element7=driver.find_element_by_class_name('form-check-label').text
       self.assertEqual(element7,"Remember Me")
      except (AssertionError) as x:
            pas=False
            print("Error:",x)

      try:
           logo3 = driver.find_element_by_xpath("//img[@src='img/social-icons/twitter.png']")
           self.assertTrue(logo3.is_displayed())
      except (AssertionError,Exception) as x:
            pas=False
            print("Error1:",x)


      try:
          
           logo4 = driver.find_element_by_xpath("//img[@src='img/social-icons/facebook.png']")
           self.assertTrue(logo4.is_displayed())
      except (AssertionError,Exception) as x:
            pas=False
            print("Error2:",x)

      try:
           logo5 = driver.find_element_by_xpath("//img[@src='img/social-icons/linkedin.png']")
           self.assertTrue(logo5.is_displayed())
      except (AssertionError,Exception) as x:
            pas=False
            print("Error3:",x)
      if pas==True:
          print("Test1 Passed")
      else:
          print("Test1 Failed with assertion")
      print("-"*20)


      
    def test2(self):
     pas=True  
     try:
      print("Test Case 2:Data-Driven Test")
      
      #Expected=["Password must be present","Both Username and Password must be present","Username must be present"]

      element = driver.find_element_by_id("username")
      element1 = driver.find_element_by_id("password")

      #case no username
      Actualmsg=""
      expectedmsg="Username must be present"
      element.send_keys("")
      element1.send_keys("Admin")
      element1.send_keys(Keys.RETURN)
      if Actualmsg =='':
            error = driver.find_element_by_xpath("//div[@class='alert alert-warning']")
            Actualmsg1=error.text
            self.assertEqual(expectedmsg, Actualmsg1)
      else:
            self.assertIn(driver.current_url,login_after)
            #self.assertTrue(logo.is_displayed())    
     

     except (AssertionError,Exception) as x:
                pas=False
                print("Error3:",x)
     try:
      Actualmsg=""
      expectedmsg="Password must be present"        
      #case no Password
      driver.find_element_by_id('password').clear()
      element.send_keys("Admin")
      element1.send_keys("")
      element1.send_keys(Keys.RETURN)
      if Actualmsg =='':
            error = driver.find_element_by_xpath("//div[@class='alert alert-warning']")
            Actualmsg1=error.text
            self.assertEqual(expectedmsg, Actualmsg1)
      else:
            self.assertIn(driver.current_url,login_after)

     except (AssertionError,Exception) as x:
                pas=False
                print("Error3:",x)
     try:
      Actualmsg=""
      expectedmsg="Both Username and Password must be present"           
      #case no username and  Password
      driver.find_element_by_id('username').clear()
      element.send_keys("")
      element1.send_keys("")
      element1.send_keys(Keys.RETURN)
      if Actualmsg =='':
            error = driver.find_element_by_xpath("//div[@class='alert alert-warning']")
            Actualmsg1=error.text
            self.assertEqual(expectedmsg, Actualmsg1)
      else:
            self.assertIn(driver.current_url,login_after)


     except (AssertionError,Exception) as x:
                pas=False
                print("Error3:",x)
     try:                    
      #case with username and  Password
      element.send_keys("Admin")
      element1.send_keys("Admin")
      element1.send_keys(Keys.RETURN)
 
      self.assertIn(driver.current_url,login_after)

     except (AssertionError,Exception) as x:
                pas=False
                print("Error3:",x)

     if pas==True:
          print("Test2 Passed")
     else:
          print("Test2 Failed with assertion")
     print("-"*20)


     
    def test3(self):
      print("Test Case 3:Table Sort Test")
      pas=True
      table_id = driver.find_element_by_xpath('//*[@id="transactionsTable"]')

      rows_old = table_id.find_elements(By.TAG_NAME, "tr")
      old_table=Calc(rows_old).compute()
      
      element = driver.find_element_by_xpath('//*[@id="amount"]')
      element.click()
      
     
      rows_new = table_id.find_elements(By.TAG_NAME, "tr")

      new_table=Calc(rows_new).compute()

      
      for i,row in enumerate(rows_new):
            cols = row.find_elements(By.XPATH, '//*[@id="transactionsTable"]/tbody/tr["+i+"]/td[5]') 
      values=[float(("".join(col.text.split(" ", 2)[:2])).replace(",","")) for col in cols]
      
      sorted_values=sorted(values)
 
      try:
          self.assertEqual(values,sorted_values)
      except (AssertionError) as x:
            pas=False
            print("Error:",x)

      old_table=sorted(old_table)
      new_table=sorted(new_table)
      try:
          self.assertEqual(old_table,new_table)
      except (AssertionError) as x:
            pas=False
            print("Error:",x)

      if pas==True:
          print("Test3 Passed")
      else:
          print("Test3 Failed with assertion")
      print("-"*20)

      
    def test4(self):
      print("Test Case 4:Canvas Chart Test")
      pas=True
      i=1
      element= driver.find_element_by_xpath('//*[@id="showExpensesChart"]')
      element.click()

      element= driver.find_element_by_xpath('//*[@id="addDataset"]')
      element.click()
      

      
      old=scriptval(i).beforeclick()
      new=scriptval(i).afterclick()

      try:
          for i in old:
            self.assertIn(i,new)
      except (AssertionError) as x:
            pas=False
            print("Error:",x)
      if pas==True:
          print("Test4 Passed")
      else:
          print("Test4 Failed with assertion")
      print("-"*20)   
    time.sleep(2)

    
    def test5(self):
      print("Test Case 5:Dynamic Content Test")
      pas=True
      driver.get(urls+"?showAd=true")
      element = driver.find_element_by_id("username")
      element1 = driver.find_element_by_id("password")      
      element.send_keys("Admin")
      element1.send_keys("Admin")
      element1.send_keys(Keys.RETURN)
 
      
      try:
           g=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/img")))
           self.assertTrue(g.is_displayed())
  
      except (AssertionError,Exception) as x:
            pas=False
            print("Error:","gif not found")

                                
      try:

           g1=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[4]/img")))
           self.assertTrue(g1.is_displayed())

      except (AssertionError,Exception) as x:
            pas=False
            print("Error:","gif not found")
      if pas==True:
          print("Test5 Passed")
      else:
          print("Test5 Failed with assertion")
      print("-"*20)   
      driver.quit()

class scriptval:

    def __init__(self,i):
         self.i=i
    def beforeclick(self):
         old=[]
                        
         dump1=[10, 20, 30, 40, 50, 60, 70]
         dump2=[8, 9, -10, 10, 40, 60, 40]
         old.append(driver.execute_script('return window.barChartData.labels'))
         old.append(dump1)
         old.append(driver.execute_script('return window.barChartData.labels'))
         old.append(dump2)
         
         return old
    def afterclick(self):
    
        new=[]
       
        new.append(driver.execute_script('return window.barChartData.labels'))
        new.append(driver.execute_script('return window.barChartData.datasets[0].data'))
        new.append(driver.execute_script('return window.barChartData.labels'))
        new.append(driver.execute_script('return window.barChartData.datasets[1].data'))
        new.append(driver.execute_script('return window.barChartData.labels'))
        new.append(driver.execute_script('return window.barChartData.datasets[2].data'))
        
        return new       

class Calc:

    def __init__(self,rows):
         self.rows=rows

    def compute(self):
      temp=[]  
      for row in self.rows:
        
              row_vala=row.find_elements(By.XPATH, '//*[@id="transactionsTable"]/tbody/tr["+op+"]/td["+po+"]')
      for i in row_vala:
         temp.append(i.text)
      i=0
      new_list=[]
      while i<len(temp):
        new_list.append(temp[i:i+5])
        i+=5
      return new_list    

if  __name__=="__main__":
    unittest.main()
    
