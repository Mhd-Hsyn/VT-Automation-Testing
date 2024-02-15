"""
Helpers Function for Testing the Doctors Panel 

"""

import time, random
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select





# Testing For the Dashboard 
def dashboard_testing(driver: WebDriver):
    """
    This function is responsible for the testing of the dashboard of the Patient 
    """
    target_div = driver.find_element(By.XPATH, "//div[@class='row draggable-cards' and @id='draggable-area']")
    all_cards= target_div.find_elements(By.XPATH, "//div[@class='col-lg-6  col-md-12 col-sm-12']")

    time.sleep(2)
    print("Length is ______ ",len(all_cards))

    for index, card in enumerate(all_cards, start=1):
        if index == 5:
            break
        if index % 2 != 0 :
            scroll_amount = index * 100  # Adjust the multiplication factor as needed
            # driver.execute_script(f"window.scrollTo(0, window.scrollY + {scroll_amount})")

        time.sleep(2)
        print(f"\n********** {index} is Start ***********")
       
        span_element = card.find_element(By.XPATH, ".//span[@class='float-right' and @id='panel3']")
        eye_labels = span_element.find_elements(By.XPATH, ".//label[@class='control-label warning']")[1]
        svg_element = eye_labels.find_element(By.TAG_NAME, "svg")
        driver.execute_script(svg_element.get_attribute("onclick"))

        time.sleep(2)
        print("Click on SVG")
        close_element = driver.find_element(By.XPATH, "//a[contains(@onclick, 'closeViewCasePannel')]")
        close_element.click()
        print("Click on CLOSE\n")
        time.sleep(2)



def all_appointments_panel(driver: WebDriver):
    """
    This function is responsible for the testing of the all_appointments_panel of the Doctor 
    where all Current And Previous Appointments of the perticular Doctor is available
    """

    # main_div= driver.find_element(By.XPATH, "//div//[@class='card-body']")
    target_ul= driver.find_element(By.XPATH, ".//ul[@class='nav nav-tabs customtab' and @role='tablist']")
    all_li = target_ul.find_elements(By.XPATH, ".//li[@class='nav-item']")
    
    # 2 a_tags (one for current appointment other previous appointment)
    for main_index, li in enumerate(all_li):
        a_tag= li.find_element(By.TAG_NAME, "a")
        a_tag.click()

        if main_index == 0 :
            main_div= driver.find_element(By.XPATH, "//div[@class='tab-pane p-4 active' and @id='home2']")
            target_div = main_div.find_element(By.XPATH, ".//div[@class='row draggable-cards' and @id='draggable-area']")
            all_cards= target_div.find_elements(By.XPATH, ".//div[@class='col-lg-6 col-md-12 col-sm-12']")

            for index, card in enumerate(all_cards, start=1):
                if index == 5:
                    break
                if index % 2 != 0 :
                    scroll_amount = index * 80  # Adjust the multiplication factor as needed
                    # driver.execute_script(f"window.scrollTo(0, window.scrollY + {scroll_amount})")
                    time.sleep(2)
                
                a_tag = card.find_element(By.XPATH, ".//a[@id='panel25']")  # Adjusted XPath here
                driver.execute_script(a_tag.get_attribute("onclick"))
                time.sleep(2)
                close_element = driver.find_element(By.XPATH, "//a[contains(@onclick, 'closeViewCasePannel')]")
                close_element.click()
                time.sleep(2)
            

        if main_index== 1:

            main_div= driver.find_element(By.XPATH, "//div[@class='tab-pane p-4 active' and @id='profile2']")
            target_div = main_div.find_element(By.XPATH, ".//div[@class='row draggable-cards' and @id='draggable-area']")
            all_cards= target_div.find_elements(By.XPATH, ".//div[@class='col-md-12 col-lg-6']")

            for index, card in enumerate(all_cards, start=1):
                if index == 5:
                    break
                if index % 2 != 0 :
                    scroll_amount = index * 80  # Adjust the multiplication factor as needed
                    # driver.execute_script(f"window.scrollTo(0, window.scrollY + {scroll_amount})")
                    time.sleep(2)
                cardbody= card.find_element(By.XPATH, ".//div[@class='card-body']")
                # print("\n\n *********CARD BODY******** \n\n",cardbody.get_attribute("outerHTML"))
                span_tag= cardbody.find_element(By.XPATH, ".//span[@class='float-right']")
                # print("\n\n *********SPAN******** \n\n",span_tag.get_attribute("outerHTML"))
                eye_label = span_tag.find_elements(By.XPATH, ".//label[@class='control-label warning']")[0]
                svg = eye_label.find_element(By.TAG_NAME, "svg")
                # print("\n\n *********svg******** \n\n",svg.get_attribute("outerHTML"))
                driver.execute_script(svg.get_attribute("onclick"))
                time.sleep(2)



