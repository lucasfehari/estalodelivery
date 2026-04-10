<script setup lang="ts">

</script>

<template>
  <section>
    <div class="relative group">
      <div class="absolute inset-y-0 left-4 flex items-center pointer-events-none">
        <span class="material-symbols-outlined text-slate-400 group-focus-within:text-primary transition-colors">search</span>
      </div>
      <input
        class="w-full h-12 pl-12 pr-5 bg-white border border-slate-100 rounded-full text-sm font-medium placeholder:text-gray-500 focus:ring-4 focus:ring-primary/10 focus:border-primary transition-all shadow-sm"
        placeholder="Item ou loja..."
        type="text"
      />
    </div>
  </section>
</template>
