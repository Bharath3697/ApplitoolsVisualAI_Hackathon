from selenium import webdriver
from applitools.selenium import Eyes, Target
class Appli:
    Version1 = "https://demo.applitools.com/hackathon.html"
    Version2 = "https://demo.applitools.com/hackathonV2.html"
    url = Version2
    driver = webdriver.Chrome(
        executable_path="C:/Users/BharathK/Desktop/chromedriver.exe")
    eyes = Eyes()  
    api_key = 'Mb36HqwKXQGa5aPPmshDwlOalMdm2TuR7MT8OQqd7VY110'
    eyes.api_key = api_key
    try:

        driver.execute_script("document.body.style.zoom='zoom 100%'")
        
        eyes.open(driver, "Test app", "Applitool Hackathon Test3", {'width': 800, 'height': 600})
        
        driver.get(url)

        eyes.force_full_page_screenshot = True
        eyes.check("Login Window test", Target.window())
        userName = driver.find_element_by_id("username")
        userName.clear()
        passWord = driver.find_element_by_id("password")
        passWord.clear()
        buttonLogIn = driver.find_element_by_id("log-in")
        buttonLogIn.click()
        eyes.check("No UserName NO Password test",Target.window())
        userName.clear()
        userName.send_keys("username")
        passWord.clear()
        buttonLogIn.click()
        eyes.check(" UserName NO Password test", Target.window())
        userName.clear()
        passWord.clear()
        passWord.send_keys("password")
        buttonLogIn.click()
        eyes.check(" No UserName  Password test", Target.window())
        userName.clear()
        userName.send_keys("username")
        passWord.clear()
        passWord.send_keys("password")
        buttonLogIn.click()
        eyes.check("  UserName  Password test", Target.window())
        element = driver.find_element_by_xpath('//*[@id="amount"]')
        element.click()
        eyes.check("Tablesort Test",Target.window())
        expense = driver.find_element_by_id("showExpensesChart")
        expense.click()
        eyes.check("Before Canvas Test", Target.window())
        nextdata = driver.find_element_by_id("addDataset")
        nextdata.click()
        eyes.check("After Canvas Test", Target.window())
        driver.get(url+"?showAd=true")
        userName = driver.find_element_by_id("username")
        userName.clear()
        userName.send_keys("username")

        passWord = driver.find_element_by_id("password")
        passWord.clear()
        passWord.send_keys("password")
        buttonLogIn = driver.find_element_by_id("log-in")
        buttonLogIn.click()
        eyes.check("Ad Test",Target.window())

        results = eyes.close(False)
        print(results)
    finally:

        driver.quit()
       
        eyes.abort()
