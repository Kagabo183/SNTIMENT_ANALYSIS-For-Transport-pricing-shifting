import time
import random
import csv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc

# Configuration
TWEET_URL = 'https://x.com/RURA_RWANDA/status/1863659059913576853'
OUTPUT_CSV = 'tweet_comments.csv'
MAX_DURATION = 60 * 60  # 60 minutes

def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    return uc.Chrome(options=options)

def wait_for_login():
    print("\n🔐 Please log in to Twitter (X).")
    input("➡️ After logging in and seeing your homepage, press ENTER here to continue...")

def scroll_until_done(driver, timeout=MAX_DURATION):
    start = time.time()
    last_height = driver.execute_script("return document.body.scrollHeight")
    stable_scrolls = 0
    all_comments = set()

    while time.time() - start < timeout:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("🔄 Scrolled down...")
        time.sleep(random.uniform(3, 6))

        new_comments = extract_replies(driver)
        old_count = len(all_comments)
        all_comments.update(new_comments)
        new_count = len(all_comments)

        print(f"💬 {new_count} unique comments collected so far")

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            stable_scrolls += 1
        else:
            stable_scrolls = 0

        if stable_scrolls >= 5:
            print("✅ No new content loading after several scrolls. Ending scroll.")
            break

        last_height = new_height

    return list(all_comments)

def extract_replies(driver):
    replies = set()
    try:
        tweet_blocks = driver.find_elements(By.XPATH, '//article[@role="article"]')
        for tweet in tweet_blocks:
            try:
                name_elem = tweet.find_element(By.XPATH, './/div[@data-testid="User-Name"]//span[1]')
                handle_elem = tweet.find_element(By.XPATH, './/div[@data-testid="User-Name"]//span[contains(text(), "@")]')
                comment_elem = tweet.find_element(By.XPATH, './/div[@data-testid="tweetText"]')

                name = name_elem.text.strip()
                handle = handle_elem.text.strip()
                comment = comment_elem.text.strip()

                if comment and len(comment) > 5:
                    replies.add((name, handle, comment))
            except NoSuchElementException:
                continue
    except NoSuchElementException:
        pass
    return replies

def save_to_csv(replies):
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Handle', 'Comment'])
        for name, handle, comment in replies:
            writer.writerow([name, handle, comment])
    print(f"\n✅ Saved {len(replies)} comments to '{OUTPUT_CSV}'")

def main():
    driver = setup_driver()
    driver.get("https://x.com/login")
    wait_for_login()

    driver.get(TWEET_URL)
    time.sleep(random.uniform(5, 8))  # Let tweet load

    all_comments = scroll_until_done(driver)
    driver.quit()

    print(f"\n💬 Total comments extracted: {len(all_comments)}")
    save_to_csv(all_comments)

if __name__ == '__main__':
    main()
