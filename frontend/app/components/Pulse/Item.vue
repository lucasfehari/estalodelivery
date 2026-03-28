<script setup>
defineProps({
  item: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <section class="h-full w-full snap-start relative flex flex-col justify-end">
    <!-- Image Background -->
    <img
      :src="item.image"
      :alt="item.title"
      class="absolute inset-0 w-full h-full object-cover"
    />

    <!-- Bottom Gradient Overlay -->
    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none"></div>

    <!-- Content Overlay -->
    <div class="relative z-10 px-6 pb-32 flex justify-between items-end w-full">
      <!-- Merchant & Info -->
      <div class="flex-1 max-w-[70%] space-y-3">
        <div class="flex items-center gap-2">
          <div :class="['w-10 h-10 rounded-full border-2 overflow-hidden', item.merchantBorderClass]">
            <img :src="item.merchantLogo" class="w-full h-full object-cover" :alt="item.merchantName" />
          </div>
          <span class="text-white font-headline font-bold text-sm tracking-tight">{{ item.merchantName }}</span>
        </div>
        <div>
          <h2 class="text-white font-headline font-extrabold text-2xl tracking-tighter leading-tight">{{ item.title }}</h2>
          <p class="text-white/70 text-sm font-medium mt-1">{{ item.description }}</p>
        </div>
        <div class="text-secondary-fixed-dim font-headline font-extrabold text-3xl">{{ item.price }}</div>
      </div>

      <!-- Vertical Sidebar -->
      <div class="flex flex-col items-center gap-6 mb-4">
        <div class="flex flex-col items-center gap-1 group">
          <div class="w-12 h-12 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center hover:bg-white/20 transition-all active:scale-90">
            <span class="material-symbols-outlined text-white" style="font-variation-settings: 'FILL' 1;">favorite</span>
          </div>
          <span class="text-white text-[10px] font-bold">{{ item.likesCount }}</span>
        </div>
        <div class="flex flex-col items-center gap-1 group">
          <div class="w-12 h-12 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center hover:bg-white/20 transition-all active:scale-90">
            <span class="material-symbols-outlined text-white">share</span>
          </div>
          <span class="text-white text-[10px] font-bold">Share</span>
        </div>
        <button class="w-14 h-14 rounded-full bg-primary flex items-center justify-center shadow-lg shadow-primary/40 active:scale-95 transition-transform">
          <span class="material-symbols-outlined text-white text-3xl">shopping_basket</span>
        </button>
      </div>
    </div>
  </section>
</template>
