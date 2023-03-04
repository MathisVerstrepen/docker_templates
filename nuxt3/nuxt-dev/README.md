# Nuxt 3 dev environment starter

This docker image is designed to provide you with a development environment equipped with everything you need to build a web application based on Nuxt 3.

It includes the initial files needed to start development as well as modules to increase productivity and ease development such as Tailwind CSS and VueUse.


## Included Dependencies

| Dependency | Description | Documentation |
| --- | --- | --- |
| Nuxt Image | Plug-and-play image optimization, resize and transform your images using built-in optimizer or your favorite images CDN. | [Global Doc](https://v1.image.nuxtjs.org/get-started) |
| Tailwind CSS | Utility-first CSS framework with predefined classes that you can use to build and design web pages directly in your markup. | [Nuxt Specific](https://tailwindcss.nuxtjs.org/getting-started/setup) / [Global Doc](https://tailwindcss.com/docs/installation) |
| VueUse | Collection of utility functions based on Composition API. | [Global Doc](https://vueuse.org/guide/) |
| i18n | Internationalization framework, provide lightweight simple translation management. | [Nuxt Specific](https://v8.i18n.nuxtjs.org/getting-started/basic-usage) |
| Pinia | Store library for Vue, it allows you to share a state across components/pages. | [Global Doc](https://pinia.vuejs.org/introduction.html) |


## Installation

Create a new directory and copy the contents from git:

```bash
mkdir nuxt-dev && cd nuxt-dev
git init
git remote add -f origin git@github.com:MathisVerstrepen/docker_templates.git
git config core.sparseCheckout true
git sparse-checkout init
git sparse-checkout set nuxt3/nuxt-dev
git pull origin master
cd nuxt3/nuxt-dev
```

Build the Docker image using the following command:
```bash
 sudo docker compose build --no-cache
```

Run the Docker compose using the following command:
```bash
sudo docker compose up -d
```
