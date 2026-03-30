<script setup>
const navItems = [
  { id: 1, icon: 'home',         label: 'Início',  active: true, to: '/inicio' },
  { id: 2, icon: 'search',       label: 'Busca',   active: false, to: '/busca' },
  { id: 3, icon: 'local_fire_department', label: 'Estalos', active: false, to: '/estalos' },
  { id: 4, icon: 'receipt_long', label: 'Pedidos', active: false, to: '/pedidos' },
  { id: 5, icon: 'person',       label: 'Perfil',  active: false, to: '/perfil' },
]
</script>

<template>
  <nav class="fixed bottom-0 left-0 w-full bg-white h-20 px-4 border-t border-slate-100 shadow-[0_-4px_20px_rgba(0,0,0,0.04)] flex items-center justify-between z-50">
    <NuxtLink
      v-for="item in navItems"
      :key="item.id"
      :to="item.to"
      class="flex flex-col items-center justify-center gap-1 group active:scale-90 transition-transform px-4 py-2"
      :class="item.active ? 'bg-indigo-50 rounded-2xl' : ''"
    >
      <span
        class="material-symbols-outlined text-[28px]"
        :class="item.active ? 'text-primary' : 'text-slate-400 group-hover:text-primary transition-colors'"
        :style="item.active ? `font-variation-settings: 'FILL' 1` : ''"
      >
        {{ item.icon }}
      </span>
      <span
        class="text-[10px] uppercase tracking-wider"
        :class="item.active ? 'font-extrabold text-primary' : 'font-bold text-slate-500'"
      >
        {{ item.label }}
      </span>
    </NuxtLink>
  </nav>
</template>