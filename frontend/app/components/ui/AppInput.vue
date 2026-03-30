<script setup lang="ts">
/**
 * COMPONENTE: AppInput
 * DESCRIÇÃO: Campo de texto reutilizável para formulários. Suporta ícone de "revelar senha" se for do tipo password.
 */
import { ref, computed } from 'vue'

const props = defineProps<{
  modelValue: string | number
  label?: string
  type?: string
  placeholder?: string
  required?: boolean
  icon?: string // Ícone do Material Symbols à esquerda
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string | number]
}>()

const inputType = ref(props.type || 'text')
const isPassword = computed(() => props.type === 'password')

const togglePassword = () => {
  inputType.value = inputType.value === 'password' ? 'text' : 'password'
}
</script>

<template>
  <div class="space-y-2">
    <!-- Label Opcional -->
    <label v-if="label" class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant ml-4">
      {{ label }}
    </label>
    
    <div class="relative w-full">
      <!-- Ícone Opcional à Esquerda -->
      <div v-if="icon" class="absolute inset-y-0 left-5 flex items-center pointer-events-none">
        <span class="material-symbols-outlined text-on-surface-variant transition-colors" style="font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;">
          {{ icon }}
        </span>
      </div>

      <input
        :value="modelValue"
        @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
        :type="inputType"
        :placeholder="placeholder"
        :required="required"
        class="w-full h-16 bg-surface-container-low border-none rounded-lg text-on-surface placeholder:text-on-surface-variant/50 focus:ring-2 focus:ring-primary/20 focus:bg-surface-container-lowest transition-all duration-300 outline-none font-medium text-lg"
        :class="[
          isPassword ? 'pr-14' : 'pr-6',
          icon ? 'pl-14' : 'px-6'
        ]"
      />
      
      <!-- Olhinho para Password -->
      <button
        v-if="isPassword"
        type="button"
        @click="togglePassword"
        class="absolute right-5 top-1/2 -translate-y-1/2 text-on-surface-variant/60 hover:text-on-surface transition-colors focus:outline-none"
        tabindex="-1"
      >
        <span class="material-symbols-outlined select-none" style="font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;">
          {{ inputType === 'password' ? 'visibility' : 'visibility_off' }}
        </span>
      </button>
    </div>
  </div>
</template>
