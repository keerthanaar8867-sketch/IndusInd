# IndusInd
End-to-end Health Insurance purchase automation using Python and Selenium WebDriver on the Insurekkart UAT website. Automates customer details, insurance plan selection, proposer and nominee details, address submission, payment gateway navigation, and document download.

Health Insurance Purchase Automation using Selenium
1. Project Overview

This project automates the end-to-end health insurance purchase journey on the Insurekkart UAT (User Acceptance Testing) website using Python and Selenium WebDriver.

The automation script navigates through the website, enters customer and nominee details, selects a health insurance plan, completes the proposal form, proceeds through the payment gateway, and attempts to download the final document.

Application URL: https://uatweb.insurekkart.com/

Automation Tool: Selenium WebDriver

Programming Language: Python

Browser: Google Chrome

2. Objectives
Automate the health insurance purchase workflow.
Enter customer contact and personal information.
Select the insured member's age and coverage amount.
Filter insurance plans and select a specific provider and product.
Fill in proposer, nominee, and address details.
Complete the proposal submission process.
Navigate through the payment gateway.
Download the final document, if available.
3. Technologies Used
Python 3
Selenium WebDriver
Google Chrome
ChromeDriver (managed automatically by compatible Selenium versions)
Python time module
Python json module
Selenium explicit waits and XPath/CSS selectors
4. Prerequisites

Before running the automation script, ensure that the following are installed:

Python 3.10 or a compatible version.
Google Chrome browser.
Selenium Python package.
Access to the Insurekkart UAT environment.
Valid test data for the customer, proposer, nominee, and payment workflow.
5. Installation
Step 1: Clone or download the project

Download the project files or clone the repository:

git clone <your-repository-url>
cd <your-project-folder>


Replace the repository URL and project folder with your actual details.

Step 2: Create a virtual environment (optional)
python -m venv venv


Activate the environment.

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

Step 3: Install dependencies
pip install selenium

Step 4: Run the script

Save the Python automation script as health_insurance_automation.py and execute:

python health_insurance_automation.py

6. Automation Workflow

The script executes the following steps in sequence.

Step 1: Launch the application
Launches Google Chrome.
Opens the Insurekkart UAT website.
Maximizes the browser window.
Step 2: Select Health Insurance
Clicks the Health Insurance option.
Opens the customer contact form.
Step 3: Enter customer contact details
Selects gender.
Enters first name and last name.
Enters email address and mobile number.
Enters the PIN code.
Selects the political exposure response.
Proceeds to the next stage.
Step 4: Enter insured member details
Selects the self member option.
Chooses the member's age.
Selects the insurance coverage amount of ₹10 lakh.
Applies the selected filters.
Scrolls through the page to load insurance quote options.
Step 5: Select the insurance provider and product

The script identifies the insurance provider using its provider ID and selects the product based on its product name.

Configured selection:

Insurance Provider: IndusInd
Product Name: Health Infinity
Provider ID: 12

The script locates the corresponding Buy Now button using a CSS selector and checks the button's data-item attribute to match the product name.

Step 6: Complete proposer details

The script enters or selects the following details:

Proposer date of birth.
Insured member's date of birth.
Marital status.
Occupation.
Height.
Weight.
Annual income.

It then proceeds through the proposal and premium calculation steps.

Step 7: Enter nominee details

The script fills in:

Nominee title.
Nominee first and last names.
Relationship with the proposer.
Nominee date of birth.
Nominee contact number.

It confirms the nominee contact details and proceeds to the address section.

Step 8: Enter address details

The script enters:

Address line.
Area or locality.
PAN number.

It then submits the relevant form and accepts the terms and conditions.

Step 9: Proceed to payment

The script:

Clicks the Pay Now button.
Proceeds to the payment gateway.
Selects the Paytm payment option.
Selects Net Banking.
Chooses the configured payment option.
Clicks the checkout button.

Note: Successful payment depends on the UAT gateway configuration, available test payment methods, and the application's response. Payment completion should be verified before treating the test as successful.

Step 10: Download the final document

After waiting for the payment flow to complete, the script clicks the download link.

The download should be verified by checking that the expected file exists and is not empty.

7. Insurance Provider Mapping

The script defines the following provider IDs:

Insurance Provider	Provider ID
GoDigit	29
ICICI	7
Bajaj	2
Royal Sundaram	13
HDFC	6
IndusInd	12
Care	20
Niva Bupa	9
TATA AIG	17

The provider and product can be changed using these variables:

insurer = "IndusInd"
product_name = "Health Infinity"
provider_id = provider_ids[insurer]


Ensure the provider ID and product name match the data returned by the application.

8. Important Implementation Notes
Explicit waits

The current script uses multiple time.sleep() statements. These can make execution slower and less reliable when page loading times vary.

Prefer Selenium explicit waits where possible:

wait = WebDriverWait(driver, 20)

element = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "health-data-contine")
    )
)

element.click()

Dynamic elements

Some elements may take additional time to load or may become stale after the page updates. Use explicit waits and re-locate elements when necessary.

Dropdown selection

For dropdowns, Selenium's Select class can make selections more readable:

from selenium.webdriver.support.ui import Select

dropdown = Select(
    driver.find_element(By.ID, "proposer_marital_status")
)

dropdown.select_by_value("2")

Browser and download handling

Configure a dedicated download directory and verify that the downloaded document exists before the script finishes.

Sensitive test data

Use authorized test data and approved UAT payment methods. Do not commit real customer information, PAN numbers, phone numbers, email addresses, bank details, or payment credentials to source control.

9. Troubleshooting
Issue	Possible Solution
Element not found	Verify the XPath or CSS selector and confirm the page has loaded.
Element not clickable	Wait for the element to become clickable and check for overlays or modals.
Product button not found	Confirm the provider ID and product_name match the page data.
Dropdown selection fails	Verify the option value and use Selenium's Select class.
Payment page does not load	Check UAT gateway availability and test payment configuration.
Download does not start	Verify the download link, browser settings, and download directory.
Script is too slow	Replace fixed sleeps with appropriate explicit waits.
10. Expected Outcome

When the application and test environment behave as expected, the script should:

Navigate through the health insurance purchase journey.
Select the configured insurance product.
Complete the required proposal and nominee forms.
Navigate through the UAT payment flow.
Attempt to download the final document.

The automation should be considered successful only after validating the expected application state, payment result, and downloaded document.

11. Limitations
The script relies on specific XPath and CSS selectors that may change when the application UI is updated.
Fixed delays may cause failures under slow or inconsistent network conditions.
The payment workflow depends on the UAT payment gateway and its supported test methods.
Clicking a download link does not guarantee that the file was downloaded successfully.
The current script does not include comprehensive exception handling, automated test reporting, or post-payment verification.
12. Future Enhancements
Replace fixed sleeps with explicit waits.
Add exception handling and structured logging.
Add screenshots on test failure.
Move test data into a configuration file or environment variables.
Add automated verification of payment status.
Validate the downloaded document.
Integrate the script with Pytest for repeatable test execution.
Generate HTML or JUnit test reports.
Use Page Object Model (POM) to improve maintainability.
13. Disclaimer

This automation is intended for authorized testing in the Insurekkart UAT environment. Use only approved test data and payment methods. Do not use the script to initiate unauthorized purchases or transactions in a production environment.
