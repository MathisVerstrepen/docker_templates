# Docker templates

This repository contains multiple Docker environments to facilitate the development and deployment of various applications. The environments currently included are:

| Environment | Description | Image Size |
| --- | --- | --- |
| [PostgreSQL 15](https://github.com/MathisVerstrepen/docker_templates/tree/master/postgres-15) | Docker compose setup with a configuration file, data persistence, and an initialization script for a PostgreSQL database. | / |
| [Selenium Chrome Python](https://github.com/MathisVerstrepen/docker_templates/tree/master/selenium/chromedriver-full) | Provide a full ready-to-use environment for running Selenium programs with Chrome in Python. | 1.67GB |
| [Selenium Chrome Python - Minimal](https://github.com/MathisVerstrepen/docker_templates/tree/master/selenium/chromedriver-minimal) | Provide a minimal and lightweight environment for running Selenium programs with Chrome in Python. | 497MB |
| [Selenium Firefox & Geckodriver Python](https://github.com/MathisVerstrepen/docker_templates/tree/master/selenium/firefoxdriver-full) | Provide a full ready-to-use environment for running Selenium programs with Firefox & Geckodriver in Python. | 1.45GB |
| [Nuxt 3 dev starter](https://github.com/MathisVerstrepen/docker_templates/tree/master/nuxt3/nuxt-dev) | Provide a development environment equipped with everything you need to build a web application based on Nuxt 3. | 276MB |

Each environment is provided as a separate Docker image or/and compose file, making it easy to select and use the environment that fits your needs.

## Getting Started

To use any of the environments provided in this repository, you will need to have Docker installed on your machine. Once Docker is installed, you can build and run any of the images contained in this repository by following the instructions provided in the corresponding subdirectories.

## Contributing
If you would like to contribute to this repository, please feel free to open a pull request or an issue. We welcome contributions of any kind, whether it's a bug fix, a new feature, or a typo correction.

## License
This repository is licensed under the MIT License. Feel free to use it however you like.