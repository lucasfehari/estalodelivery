<script setup>
/**
 * Para a página de busca, selecionamos apenas as categorias mais populares.
 * Isso ajuda a manter a interface limpa e focar no que o usuário mais procura.
 */
const categories = [
  { id: 1, emoji: '🍔', label: 'Lanches' },
  { id: 2, emoji: '🛒', label: 'Mercado' },
  { id: 3, emoji: '💊', label: 'Farmácia' },
  { id: 4, emoji: '⚡', label: 'Express' },
]
</script>

<template>
    <div class="p-12 flex flex-col">
<HomeSearch/>
<div class="flex flex-col gap-4">
    <p class="headline pt-4">Buscas Recentes</p>
    <div class="flex flex-col gap-4">
        <div class="flex items-center gap-2">
            <span class="material-symbols-outlined text-slate-400">search</span>
            <p>Busca</p>
            <span class="ml-auto material-symbols-outlined text-slate-400">close</span>
        </div>
        <div class="flex items-center gap-2">
            <span class="material-symbols-outlined text-slate-400">search</span>
            <p>Suchi</p>
            <span class="ml-auto material-symbols-outlined text-slate-400">close</span>
        </div>
        <div class="flex items-center gap-2">
            <span class="material-symbols-outlined text-slate-400">search</span>
            <p>Busca</p>
            <span class="ml-auto material-symbols-outlined text-slate-400">close</span>
        </div>
    </div>
</div>

 <p class="headline pt-12">Populares</p>
  <HomeCategories class="pt-4" :categories="categories"/>
    </div>

   

 <!-- Bottom Navigation -->
  <LayoutNavbar/>
</template>

<style>

</style>