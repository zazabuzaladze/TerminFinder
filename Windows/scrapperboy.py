from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

# URL of the starting website
START_URL = "https://termine.staedteregion-aachen.de/auslaenderamt/" 

# Set up the Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the starting URL
    driver.get(START_URL)

    # # Dismiss cookie message if present
    # try:
    #     WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.ID, "cookieDismissButton"))  # Replace with actual button ID
    #     ).click()
    #     #print("Cookie message dismissed.")
    # except TimeoutException:
    #     print("No cookie dismissal message found.")

    # Click the first button to navigate to a new page
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonfunktionseinheit-1"))  # Clicking the button by its ID
        ).click()
        #print("First button clicked.")
    except TimeoutException:
        print("The first button was not clickable within the timeout period.")

    # Click the second header to expand it
    try:
        header_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "header_concerns_accordion-456"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", header_element)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "header_concerns_accordion-456"))
        ).click()
        #print("Second header clicked.")
    except TimeoutException:
        print("The second header was not clickable within the timeout period.")

    # Click the third button to increase a value
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button-plus-293"))  # Clicking the button by its ID
        ).click()
        #print("Third button clicked.")
    except TimeoutException:
        print("The third button was not clickable within the timeout period.")

    # Click the 'Weiter' button to proceed
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "WeiterButton"))  # Clicking the Weiter button by its ID
        ).click()
        #print("'Weiter' button clicked.")
    except ElementClickInterceptedException:
        #print("ElementClickInterceptedException: Trying to remove overlays.")
        driver.execute_script("document.getElementById('cookie_msg').style.display = 'none';")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "WeiterButton"))
        ).click()
        #print("'Weiter' button clicked after overlay removed.")
    except TimeoutException:
        print("The 'Weiter' button was not clickable within the timeout period.")

    # Click the fifth button (OK) to confirm action
    try:
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "OKButton"))  # Clicking the OK button by its ID
        ).click()
        #print("Fifth button (OK) clicked.")
    except TimeoutException:
        print("The fifth button (OK) was not clickable within the timeout period.")

    
    try:
        # Check for iframe and switch if necessary
        try:
            iframe = driver.find_element(By.CSS_SELECTOR, "iframe")  
            driver.switch_to.frame(iframe)
            #print("Switched to iframe.")
        except Exception:
            #print("No iframe switch required.")
            pass

        # Locate the sixth button using XPath
        sixth_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='select_location' and @value='Ausländeramt Aachen, 2. Etage auswählen']"))
        )

        # Scroll into view and click
        driver.execute_script("arguments[0].scrollIntoView(true);", sixth_button)
        sixth_button.click()
        #print("Sixth button clicked successfully.")
    except TimeoutException:
        print("The sixth button was not clickable within the timeout period.")
    except Exception as e:
        print("Error interacting with the sixth button:", e)
    finally:
        # Ensure to switch back to the main content after iframe interaction
        driver.switch_to.default_content()


    # Once on the desired page, find the <h2> element with class 'h1like'
    try:
        h2_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2.h1like"))
        )
        #print("Content of <h2 class='h1like'>:", h2_element.text.strip())
        print(h2_element.text.strip())
    except TimeoutException:
        print("No <h2 class='h1like'> element found on the page within the timeout period.")

finally:
    # Close the browser
    driver.quit()
