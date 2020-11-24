from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import FirefoxOptions
import time


# starts browser 
def startfirefox(url):
    global driver 
    #options = webdriver.FirefoxOptions() 
    #options.add_argument("start-maximized")
    #options.add_argument('disable-infobars')
    #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #options.add_experimental_option('useAutomationExtension', False)

    #startss driver or the browser
    # bypass the shit out of that damn bot detector
    
    profile = webdriver.FirefoxProfile(r"C:\Users\sc1\AppData\Roaming\Mozilla\Firefox\Profiles\hzjb16ht.default-release")
    PROXY_HOST = "12.12.12.123"
    PROXY_PORT = "1234"
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", PROXY_HOST)
    profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\firefox.exe", service_log_path='NUL')
    driver.maximize_window()
    #opens url 
    driver.get(url)
    
#configure info here
def config():
    email = input("Enter zoom email: ")
    password = input("Enter zoom password: ")
    zoomid = input("Enter zoom class ID: ")
    zoompwd = input("Enter zoom class password: ")
    print("User configured! \nJoining clas now...")
    joinclass(email, password, zoomid, zoompwd)
    return None

#automatically join class
def joinclass(email, password, id, pwd):
    url = 'https://zoom.us/signin'
    urlclass = 'https://zoom.us/wc/join/' + id
    startfirefox(url)
    
    #automatically sign in
    emailinput = driver.find_element_by_id("email")
    emailinput.send_keys(email)
    passinput = driver.find_element_by_id("password")
    passinput.send_keys(password)
    passinput.send_keys(Keys.RETURN)

    time.sleep(10)
    driver.get(urlclass)
    
    #time.sleep(30)
    #driver.find_element_by_id("recaptcha-anchor").click()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
    return True


if __name__ == "__main__":
    config()
