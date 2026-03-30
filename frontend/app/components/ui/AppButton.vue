<script setup lang="ts">
/**
 * COMPONENTE: AppButton
 * DESCRIÇÃO: Botão reutilizável com estados de loading e desativado.
 */
interface Props {
  type?: 'button' | 'submit' | 'reset'
  loading?: boolean
  disabled?: boolean
  label?: string
  icon?: string // Nome do ícone do Material Symbols
  class?: string
}

withDefaults(defineProps<Props>(), {
  type: 'button',
  loading: false,
  disabled: false,
})
</script>

<template>
  <button
    :type="type"
    :disabled="disabled || loading"
    class="w-full h-16 mt-10 rounded-full bg-on-primary-fixed text-surface-bright font-bold text-xl transition-all duration-200 shadow-xl shadow-on-primary-fixed/10 flex items-center justify-center gap-3 disabled:opacity-70 disabled:cursor-not-allowed"
    :class="{
      'active:scale-95 hover:opacity-90': !disabled && !loading,
    }"
  >
    <!-- Estado de Carregamento -->
    <template v-if="loading">
      <svg class="animate-spin h-6 w-6 text-current" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 00 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
      <span>Aguarde...</span>
    </template>

    <!-- Slot Padrão (Conteúdo Flexível) -->
    <template v-else>
      <slot>
        <span>{{ label }}</span>
        <span v-if="icon" class="material-symbols-outlined text-xl" style="font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;">
          {{ icon }}
        </span>
      </slot>
    </template>
  </button>
</template>
