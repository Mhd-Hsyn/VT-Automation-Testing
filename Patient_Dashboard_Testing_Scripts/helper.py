"""
Helper file and its funstions for the Patient

"""

import time, random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


# Testing For the Dashboard 
def dashboard_testing(driver: WebDriver):
    """
    This function is responsible for the testing of the dashboard of the Patient 
    """
    target_div = driver.find_element(By.XPATH, "//div[@class='row draggable-cards' and @id='draggable-area']")
    all_cards= target_div.find_elements(By.XPATH, "//div[@class='col-lg-6 col-md-12']")

    time.sleep(2)
    print("Length is ______ ",len(all_cards))

    for index, card in enumerate(all_cards, start=1):
        if index == 5:
            break
        if index % 2 != 0 :
            scroll_amount = index * 100  # Adjust the multiplication factor as needed
            driver.execute_script(f"window.scrollTo(0, window.scrollY + {scroll_amount})")

        time.sleep(2)
        print(f"\n********** {index} is Start ***********")

        span_element = card.find_element(By.XPATH, ".//span[@class='float-right' and @id='panel2']")  # Adjusted XPath here
        all_labels = span_element.find_elements(By.XPATH, ".//label[@class='control-label warning']")  # Adjusted XPath here
        for index, label in enumerate(all_labels, start=1):
            if index == 2:
                svg_element = label.find_element(By.TAG_NAME, "svg")
                driver.execute_script(svg_element.get_attribute("onclick"))

                time.sleep(2)
                print("Click on SVG")
                close_element = driver.find_element(By.XPATH, "//a[contains(@onclick, 'closeViewCasePannel')]")
                close_element.click()
                print("Click on CLOSE\n")
                time.sleep(2)



def all_appointments_panel(driver: WebDriver):
    """
    This function is responsible for the testing of the all_appointments_panel of the Patient 
    where all Current Appointments of the perticular patient is available
    """
    target_div = driver.find_element(By.XPATH, "//div[@class='row draggable-cards' and @id='draggable-area']")
    all_cards= target_div.find_elements(By.XPATH, "//div[@class='col-md-6 col-sm-12']")

    for index, card in enumerate(all_cards, start=1):
        if index == 5:
            break
        if index % 2 != 0 :
            scroll_amount = index * 80  # Adjust the multiplication factor as needed
            driver.execute_script(f"window.scrollTo(0, window.scrollY + {scroll_amount})")
            time.sleep(2)

        a_tag = card.find_element(By.XPATH, ".//a[@id='panel21']")  # Adjusted XPath here
        driver.execute_script(a_tag.get_attribute("onclick"))
        time.sleep(2)
        close_element = driver.find_element(By.XPATH, "//a[contains(@onclick, 'closeViewCasePannel')]")
        close_element.click()
        time.sleep(2)




def book_appointments_panel(driver: WebDriver):
    book_appointment_date = 12

    """
    This Function is for testing the Booking Appointment Process of the Patient
    """

    time.sleep(3)
    # Click on "Register Clinics"
    target_div = driver.find_element(By.XPATH, "//div[@class='active mt-2 col-md-7 col-sm-12' and @id='panel5']")
    a_tag = target_div.find_element(By.XPATH, ".//a[@class='btn btn-primary']")
    a_tag.click()
    time.sleep(3)
    
    # Click on "Canada Clinic"
    canada_clinic_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Canada Clinic"))
    )
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {200})")
    canada_clinic_link.click()
    time.sleep(3)

    # Click on the "Continue" button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']"))
    )
    continue_button.click()
    time.sleep(10)

    # Click Book Slot of Dr Hamza Ameer
    target_div =  driver.find_element(By.XPATH, "//div[@class='row draggable-cards' and @id='draggable-area']")
    all_card_div = target_div.find_elements(By.XPATH, ".//div[@class='col-md-6 col-sm-12']")
    dr_hamza_ameer_card = all_card_div[1]
    book_slot_btn = dr_hamza_ameer_card.find_element(By.XPATH, ".//button[@type='button' and @id='panel7']")
    book_slot_btn.click()
    print("click on the Book Slot of Dr Hamza Ameer")

    print("select the DR Hamza Ameer and time start")
    time.sleep(5)
    print("time end")

    # # ********** Change The Month for slot booking ********** 
    # # Find the next month element by XPath
    # next_month = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@title='Next' and @data-handler='next']"))
    # )
    # next_month.click()
    # time.sleep(2)
    # next_month = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@title='Next' and @data-handler='next']"))
    # )
    # next_month.click()
    # time.sleep(2)

    ## ********** for current date ********** 
    # select_current_date = driver.find_element(By.XPATH, "//td[contains(@class, 'ui-datepicker-days-cell-over') and contains(@class, 'ui-datepicker-current-day') and contains(@class, 'ui-datepicker-today')]")
    # select_current_date.click()
    # driver.execute_script(f"window.scrollTo(0, window.scrollY + {200})")

    # For Random selection of Day
    date_table = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']")
    all_td = date_table.find_elements(By.XPATH, ".//td[not(contains(@class, 'ui-datepicker-week-end')) and not(contains(@class, 'ui-datepicker-today'))][@data-handler='selectDay' and @data-event='click']")
    
    random_select_day = random.choice(all_td)
    random_select_day.click()
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {500})")
    print("Select the Random Date ------ and ------- New time start")
    time.sleep(7)
    print("New time end")

    all_available_scedule = driver.find_elements(By.XPATH, "//input[@id='openConsultation2' and @onclick='status()']")
    random.choice(all_available_scedule).click()
    time.sleep(3)

    # Click on Next Button after Selecting Appointmnet Date and time slot
    next_btn = driver.find_element(By.XPATH, "//button[@id='checkavaiilibiltyStatus' and text()='Next']")
    next_btn.click()
    
    time.sleep(3)
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {1500})")
    time.sleep(2)


    # Directly Click on the "Describe a Problem"
    next_btn3 = driver.find_element(By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary') and contains(@class, 'mb-2') and contains(@class, 'nxtbtn3') and @onclick='tourstart3()'][text()='Next']")
    next_btn3.click()

    time.sleep(3)
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {1500})")
    time.sleep(2)
    
    # Directly click on upload images 
    next_btn4 = driver.find_element(By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary') and contains(@class, 'nxtbtn4') and contains(@class, 'mb-2')][text()='Next']")
    next_btn4.click()

    time.sleep(2)
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {1500})")
    time.sleep(2)
    
    # Directly click on Completeion
    next_btn_complete = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn btn-primary mb-2' and @id='step67']")
    next_btn_complete.click()
    
    time.sleep(2)
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {3500})")
    time.sleep(2)

    # Accept Terms and Condition
    accept_btn = driver.find_element(By.XPATH,  "//button[@class='btn btn-primary' and @type='button' and @onclick='Accept()']")
    accept_btn.click()
    time.sleep(2)
    # click book appointment btn
    bk_apoint_btn = driver.find_element(By.XPATH, "//button[@class= 'btn btn-primary' and @id='book_appointment']")
    bk_apoint_btn.click()

    time.sleep(20)