# Doctor Schedule Panel Testing 
def dr_schedule_panel_testing(driver: WebDriver):
    try:
        time.sleep(2)
        # Get today's date
        today = datetime.now()
        # Calculate the start date (today + 1 day)
        start_date = today + timedelta(days=1)
        # Calculate the end date (start date + 1 week)
        end_date = start_date + timedelta(weeks=1)
        # Format the dates as "DD-MM-YYYY"
        start_date_formatted = start_date.strftime("%m-%d-%Y")
        end_date_formatted = end_date.strftime("%m-%d-%Y")

        # for selecting the date range
        target_div= driver.find_element(By.XPATH, "//div[@class='material-card card' and @id='panel12']")
        start_date_range_ele= target_div.find_element(By.XPATH, ".//div[@class='col-md-3' and @id='panel13']")
        s_date_input= start_date_range_ele.find_element(By.XPATH, ".//input[@id='sdate']")
        s_date_input.clear()
        s_date_input.send_keys(start_date_formatted)
        time.sleep(2)

        end_date_range_ele= target_div.find_element(By.XPATH, ".//div[@class='col-md-3' and @id='panel14']")
        e_date_input= end_date_range_ele.find_element(By.XPATH, ".//input[@id='edate']")
        e_date_input.clear()
        e_date_input.send_keys(end_date_formatted)
        time.sleep(2)

        price_ele= target_div.find_element(By.XPATH, ".//div[@class='col-md-3' and @id='panel15']")
        price_input = price_ele.find_element(By.XPATH, ".//input[@id='Price']")
        price_input.clear()
        price_input.send_keys("200")

        appointment_duration= target_div.find_element(By.XPATH, ".//div[@class='col-md-3' and @id='panel16']")
        duration_btn= appointment_duration.find_element(By.TAG_NAME, "button")
        duration_btn.click()
        time.sleep(2)

        # all days duration in week 5 minutes to 30 mintues option 
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        for day in days:
            select_ele= driver.find_element(By.XPATH, f"//select[@id='{day}Duration']")
            all_options = select_ele.find_elements(By.XPATH, ".//option[@value!='false']")
            random_option = random.choice(all_options)
            random_option.click()
            time.sleep(2)
        
        save_changes_btn = driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and text()='Save changes']")
        save_changes_btn.click()
        
        time.sleep(2)
        
        driver.execute_script(f"window.scrollTo(0, window.scrollY + {2000})")
        input_field_names = {
            'Monday': ('mondayfrom', 'mondayto'),
            'Tuesday': ('tuesdayfrom', 'tuesdayto'),
            'Wednesday': ('wedfrom', 'wedto'),
            'Thursday': ('thursFrom', 'thursto'),
            'Friday': ('frifrom', 'frito'),
            'Saturday': ('satfrom', 'satto')
        }

        for day in days:
            driver.execute_script(f"window.scrollTo(0, window.scrollY + {2000})")

            day_link = driver.find_element(By.XPATH, f"//a[@class='card-title' and normalize-space()='{day}']")
            day_link.click()
            time.sleep(1)
            

            availability_div = driver.find_element(By.XPATH, f".//div[@id='{day.lower()}' and @data-get='{day.lower()}']")
            
            # using the dict call the input field name
            from_input_day, to_input_day= input_field_names[day]

            from_input = availability_div.find_element(By.XPATH, f".//input[@name='{from_input_day}']")
            to_input = availability_div.find_element(By.XPATH, f".//input[@name='{to_input_day}']")


            # Clear the input field
            from_input.clear()
            random_time = random.randint(13, 17)
            start_time= f"{random_time}:00"
            end_time= f"{random_time+2}:00"

            # Input a new value
            from_input.send_keys(start_time)
            
            # Similar actions can be performed for the 'To' input element
            to_input.clear()
            to_input.send_keys(end_time)

            time.sleep(2)

        button = driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Save Schedule']")
        button.click()

    except Exception as e:
        print(e)








