<script setup>
defineProps({
  categories: {
    type: Array,
    required: true,
  },
})
</script>

<template>
  <section class="grid grid-cols-4 gap-3">
    <div
      v-for="category in categories"
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