# My Consultation Panel 
def consultation_panel_testing(driver: WebDriver):
    """
    Rating the doctor and 
    Cancel Booked Appointment 
    """
    try:
        time.sleep(2)
        # Scroll Horizontally
        element = driver.find_element_by_class_name('card-body.table-responsive')
        driver.execute_script("arguments[0].scrollLeft += 1000;", element)
        time.sleep(5)
        table = driver.find_element(By.XPATH, "//table[@id='zero_config' and @class='table table-striped table-bordered display dataTable no-footer']")
        tbody = table.find_element(By.XPATH, ".//tbody")
        all_rows = tbody.find_elements(By.XPATH, ".//tr[contains(@class, 'odd') or contains(@class, 'even')]")
        first_row = all_rows[0]
        
        print("\n******** Start RATING *******")
        # rating stars
        ratingfield = first_row.find_element(By.XPATH, ".//fieldset[@class='rating']")
        
        all_labels = ratingfield.find_elements(By.XPATH, ".//label[@class='full']")
        for star in reversed(all_labels):
            star.click()
            time.sleep(2)

        print("\n******** COMPLETE RATING *******")

        all_td = first_row.find_elements(By.XPATH, ".//td[@class='text-center']")

        # for attachment btn
        attachment_td = all_td[-2]
        attachment_svg = attachment_td.find_element(By.TAG_NAME, "svg")
        attachment_svg.click()
        time.sleep(1)
        attachment_popup= driver.find_element(By.XPATH, "//div[@id='exampleModalattachment']")
        cancel_btn = attachment_popup.find_element(By.XPATH, ".//button[@type='button' and @data-dismiss='modal']")
        cancel_btn.click()
        time.sleep(1)

        # for viewcase 
        viewcase_td = all_td[-4]
        viewcase_btn = viewcase_td.find_element(By.TAG_NAME, "svg")
        viewcase_btn.click()
        time.sleep(2)
        viewcase_popup= driver.find_element(By.XPATH, "//asidee[@id='view-panel']")
        close_element = viewcase_popup.find_element(By.XPATH, ".//a[contains(@onclick, 'closeViewCasePannel')]")
        close_element.click()
        time.sleep(1)

        cancel_td = all_td[-1]
        svg_element = cancel_td.find_element(By.TAG_NAME, "svg")
        svg_element.click()
        # driver.execute_script(svg_element.get_attribute("onclick"))
        time.sleep(5)

        # horizontal scroll again
        element = driver.find_element_by_class_name('card-body.table-responsive')
        driver.execute_script("arguments[0].scrollLeft += 1000;", element)
        
    except Exception as e :
        print(e)





def profile_panel_testing(driver: WebDriver):
    time.sleep(3)
    try:
        # Fill out the form
        first_name_input = driver.find_element_by_name("First_Name")
        first_name_input.clear()
        time.sleep(1)
        first_name_input.send_keys("Huzaifa Khalil")
        time.sleep(1)

        last_name_input = driver.find_element_by_name("Last_Name")
        last_name_input.clear()
        time.sleep(1)
        last_name_input.send_keys("Khalil Ur Rehman")
        time.sleep(1)


        gender_select = Select(driver.find_element_by_name("Gender"))
        gender_select.select_by_value("Female")  # Select Male or Female based on your preference
        time.sleep(1)

        # Submit the form
        submit_button = driver.find_element_by_xpath("//button[contains(text(),'Update Profile')]")
        submit_button.click()
        # Close the browser after submission
        time.sleep(5)  # Wait for 5 seconds to see the result


        # ********* RECHANGE THE FORM AGAIN  ************ 

        first_name_input = driver.find_element_by_name("First_Name")
        first_name_input.clear()
        time.sleep(1)
        first_name_input.send_keys("Huzaifa")
        time.sleep(1)

        last_name_input = driver.find_element_by_name("Last_Name")
        last_name_input.clear()
        time.sleep(1)
        last_name_input.send_keys("Khalil")
        time.sleep(1)

        gender_select = Select(driver.find_element_by_name("Gender"))
        gender_select.select_by_value("Male")
        time.sleep(1)

        # Submit the form
        submit_button = driver.find_element_by_xpath("//button[contains(text(),'Update Profile')]") 
        submit_button.click()
        time.sleep(5)  # Wait for 5 seconds to see the result

        
    except Exception as e :
        print(e)
