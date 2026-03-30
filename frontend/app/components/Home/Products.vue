<script setup>
defineProps({
  products: {
    type: Array,
    required: true,
  },
})


const {asyncData, data: products, pending, error} = await useFetch("http://localhost:8000/produtos")

</script>

<template>
  <section>
    <div class="flex items-center justify-between mb-4">
      <h2 class="font-bold text-lg tracking-tight">Rápidos e com Desconto</h2>
      <a class="text-primary font-bold text-xs uppercase tracking-widest" href="#">Ver mais</a>
    </div>

    <div class="flex gap-4 overflow-x-auto -mx-5 px-5 hide-scrollbar">
      <div
        v-for="product in products"
        :key="product.id_produto"
        class="flex-shrink-0 w-44 bg-white border border-slate-100 rounded-2xl p-2 shadow-soft active:scale-95 transition-transform"
      >
        <div class="relative mb-3">
          <img :src="product.capa" :alt="product.nome" class="w-full aspect-square object-cover rounded-xl" />
          <div class="absolute bottom-2 left-2 bg-white/95 backdrop-blur px-2 py-1 rounded-lg flex items-center gap-1 shadow-sm">
            <span class="material-symbols-outlined text-orange-500 text-[12px]" style="font-variation-settings: 'FILL' 1;">timer</span>
            <span class="text-[10px] font-bold text-slate-700 uppercase">{{ product.tempo_entrega }}</span>
          </div>
        </div>
        <div class="px-1 pb-1">
          <h4 class="font-bold text-sm text-slate-800 line-clamp-1 mb-1 leading-none">{{ product.nome }}</h4>
          <div class="flex items-center gap-2 mb-1">
            <span class="text-green-600 font-extrabold text-base">R$ {{ product.preco }}</span>
            <span class="text-slate-400 text-[10px] line-through">R$ {{ product.preco_promocao }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
