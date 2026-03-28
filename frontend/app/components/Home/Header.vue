<template>
  <header class="fixed top-0 left-0 w-full z-50 bg-glass border-b border-slate-100/50 h-16 flex items-center justify-between px-5">
    <div class="flex items-center gap-2 active:scale-95 transition-transform cursor-pointer">
      <div class="bg-primary/10 p-1.5 rounded-full">
        <span class="material-symbols-outlined text-primary text-[20px]" style="font-variation-settings: 'FILL' 1;">location_on</span>
      </div>
      <div class="flex flex-col">
        <div class="flex items-center gap-1">
          <span class="text-[13px] font-bold text-slate-900">Rua das Flores, 123</span>
          <span class="material-symbols-outlined text-primary text-[16px]">expand_more</span>
        </div>
        <span class="text-[10px] text-slate-500 font-medium">Entregar agora</span>
      </div>
    </div>

    <button class="relative w-10 h-10 flex items-center justify-center rounded-full bg-white border border-slate-100 shadow-sm active:scale-90 transition-transform">
      <span class="material-symbols-outlined text-slate-600">notifications</span>
      <span class="absolute top-2.5 right-2.5 w-2 h-2 bg-red-500 border-2 border-white rounded-full"></span>
    </button>
  </header>
</template>
