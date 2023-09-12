from selenium import webdriver

# if we are using chromebrowser on multiple projects, make sure to add it in the env paths of windows
# chrome_browser = webdriver.Chrome()
chrome_browser = webdriver.Chrome("./chromedriver.exe")

chrome_browser.get("https://www.seleniumeasy.com")
assert (
    "Learn Selenium with Best Practices and Examples | Selenium Easy"
    in chrome_browser.title
)

btn_text = chrome_browser.find_element_by_class_name("btn-dev").get_attribute(
    "innerHTML"
)
assert "Selenium Articles" in btn_text

# input element
user_msg = chrome_browser.find_element_by_id("user-message")
user_msg.clear()
# type in input
user_msg.send_keys("typing from selenium")


# close the current window
chrome_browser.close()
# close the browser, and executable
chrome_browser.quit()
