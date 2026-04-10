<script setup>
// Importamos o hook useRoute para acessar informações da rota atual de forma reativa
import { useRoute } from 'vue-router'

const route = useRoute()

// Definimos a lista de itens da navegação
// Note que removemos a propriedade 'active' fixa, pois agora será dinâmica
const navItems = [
  { id: 1, icon: 'home',                  label: 'Início',  to: '/inicio' },
  { id: 2, icon: 'search',                label: 'Busca',   to: '/busca' },
  { id: 3, icon: 'local_fire_department', label: 'Estalos', to: '/estalos' },
  { id: 4, icon: 'receipt_long',           label: 'Pedidos', to: '/pedidos' },
  { id: 5, icon: 'person',                label: 'Perfil',  to: '/perfil' },
]

/**
 * Função para verificar se o item de menu deve ser exibido como ativo.
 * Comparamos o caminho atual do navegador (route.path) com o destino do item (to).
 */
const isActive = (path) => {
  // Verifica se o caminho atual é exatamente igual ao destino do item
  return route.path === path
}
</script>

<template>
  <!-- Barra de navegação inferior fixa - Estilo Mobile-First -->
  <nav class="fixed bottom-0 left-0 w-full bg-white h-20 px-4 border-t border-slate-100 shadow-[0_-4px_20px_rgba(0,0,0,0.04)] flex items-center justify-between z-50">
    
    <!-- Iteramos sobre os itens de navegação usando NuxtLink para SPA navigation -->
    <NuxtLink
      v-for="item in navItems"
      :key="item.id"
      :to="item.to"
      class="flex flex-col items-center justify-center gap-1 group active:scale-90 transition-transform px-4 py-2"
      :class="isActive(item.to) ? 'bg-indigo-50 rounded-2xl' : ''"
    >
      <!-- Ícone: Mudamos a cor e o preenchimento (FILL) se estiver ativo -->
      <span
        class="material-symbols-outlined text-[28px]"
        :class="isActive(item.to) ? 'text-primary' : 'text-slate-400 group-hover:text-primary transition-colors'"
        :style="isActive(item.to) ? `font-variation-settings: 'FILL' 1` : ''"
      >
        {{ item.icon }}
      </span>

      <!-- Label: Alteramos o peso da fonte e a cor se estiver ativo -->
      <span
        class="text-[10px] uppercase tracking-wider"
        :class="isActive(item.to) ? 'font-extrabold text-primary' : 'font-bold text-slate-500'"
      >
        {{ item.label }}
      </span>
    </NuxtLink>
  </nav>
</template>