<script setup>
defineProps({
  banners: {
    type: Array,
    required: true,
  },
})
</script>

<template>
  <section class="-mx-5">
    <div class="flex gap-4 overflow-x-auto px-5 hide-scrollbar">
      <div
        v-for="banner in banners"
        :key="banner.id"
        :class="`flex-shrink-0 w-[300px] h-[140px] ${banner.bgClass} rounded-2xl relative overflow-hidden flex items-center p-6 active:scale-95 transition-transform cursor-pointer shadow-lg`"
      >
        <!-- Text Content -->
        <div class="z-10 flex flex-col gap-1 max-w-[160px]">
          <span class="bg-white/20 w-fit px-2 py-0.5 rounded-full text-[10px] font-bold text-white uppercase tracking-wider">
            {{ banner.tag }}
          </span>
          <!-- eslint-disable-next-line vue/no-v-html -->
          <h3 class="text-white font-extrabold text-2xl leading-tight" v-html="banner.title" />
          <p class="text-white/80 text-xs font-medium">{{ banner.subtitle }}</p>
        </div>

        <!-- Banner decoration: image -->
        <img
          v-if="banner.type === 'image'"
          :src="banner.image"
          alt="Banner"
          class="absolute -right-4 -bottom-4 w-40 h-40 object-cover rotate-12 drop-shadow-2xl"
        />
        <!-- Banner decoration: icon -->
        <div
          v-else-if="banner.type === 'icon'"
          class="absolute -right-6 -bottom-6 w-44 h-44 bg-white/10 rounded-full flex items-center justify-center"
        >
          <span class="material-symbols-outlined text-white text-[80px] opacity-40">{{ banner.icon }}</span>
        </div>
      </div>
    </div>
  </section>
</template>
