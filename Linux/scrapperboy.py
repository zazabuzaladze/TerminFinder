from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


START_URL = "https://termine.staedteregion-aachen.de/auslaenderamt/"


options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    driver.get(START_URL)

    # try:
    #     WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.ID, "cookieDismissButton"))
    #     ).click()
    #     #print("Cookie message dismissed.")
    # except TimeoutException:
    #     print("No cookie dismissal message found.")

    try:
        cookie_msg = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "cookie_msg"))
        )
        driver.execute_script("arguments[0].style.display = 'none';", cookie_msg)
        #print("Cookie message dismissed.")
    except TimeoutException:
        print("No cookie message found.")

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonfunktionseinheit-1"))
        ).click()
        #print("First button clicked.")
    except TimeoutException:
        print("The first button was not clickable within the timeout period.")

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

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button-plus-293"))
        ).click()
        #print("Third button clicked.")
    except TimeoutException:
        print("The third button was not clickable within the timeout period.")

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "WeiterButton"))
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

    try:
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "OKButton"))
        ).click()
        #print("Fifth button (OK) clicked.")
    except TimeoutException:
        print("The fifth button (OK) was not clickable within the timeout period.")

    
    try:
        try:
            iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
            driver.switch_to.frame(iframe)
            #print("Switched to iframe.")
        except Exception:
            #print("No iframe switch required.")
            pass

        sixth_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='select_location' and @value='Ausländeramt Aachen, 2. Etage auswählen']"))
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", sixth_button)
        sixth_button.click()
        #print("Sixth button clicked successfully.")
    except TimeoutException:
        print("The sixth button was not clickable within the timeout period.")
    except Exception as e:
        print("Error interacting with the sixth button:", e)
    finally:
        driver.switch_to.default_content()


    try:
        h2_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2.h1like"))
        )
        print(h2_element.text.strip())
    except TimeoutException:
        print("No <h2 class='h1like'> element found on the page within the timeout period.")

finally:
    driver.quit()
