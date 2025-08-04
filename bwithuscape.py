import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By  # missing import
import time 

print("[DEBUG] Setting Chrome options...")
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

print("[DEBUG] Initializing WebDriver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# CONFIG
TARGET_TOWNS = ["Rawtenstall", "Burnley", "BARNOLDSWICK"]
USERNAME = ""
PASSWORD = ""
BASE_URL = "https://www.b-with-us.co.uk/"
LISTINGS_URL = "https://www.b-with-us.co.uk/properties/?eligibleOnly=1"
LOGIN_URL = "https://www.b-with-us.co.uk/login/"
CHECK_INTERVAL = 5

def check_properties():
    print("[DEBUG] Entering check_properties()...")
    try:
        print("[DEBUG] Starting new session and requesting listings page...")
        session = requests.Session()
        response = session.get(LISTINGS_URL)
        print(f"[DEBUG] Received response: {response.status_code}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        properties = soup.find_all("div", class_="property-listing")
        print(f"[DEBUG] Found {len(properties)} properties")

        for prop in properties:
            print("[DEBUG] Inspecting a property...")
            title = prop.find("h2").text.strip()
            town = prop.find("span", class_="town").text.strip()
            print(f"[DEBUG] Property title: {title}, town: {town}")

            if any(town.lower() == t.lower() for t in TARGET_TOWNS):
                property_href = prop.find("a", href=True)["href"]
                print(f"[MATCH] Found property in {town}: {title}")
                return BASE_URL + property_href
        print("[DEBUG] No matching properties found.")
        return None
    except Exception as e:
        print(f"[ERROR] While checking properties: {e}")
        return None

def bid_on_property(property_url):
    print(f"[DEBUG] Entering bid_on_property() with URL: {property_url}")
    try:
        print(f"[INFO] Launching browser to bid on {property_url}")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Remove to view browser
        driver = webdriver.Chrome(options=chrome_options)

        print("[DEBUG] Navigating to login page...")
        driver.get(LOGIN_URL)
        print("[DEBUG] Filling in login form...")
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "loginBtn").click()
        print("[DEBUG] Submitted login form.")
        time.sleep(2)

        print("[DEBUG] Navigating to property page...")
        driver.get(property_url)
        time.sleep(2)

        print("[DEBUG] Attempting to click 'Apply' button...")
        bid_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
        bid_button.click()
        time.sleep(1)

        print("[DEBUG] Attempting to click 'CONFIRM' button...")
        confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'CONFIRM')]")
        confirm_button.click()

        print("[SUCCESS] Bid placed!")
    except NoSuchElementException as e:
        print(f"[ERROR] Element not found: {e}")
    except WebDriverException as e:
        print(f"[ERROR] WebDriver issue: {e}")
    except Exception as e:
        print(f"[ERROR] General issue in bid_on_property: {e}")
    finally:
        print("[DEBUG] Quitting browser...")
        driver.quit()

# ------------------ MAIN LOOP ------------------
if __name__ == "__main__":
    print("[INFO] Starting housing monitor bot...")
    while True:
        try:
            print("[DEBUG] Calling check_properties()...")
            property_url = check_properties()
            if property_url:
                print("[DEBUG] Property matched, calling bid_on_property()...")
                bid_on_property(property_url)
            else:
                print("[DEBUG] No property to bid on this cycle.")
        except Exception as e:
            print(f"[FATAL] Unhandled error: {e}")

        print(f"[WAIT] Sleeping for {CHECK_INTERVAL} seconds...\n")
        time.sleep(CHECK_INTERVAL)
