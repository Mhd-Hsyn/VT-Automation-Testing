"""
VT-Dashboard PATIENT Live Testing Automation using Selenium

https://portal.virtualtriage.ca/

"""


import time
from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from helper import(
    dashboard_testing,
    all_appointments_panel,
    book_appointments_panel,
    consultation_panel_testing,
    profile_panel_testing
)


def get_random_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US, en;q=0.5'
    }
    return headers

headers = get_random_headers()

print("\nMy Random Header is : \n", headers)
print("\n\n")

# for translation
prefs = {
  "translate_whitelists": {"ar":"en"},
  "translate":{"enabled":"true"}
}

# Set Chrome options
options = Options()
# options.headless = False
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
# options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
options.add_argument(f'user-agent={headers["User-Agent"]}')
options.add_argument('--no-sandbox')
options.add_argument("chrome://settings/")
options.add_argument("--lang=en") 
options.add_argument("--disable-translate")
options.add_experimental_option("prefs", prefs)  # for translation



def sysInit():
    display = Display(visible=0, size=(800, 600))
    # display.start()
    driver = None
    try:
        print(" *************** Starting Automation VT Dashboard *****************\n")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        driver.get("https://portal.virtualtriage.ca/login")
        
        time.sleep(2)

        # Enter email
        email_input = driver.find_element_by_id("uname")
        email_input.send_keys("dev.huzaifa.khalil@gmail.com")
        # email_input.send_keys("developer.hsyn@gmail.com")
        print("email_input")
        
        # Enter password
        password_input = driver.find_element_by_id("passwordInput")
        password_input.send_keys("Abc@1234")
        # password_input.send_keys("Dev@123456")
        print("password_input")
        
        # Select role
        role_select = driver.find_element_by_name("Role")
        role_select.click()
        time.sleep(1)  # Add a small delay to ensure the dropdown fully expands
        role_option = driver.find_element_by_xpath("//option[text()='Patient']")  # Change this to 'Practitioner' if needed
        role_option.click()
        print("role_select")


        # Enter Login
        submit_ele = driver.find_element_by_xpath("//input[@value='Login']")
        submit_ele.click()
        print("submit_ele")

        time.sleep(5)   # sleep for enter the OTP from email 

        # For OTP Verification
        otp_field = driver.find_element_by_id("number")
        otp_field.send_keys("123456")
        time.sleep(2)

        submit_ele = driver.find_element_by_xpath("//button[@type='submit']")
        submit_ele.click()

        time.sleep(10) # for refresh the new page

        try :
            tour_popup = driver.find_elements(By.XPATH, "//div[@class='popover tour tour-tour tour-tour-0 fade right in']")
            if tour_popup:
                # Find the "End Tour" button and click on it
                end_tour_button = driver.find_element(By.XPATH, "//button[@class='btn btn-warning endbtn1']")
                end_tour_button.click()
                print("Clicked on End Tour button")
        except:
            print("N0o POPUP")
            pass

        time.sleep(2)

        # DashBoard Testing
        dashboard_testing(driver= driver)
        time.sleep(5)

        # All Appointments Panel Testing
        try:
            appointment_ele = driver.find_element(
                By.XPATH,  "//li[@class='sidebar-item' and @id='panel18']"
                )
            appointment_ele.click()
            time.sleep(10)
            # calling the function for booking an appointment
            all_appointments_panel(driver)

        except Exception as e:
            print(e)
            pass

        time.sleep(5)


        # Book Appointment Panel Testing
        try:
            appointment_ele = driver.find_element(
                By.XPATH,  "//li[@class='sidebar-item' and @id='panel3']"
                )
            appointment_ele.click()
            time.sleep(10)
            # calling the function for booking an appointment
            book_appointments_panel(driver)

        except Exception as e:
            print(e)
            pass
        
        time.sleep(2)

        
        ##################################################


        # My Consultation Panel Testing
        try:
            print("\n\n****************** My Consultation Panel Testing Start ****************** ")
            consultation_ele = driver.find_element(
                By.XPATH,  "//li[@class='sidebar-item' and @id='panel15']"
                )
            consultation_ele.click()
            time.sleep(10)
            # calling the function for booking an appointment
            consultation_panel_testing(driver)

        except Exception as e:
            print(e)
            pass
        time.sleep(5)




        # # My Profile Panel Testing
        try:
            print("\n\n****************** My Profile Panel Testing Start ****************** ")
            profile_ele = driver.find_element(
                By.XPATH,  "//li[@class='sidebar-item' and @id='panel25']"
                )
            profile_ele.click()
            time.sleep(5)
            # calling the function for booking an appointment
            profile_panel_testing(driver)

        except Exception as e:
            print(e)
            pass


        time.sleep(5)


        # Logout
        try:
            print("\n\n****************** LOGOUT ****************** ")
            logout_ele = driver.find_element(
                By.XPATH,  "//li[@class='sidebar-item' and @id='panel38']"
                )
            logout_ele.click()
            time.sleep(10)
        except Exception as e:
            print(e)
            pass

        time.sleep(5)



    finally:
        print("QUIT WEB DRIVER ______________")
        # display.stop()
        if driver:
            driver.quit()


sysInit()