# (Work In Progress) B-WITHUS-AUTOBOT
# This is a passion project i am a Beginner  
# 🏠 B-With-Us Auto-Bid Bot

A fully automated bot built in Python to monitor and place bids on housing listings from the [B-With-Us](https://www.b-with-us.co.uk/) platform, tailored for specific towns of interest. The bot scans listings regularly and automatically places bids on your behalf when matches are found — saving you time and ensuring you're always one step ahead in the housing game.

---

## 🚀 Features

- 🔍 **Real-Time Property Scanning**  
  Continuously monitors the B-With-Us property listings page to detect new eligible properties.

- 🧠 **Smart Town Filtering**  
  Only targets properties located in towns you care about. Easily configurable via a list.

- 🤖 **Automated Bidding**  
  Uses Selenium WebDriver to log in, navigate to property pages, and place bids automatically.

- 🌐 **Web Automation via Selenium**  
  Emulates human interaction with the B-With-Us portal, including form submission and bid confirmation.

- 💬 **Verbose Debug Output**  
  Includes detailed debug logging throughout, making it easier to trace errors and monitor the bot's actions.

- 🛠️ **Modular & Maintainable Code**  
  Refactored for clarity, separation of concerns, and easy extensibility.

---

## ⚙️ How It Works

1. **Session Initialization**  
   The bot uses `requests` to fetch the B-With-Us listings page and `BeautifulSoup` to parse the property details.

2. **Town Matching**  
   It scans each property and checks whether its location matches any of the towns listed in `TARGET_TOWNS`.

3. **Bidding Trigger**  
   When a match is found, the bot launches a visible (non-headless) Chrome browser using Selenium.

4. **Authentication**  
   Logs in using your credentials on the B-With-Us login page.

5. **Bid Execution**  
   Automatically navigates to the matched property page, clicks the "Apply" and "CONFIRM" buttons, and places the bid.

6. **Sleep & Repeat**  
   The bot sleeps for a specified interval (`CHECK_INTERVAL`) and then restarts the scan loop.

---

## 🧾 Configuration

You can easily update the following values in the script:

```python
TARGET_TOWNS = ["Rawtenstall", "Crawshawbooth", "BARNOLDSWICK"]
USERNAME = "your_email@example.com"
PASSWORD = "your_password"
CHECK_INTERVAL = 5  # Time in seconds between scans
```

> ⚠️ **Keep your credentials secure!** Consider using environment variables or a `.env` file in production.

---

## 🧰 Tech Stack

- **Python 3**
- **Selenium**
- **BeautifulSoup**
- **Requests**
- **WebDriver Manager** (for auto-installing/updating ChromeDriver)

---

## 📸 Screenshots

> Add a few screenshots or even a screen recording here of the browser opening, logging in, and placing a bid.

---

## 🧪 Example Output

```text
[INFO] Starting housing monitor bot...
[DEBUG] Checking properties...
[DEBUG] Found 4 properties
[MATCH] Found property in Rawtenstall: 2 Bed Flat
[INFO] Starting bid process for https://www.b-with-us.co.uk/property-details
[DEBUG] Logging in...
[SUCCESS] Bid placed!
[WAIT] Sleeping for 5 seconds...
```

---

## 📦 Setup & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/bwithus-auto-bid.git
   cd bwithus-auto-bid
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the bot:
   ```bash
   python bwithus.py
   ```

---

## ✅ To-Do / Improvements

- [ ] Use `.env` or secure credential storage
- [ ] Add email or SMS notifications on successful bid
- [ ] Add Docker support for easy deployment
- [ ] Support headless mode toggle via CLI flag
- [ ] Unit tests for property parsing

---

## 🙏 Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- B-With-Us for making listings publicly accessible

---

## 📜 License

MIT License. Feel free to use and modify this project — contributions welcome!
