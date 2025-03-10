# EFA Assistant

EFA Assistant is a semi-automated tool designed to streamline the tedious task of marking spam emails in the EFA system. Built with Python, Selenium, and CustomTkinter, this utility saves time by automating repetitive steps, making it an ideal companion for users handling large volumes of spam.

## Features

- **VPN Integration:** Easily connect to your VPN with a single click.
- **Automated EFA Navigation:** Automatically log in and navigate through the EFA interface.
- **Spam Marking:** Mark multiple emails as spam simultaneously using Selenium.
- **Tab Management:** Open up to 50 tabs for processing and close them efficiently.
- **Responsive UI:** Leverages multi-threading to ensure the GUI remains responsive during operations.

## Prerequisites

- <b> Python 3.x </b>
- [Selenium](https://selenium-python.readthedocs.io/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/) (compatible with your installed version of Google Chrome)

## Setup

1. **VPN Batch File:**  
   Update the path in the `connect_to_vpn()` function to point to your VPN batch file (skip if not required).

2. **Credentials:**  
   In the `open_efa_task()` function, replace the placeholder username and password with your EFA credentials. For enhanced security, consider using environment variables.

3. **EFA URL:**  
   Set the correct URL or IP address for your EFA in the `url` variable.
