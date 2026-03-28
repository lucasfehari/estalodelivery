<script setup>
defineProps({
  stores: {
    type: Array,
    required: true,
  },
})
</script>

<template>
  <section>
    <div class="flex items-center justify-between mb-5">
      <h2 class="font-bold text-lg tracking-tight">Lojas Premium</h2>
    </div>

    <div class="flex gap-5 overflow-x-auto -mx-5 px-5 hide-scrollbar">
      <div
        v-for="store in stores"
        :key="store.id"
        class="flex flex-col items-center gap-2 flex-shrink-0 group cursor-pointer active:scale-90 transition-transform"
      >
        <div class="w-16 h-16 rounded-full p-[3px] bg-gradient-to-tr from-rose-500 via-purple-500 to-indigo-500">
          <div class="w-full h-full rounded-full border-2 border-white overflow-hidden bg-white">
            <img :src="store.image" :alt="store.name" class="w-full h-full object-cover" />
          </div>
        </div>
        <span class="text-[11px] font-bold text-slate-700 tracking-tight">{{ store.name }}</span>
      </div>
    </div>
  </section>
</template>
