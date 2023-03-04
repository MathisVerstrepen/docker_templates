# Selenium Firefox & Geckodriver Full

This Docker image is designed to provide a ready-to-use environment for running Selenium programs with Firefox and Geckodriver in Python. It includes Firefox, the Geckodriver executable, and an initial Python program.

By using this Docker image, you can avoid the need to install and configure these tools on your local machine, which can save time and ensure consistency across different environments.


## Installation

Create a new directory and copy the contents from git:

```bash
mkdir firefoxdriver-full && cd firefoxdriver-full
git init
git remote add -f origin git@github.com:MathisVerstrepen/docker_templates.git
git config core.sparseCheckout true
git sparse-checkout init
git sparse-checkout set selenium/firefoxdriver-full
git pull origin master
cd selenium/firefoxdriver-full
```

Build the Docker image using the following command:
```bash
sudo docker build -t selenium_chrome_full:latest -f .dockerfile .
```

Run the Docker container using the following command:
```bash
sudo docker run selenium_chrome_full
```