# DOCTOR My CASES Panel 
def cases_panel_testing(driver: WebDriver):
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
        table = driver.find_element(By.XPATH, "//table[@id='multi_col_order' and @class='table table-striped table-bordered display dataTable no-footer']")
        tbody = table.find_element(By.XPATH, ".//tbody")
        all_rows = tbody.find_elements(By.XPATH, ".//tr[contains(@class, 'odd') or contains(@class, 'even')]")
        first_row = all_rows[1]

        all_td = first_row.find_elements(By.XPATH, ".//td[@class='text-center']")
        
        # For Attachment
        attachment_td = all_td[-1]
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


        # Accept/Rejected Appointments by Doctor
        select_status_td= all_td[-3]
        select_ele = select_status_td.find_element(By.XPATH, ".//select[@class='form-control'  and contains(@onchange, 'AppointmentStatusChange')]")
        option= select_ele.find_element(By.XPATH, ".//option[@value='Rejected' or @value='Accept']")
        option.click()
        time.sleep(2)
        # For Javascript ALERT 
        try:
            # Switch to the alert
            alert = driver.switch_to.alert
            
            # Accept the alert (click OK)
            alert.accept()
            print("Alert accepted successfully.")
        except:
            print("No alert present.")
        
        time.sleep(5)        

    except Exception as e :
        print(e)





def profile_panel_testing(driver: WebDriver):
    time.sleep(3)
    try:
        # target_div = driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']")
        # a_tag = target_div.find_element(By.XPATH, ".a//[@onclick='ToggleClass']")
        # a_tag.click()

        # Fill out the form
        first_name_input = driver.find_element_by_name("First_Name")
        first_name_input.clear()
        time.sleep(1)
        first_name_input.send_keys("Dr. xyz")
        time.sleep(1)

        last_name_input = driver.find_element_by_name("Last_Name")
        last_name_input.clear()
        time.sleep(1)
        last_name_input.send_keys("Bibi")
        time.sleep(1)

        gender_select = Select(driver.find_element_by_name("Gender"))
        gender_select.select_by_value("Female")  # Select Male or Female based on your preference
        time.sleep(1)

        date_of_birth_input = driver.find_element_by_name("Date_of_Birth")
        date_of_birth_input.clear()
        time.sleep(1)
        date_of_birth_input.send_keys("09-22-1966")  # Enter your date of birth in this format
        time.sleep(1)

        degree_input = driver.find_element_by_name("Degree")
        degree_input.clear()
        time.sleep(1)
        degree_input.send_keys("PhD")
        time.sleep(1)

        driver.execute_script(f"window.scrollTo(0, window.scrollY + {200})")

        # Submit the form
        submit_button = driver.find_element_by_xpath("//button[contains(text(),'Update Profile')]")
        submit_button.click()
        # Close the browser after submission
        time.sleep(5)  # Wait for 5 seconds to see the result


        # ********* RECHANGE THE FORM AGAIN  ************ 

        first_name_input = driver.find_element_by_name("First_Name")
        first_name_input.clear()
        time.sleep(1)
        first_name_input.send_keys("Hamza")
        time.sleep(1)

        last_name_input = driver.find_element_by_name("Last_Name")
        last_name_input.clear()
        time.sleep(1)
        last_name_input.send_keys("Ameer")
        time.sleep(1)

        gender_select = Select(driver.find_element_by_name("Gender"))
        gender_select.select_by_value("Male")
        time.sleep(1)

        date_of_birth_input = driver.find_element_by_name("Date_of_Birth")
        date_of_birth_input.clear()
        time.sleep(1)
        date_of_birth_input.send_keys("01-25-1997")  # Enter your date of birth in this format
        time.sleep(1)

        degree_input = driver.find_element_by_name("Degree")
        degree_input.clear()
        time.sleep(1)
        degree_input.send_keys("Masters")
        time.sleep(1)

        # Submit the form
        submit_button = driver.find_element_by_xpath("//button[contains(text(),'Update Profile')]") 
        submit_button.click()
        time.sleep(5)  # Wait for 5 seconds to see the result

        
    except Exception as e :
        print(e)


