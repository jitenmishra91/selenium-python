from selenium import webdriver

class userCreate:
	dr=webdriver.Chrome("C://selenium//chromedriver.exe")
	dr.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/auth/login");
	username=dr.find_element_by_id("txtUsername")
	username.send_keys("admin")
	password=dr.find_element_by_id("txtPassword")
	password.send_keys("admin")
	loginclick=dr.find_element_by_id("btnLogin")
	loginclick.click()