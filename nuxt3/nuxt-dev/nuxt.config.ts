// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    runtimeConfig: {
        // The private keys which are only available within server-side
        privateKeyExample: '',
        // Keys within public, will be also exposed to the client-side
        public: {
            publicKeyExample: '',
        }
    },
    modules: [
        '@nuxt/image-edge',
        "@nuxtjs/tailwindcss",
        '@vueuse/nuxt',
        '@nuxtjs/i18n',
        '@pinia/nuxt',
    ],
    i18n: {
        vueI18n: {
            legacy: false,
            locale: 'en',
            messages: {
            en: {
                welcome: 'Welcome'
            },
            fr: {
                welcome: 'Bienvenue'
            }
            }
        }
    },
    pinia: {
        autoImports: [
          'defineStore', // import { defineStore } from 'pinia'
        ],
    },
})
