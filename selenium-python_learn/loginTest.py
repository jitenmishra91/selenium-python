from selenium import webdriver

class LoginTest:
	dr=webdriver.Chrome("C://selenium//chromedriver.exe")
	dr.get("https://opensource-demo.orangehrmlive.com/")
	username=dr.find_element_by_id("txtUsername")
	username.send_keys("admin")