<script setup>
// Definimos as propriedades do componente. 
// Tornamos 'categories' opcional e usamos as categorias padrão caso nada seja passado.
const props = defineProps({
  categories: {
    type: Array,
    default: () => [
      { id: 1, emoji: '🍔', label: 'Lanches' },
      { id: 2, emoji: '🛒', label: 'Mercado' },
      { id: 3, emoji: '💊', label: 'Farmácia' },
      { id: 4, emoji: '🎧', label: 'Eletrônicos' },
      { id: 5, emoji: '🥤', label: 'Bebidas' },
      { id: 6, emoji: '🐾', label: 'Pet' },
      { id: 7, emoji: '🧁', label: 'Doces' },
      { id: 8, emoji: '⚡', label: 'Express' },
    ]
  },
})
</script>

<template>
  <section class="grid grid-cols-4 gap-3">
    <div
      v-for="category in props.categories"
      :key="category.id"
      class="flex flex-col items-center gap-2 group cursor-pointer active:scale-90 transition-transform"
    >
      <div class="w-full aspect-square bg-white border border-slate-50 rounded-2xl flex items-center justify-center shadow-soft group-hover:bg-blue-50 transition-colors">
        <span class="text-2xl">{{ category.emoji }}</span>
      </div>
      <span class="text-[10px] font-bold text-slate-600 uppercase tracking-tight">{{ category.label }}</span>
    </div>
  </section>
</template>
