import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")  # Assuming the Flask app is running locally

def solve_captcha_manually():
    # Placeholder function to simulate manual CAPTCHA solving
    print("Please solve the CAPTCHA manually.")



def scrape_dashboard_data(driver):
    table= driver.find_element(By.ID,"DB-T1")#replace DB-T1 with the id of the element you wish to scrape data from
    rows = table.find_elements(By.TAG_NAME, "tr")#finds rows
    data = []
    for row in rows:#iterate over rows to dump in csv
        cols = row.find_elements(By.TAG_NAME, "td")
        data.append([col.text for col in cols])

    # Save the data to a CSV file
    csv_file_path = r"C:\Users\Srrijan Arora\Documents\Programming\Python\Web Scraping\dashboard_data.csv"#replace this with the path you wish to get CSV dump in
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Data scraped and saved to {csv_file_path}")#tells you the data has been scraped successfully
    pass


def login_with_selenium(email, password):#login driver method


    # Fill in the email field
    email_field = driver.find_element(By.ID, "email")#replace id with id of login field
    email_field.send_keys(Keys.BACKSPACE*50)#clear out any previous inputs left in the field, as email field is not autoclear
    email_field.send_keys(email)

    # Add a short delay before interacting with the password field
    time.sleep(1)

    # Fill in the password field
    password_field = driver.find_element(By.ID, "password")#replace with id of password field
    password_field.send_keys(password)

    # Find and click the submit button by its ID
    submit_button = driver.find_element(By.ID, "submit")#replace with id of submit field, here i am using clickable login button, so i send a click through script. can replace this with sending return
    submit_button.click()

    # Check if CAPTCHA is present
    try:
        captcha_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "g-recaptcha-response"))
        )
        solve_captcha_manually()  # Prompt the user to solve the CAPTCHA manually, as botting is against TOS
        print("Press Enter after solving the CAPTCHA.")
        input()  # Wait for user to press Enter after solving the CAPTCHA
        login_with_selenium(email,password)#re invoke method after captcha done
    except TimeoutException:
        pass  # No CAPTCHA found, continue with login process

    # Wait for the success message or error message
    try:
       dashboard_elem=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"DB-T1")))
       print("Login successful!")
       scrape_dashboard_data(driver)
    except TimeoutException:
        print("Login failed: Timeout - Couldn't find success message.")
        # Print page source for debugging
        print("Page source:", driver.page_source)
        # Take screenshot for debugging
        driver.save_screenshot("login_failed_screenshot.png")
    except Exception as e:
        print("An error occurred during login:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    #replace the credentials here in the script
    email = "sample24@examplemail.com"
    password = "s@mplepass^27"
    login_with_selenium(email, password)
