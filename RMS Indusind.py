import time
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(r"https://uatweb.insurekkart.com/")
driver.maximize_window()
time.sleep(3)

# --- Select Health Insurance ---
health = driver.find_element(By.XPATH, '//*[@id="main_content"]/div/div/div/div[4]/div/a/div')
health.click()
time.sleep(1)

# --- Fill contact form ---
driver.find_element(By.XPATH, "//input[@type='radio' and @value='female']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@type='text'][1]").send_keys("Soumya")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Pattanshetti")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 500);")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("souwm248@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='mobile_number']").send_keys("8137643243")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='pincode']").send_keys("560039")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='political' and @value='No']").click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="health-data-contine"]').click()
time.sleep(6)

# --- Fill member details ---
driver.find_element(By.XPATH, "//div[@data-bs-target='#modalSelf']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//select[@name='selfAge']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='54']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Next']").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="10L"]').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="applyAllFilters"]').click()
time.sleep(1)
# --- Scroll to load quote comparison buttons ---
driver.execute_script("window.scrollTo(0, 3000);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(5)

# --- Provider IDs ---
provider_ids = {
    "GoDigit": "29",
    "ICICI": "7",
    "Bajaj": "2",
    "Royal Sundaram": "13",
    "HDFC": "6",
    "IndusInd": "12",
    "Care": "20",
    "Niva Bupa": "9",
    "TATA AIG": "17",
}

insurer = "IndusInd"
product_name = "Health Infinity"
provider_id = provider_ids[insurer]

# --- Find all buy buttons for this insurer ---
buttons = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, f"a.btn-purchase[data-provider-id='{provider_id}']")
    )
)

# --- Find the specific product button ---
target_button = None
for button in buttons:
    data_item = button.get_attribute("data-item")
    if data_item:
        data = json.loads(data_item)
        if data.get("product_name") == product_name:
            target_button = button
            break

# --- Click it ---
if target_button:
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target_button)
    driver.execute_script("arguments[0].click();", target_button)
    print(f"{insurer} - {product_name} Buy Now clicked successfully.")
    time.sleep(5)  # let the modal load
else:
    print(f"{product_name} button not found for {insurer}.")

time.sleep(5)
driver.find_element("xpath", '//*[@id="modifyCarModal"]/div/div/div/div/button[2]').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="breakdownContent"]/div/div[5]/button[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, "//select [@class='form-select' and @id='proposer_DOBDD']/option[@value='20']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select [@class='form-select' and @id='proposer_DOBMM']/option[@value='05']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select [@class= 'form-select' and @id='members_0_dob_year' ]/option[@value='2001']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//select [@class= 'form-select' and @id='proposer_marital_status' ]/option[@value='2']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select[@name='proposer_occupation' and @id='proposer_occupation' ]/option[text()='Salaried']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select [@class='form-select me-2' and @id='members_0_height_ft' ]/option [6]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select [@class='form-select' and @id='members_0_height_in' ]/option [5]").click()
time.sleep(1)

driver.find_element(By.XPATH,"//input[@class='form-control' and @id='members_0_weight' ]").send_keys('50')
time.sleep(1)
driver.execute_script("window.scrollTo(0, 800);")
time.sleep(2)
driver.find_element(By.XPATH,"//select [@class='form-select' and @id='members_0_annual_income' ]/option [3]").click()
time.sleep(1)
# driver.find_element(By.XPATH,"//button [@class='btn btn-danger  validate-btn recalculate-premium bank-btn' and text()='Continue to Bank Details']").click()
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 100);")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='account_no']").send_keys('876545455667543456')
# time.sleep(1)
# driver.find_element("xpath", "//select [@id='accountType']/option[2]").click()
# time.sleep(1)
# driver.find_element("xpath","//input[@id='ifsc_code']").send_keys('hdfc0001234')
# time.sleep(1)
driver.find_element("xpath",'//*[@id="breakdownContent"]/div/div[4]/div[2]/div/button[2]').click()
time.sleep(15)
driver.find_element("xpath","//button[@id='premiumChange' and text()='OK']").click()
time.sleep(2)
driver.find_element("xpath", "//select[@id='nomineeTitle']/option[3]").click()
time.sleep(1)
driver.find_element("xpath","//input[@id='nomineeFirstName']").send_keys("sunitha")
time.sleep(1)
driver.find_element("xpath","//input[@id='nomineeLastName']").send_keys("C J")
time.sleep(1)
driver.find_element("xpath","//select[@id='nomineeRelation']/option[3]").click()
time.sleep(1)
driver.find_element("xpath","//select[@id='nomineeDOBDD']/option[11]").click()
time.sleep(1)
driver.find_element("xpath","//select[@id='nomineeDOBMM']/option[07]").click()
time.sleep(1)
driver.find_element("xpath","//select[@id='nomineeDOBYY']/option [@value='1982']").click()
time.sleep(1)
driver.find_element("xpath","//button[text()='Continue to Address Details']").click()
time.sleep(2)
driver.find_element("xpath",'//*[@id="nomineeContactPhone"]').send_keys("8867345623")
time.sleep(2)
driver.find_element('xpath', '//*[@id="nomineeContactConfirmBtn"]').click()
time.sleep(1)
driver.find_element("xpath","//textarea[@placeholder='Enter Address Line']").send_keys("BTM")
time.sleep(1)
driver.find_element("xpath","//textarea[@placeholder='Enter Area / Locality']").send_keys("1st street")
time.sleep(1)
driver.find_element("xpath","//input[@placeholder='Enter your PAN number']").send_keys("FWEPP5265D")
time.sleep(1)
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(2)
driver.find_element("xpath","//button[@data-target='submitForm']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='terms-and-conditions']").click()
time.sleep(1)
driver.find_element("xpath","//button[@id='payNow']").click()
time.sleep(10)
driver.find_element("xpath","//button[text()='Continue to Payment']").click()
time.sleep(1)
driver.find_element("xpath",'//*[@id="btnPaytmRouter"]').click()
time.sleep(1)
driver.find_element("xpath", '//*[@id="rdoNB"]').click()
time.sleep(10)
driver.find_element("xpath",'//*[@id="ptm-nb-inner"]/div[2]/div[1]').click()
time.sleep(1)
driver.find_element("xpath",'//*[@id="checkout-button"]/button').click()
time.sleep(16)
driver.find_element("xpath","//a[@id='download-link']").click()
time.sleep(30)

