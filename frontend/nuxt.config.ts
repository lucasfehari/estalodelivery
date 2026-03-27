// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  // Módulos do Nuxt: Tailwind CSS integrado nativamente
  modules: ['@nuxtjs/tailwindcss'],

  // CSS global aplicado em todas as páginas (contém as diretivas @tailwind)
  css: ['~/assets/css/main.css'],
})