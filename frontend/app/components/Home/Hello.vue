<script setup>
defineProps({
  user: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <section>
    <div class="flex flex-col mb-5">
      <h2 class="font-bold text-lg tracking-tight text-slate-900 ml-5">Olá, {{ user.name }}!</h2>
      <span class="text-sm text-slate-500 ml-5">O que vamos estalar hoje?</span>
    </div>
  </section>
</template>
