from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Browser
driver = webdriver.Chrome()

# Open App
driver.get("http://127.0.0.1:8000")
time.sleep(2)

# Click Transform Button
transform_btn = driver.find_element(By.ID, "transformBtn")
transform_btn.click()

print("Transform button clicked")
time.sleep(3)

# Validate QR Code Display
qr = driver.find_element(By.ID, "upiQR")
assert qr.is_displayed()
print("UPI QR displayed successfully")

# Close Browser
driver.quit()