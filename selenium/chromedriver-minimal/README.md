# Selenium ChromeDriver Minimal

This Docker image is designed to provide a minimal and lightweight environment for running your application. By using this Docker image, you can significantly reduce the size of your Docker images, resulting in faster and more efficient deployments.

This image is based on Alpine Linux, which is known for its small size and efficiency. It includes only the necessary dependencies and libraries required to run your application, without any unnecessary overhead.

By using this Docker image, you can avoid the need to install and configure these tools on your local machine, which can save time and ensure consistency across different environments.


## Installation

Create a new directory and copy the contents from git:

```bash
mkdir chromedriver-minimal && cd chromedriver-minimal
git init
git remote add -f origin git@github.com:MathisVerstrepen/docker_templates.git
git config core.sparseCheckout true
git sparse-checkout init
git sparse-checkout set selenium/chromedriver-minimal
git pull origin master
cd selenium/chromedriver-minimal
```

Build the Docker image using the following command:
```bash
sudo docker build -t selenium_chrome_min:latest -f .dockerfile .
```

Run the Docker container using the following command:
```bash
sudo docker run selenium_chrome_min
```