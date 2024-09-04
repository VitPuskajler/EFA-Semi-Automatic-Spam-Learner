import time
import subprocess
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import customtkinter as ctk

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")  # Choose between "light" and "dark"
ctk.set_default_color_theme("blue")  # Choose a color theme

# Create the main window
win = ctk.CTk()
win.title("EFA Assistant")

# Keep the window always on top
win.attributes('-topmost', True)

window_width = 300
window_height = 200
screen_width = 1920
screen_height = 1080
x = screen_width - window_width
y = 30
win.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Configure grid for centering
win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=1)
win.grid_rowconfigure(2, weight=1)
win.grid_rowconfigure(3, weight=1)
win.grid_columnconfigure(0, weight=1)

# Open BAT file - connect to VPN
def connect_to_vpn(path="place_path_to_vpn_batch_file"):
    subprocess.run([path])

# Function to perform Selenium operations for learning all as spam
def learn_as_spam_task():
    for x in range(1, 51):
        try:
            driver.switch_to.window(driver.window_handles[x])
            set_as_spam(driver)
        except Exception as e:
            print("Sorry, you are out of range")
            break
        time.sleep(0.3)
    driver.switch_to.window(driver.window_handles[0])

# Button command to learn all emails as spam with multithreading
def learn_as_spam():
    thread = threading.Thread(target=learn_as_spam_task)
    thread.start()

# Function to perform Selenium operations for closing all tabs
def finish_it_task():
    for x in range(51, 0, -1):
        try:
            driver.switch_to.window(driver.window_handles[x])
            driver.close()
        except Exception as e:
            print("Sorry, you are out of range")

# Button command to close all tabs with multithreading
def finish_it():
    thread = threading.Thread(target=finish_it_task)
    thread.start()

# Selenium WebDriver setup
def open_efa_task():
    global chrome_options, driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'none'

    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-search-engine-choice-screen")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    driver.get(url)
    driver.maximize_window()

    advanced = driver.find_element(By.XPATH, value='//*[@id="details-button"]')
    advanced.click()
    time.sleep(0.5)
    proceed = driver.find_element(By.XPATH, value='//*[@id="proceed-link"]')
    proceed.click()
    time.sleep(1.5)

    username = driver.find_element(By.XPATH, value='//*[@id="myusername"]')
    username.send_keys("username")

    password = driver.find_element(By.XPATH, value='//*[@id="mypassword"]')
    password.send_keys("password")

    login_button = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/fieldset/p[5]/button')
    login_button.click()

    time.sleep(2)
    search_and_reports = driver.find_element(By.XPATH, '//*[@id="menu"]/li[4]/a')
    search_and_reports.click()

    message_listing = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr[10]/td/ul/li[1]/a')
    message_listing.click()

# Button command to load EFA with multithreading
def open_efa():
    thread = threading.Thread(target=open_efa_task)
    thread.start()

# Set email as spam
def set_as_spam(driver, xpath='/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[3]/td[3]/input'):
    spam_checkbox = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[3]/td[3]/input')
    learn = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[3]/td[3]/select")
    spam_report = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[3]/td[3]/select/option[4]')
    submit_button = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td[2]/button')

    learn.click()
    spam_checkbox.click()
    spam_report.click()
    submit_button.click()

url = "url_to_efa"

# Create and place buttons
vpn_button = ctk.CTkButton(win, text="Connect To VPN", command=connect_to_vpn)
vpn_button.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

open_efa_button = ctk.CTkButton(win, text="Load EFA", command=open_efa)
open_efa_button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

spam_button = ctk.CTkButton(win, text="Learn All As Spam", command=learn_as_spam)
spam_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

kill_button = ctk.CTkButton(win, text="Close All Tabs", command=finish_it)
kill_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

# Start the Tkinter event loop
win.mainloop()