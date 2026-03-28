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
    <div class="flex items-center justify-between mb-5">
      <h2 class="font-bold text-lg tracking-tight text-slate-900 ml-5">Olá, {{ user.name }}!</h2>
    </div>
  </section>
</template>
