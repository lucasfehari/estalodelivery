<script setup lang="ts">
/**
 * ARQUIVO: esqueci-senha.vue
 * PROJETO: Estalo (Quick Commerce)
 * DESCRIÇÃO: Tela de Recuperação de Senha utilizando componentes modulares (UiAppInput e UiAppButton).
 *            Focada em UX simplificada e feedbacks visuais claros.
 */

import { ref } from 'vue'
import { useRouter } from 'vue-router'

definePageMeta({
  layout: false,
})

const router = useRouter()
const email = ref('')
const carregando = ref(false)
const enviado = ref(false)

// Configuração de Head para fontes e Material Symbols
useHead({
  link: [
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800&family=Inter:wght@400;500;600&display=swap'
    },
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap'
    }
  ],
  style: [
    {
      innerHTML: `
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
      `
    }
  ]
})

/**
 * Simula o disparo do e-mail de recuperação para o FastAPI.
 */
async function handleRecuperar() {
  if (!email.value) return

  carregando.value = true
  
  try {
    // Simulando chamada de API ($fetch('/api/auth/forgot-password'))
    await new Promise(resolve => setTimeout(resolve, 2000))
    enviado.value = true
  } catch (error) {
    console.error("Erro ao enviar recuperação", error)
  } finally {
    carregando.value = false
  }
}

function goBack() {
  router.back()
}
</script>

<template>
  <div class="bg-surface text-on-surface antialiased font-body min-h-[max(884px,100dvh)]">
    
    <!-- Top Navigation -->
    <header class="fixed top-0 w-full z-50 bg-[#f6f6ff]/80 backdrop-blur-lg flex items-center h-16 px-6">
      <button 
        @click="goBack"
        class="flex items-center justify-center p-2 text-primary active:scale-95 duration-200 transition-opacity hover:opacity-70"
      >
        <span class="material-symbols-outlined">arrow_back</span>
      </button>
    </header>

    <main class="min-h-screen max-w-md mx-auto relative flex flex-col justify-center px-8 pt-16 pb-24 overflow-hidden">
      
      <!-- Glow Decorativo -->
      <div class="absolute top-1/4 left-1/2 -translate-x-1/2 -z-10 w-64 h-64 bg-primary/5 rounded-full blur-[100px] pointer-events-none"></div>

      <!-- Seção de Cabeçalho / Ilustração -->
      <section class="mb-10 flex flex-col items-start z-10">
        <div class="bg-primary-container/20 p-5 rounded-xl mb-8 flex items-center justify-center">
          <div class="bg-primary-container p-4 rounded-full flex items-center justify-center shadow-sm">
            <span class="material-symbols-outlined text-on-primary-container text-3xl">key</span>
          </div>
        </div>

        <h1 class="text-[2.25rem] font-extrabold text-on-surface leading-tight tracking-tight mb-3 font-headline">
          Esqueceu a senha?
        </h1>
        
        <p class="text-on-surface-variant text-[1rem] leading-relaxed max-w-[90%] font-medium">
          Acontece nas melhores fomes. Digite seu e-mail abaixo e enviaremos um link de recuperação num estalo.
        </p>
      </section>

      <!-- Fluxo do Formulário -->
      <section v-if="!enviado" class="space-y-6 z-10 transition-all duration-500">
        <form @submit.prevent="handleRecuperar">
          <UiAppInput 
            v-model="email"
            placeholder="Seu e-mail cadastrado"
            type="email"
            icon="alternate_email"
            required
          />

          <!-- Botão Principal com as cores dark do design esqueceu-senha -->
          <UiAppButton 
            type="submit"
            :loading="carregando"
            label="Enviar link de recuperação"
            icon="send"
            class="!bg-on-background" 
          />
        </form>
      </section>

      <!-- Estado de Sucesso (Feedback Visual) -->
      <section v-else class="z-10 p-6 bg-primary-container/10 border border-primary/20 rounded-2xl animate-fade-in">
        <div class="flex items-center gap-4">
          <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center">
            <span class="material-symbols-outlined text-white">check</span>
          </div>
          <div>
            <p class="font-bold text-on-surface">E-mail enviado!</p>
            <p class="text-sm text-on-surface-variant">Confira sua caixa de entrada para redefinir sua senha.</p>
          </div>
        </div>
        <button @click="enviado = false" class="mt-4 text-sm font-bold text-primary hover:underline">
          Tentar outro e-mail
        </button>
      </section>

      <!-- Quick Help Card (Bento-style) -->
      <div class="mt-12 p-6 bg-surface-container-lowest rounded-xl flex items-center gap-4 z-10 shadow-sm border border-outline-variant/10">
        <div class="w-12 h-12 rounded-full bg-secondary-container/30 flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-secondary">contact_support</span>
        </div>
        <div>
          <p class="text-sm font-bold text-on-surface uppercase tracking-tight">Precisa de ajuda real?</p>
          <p class="text-xs text-on-surface-variant font-medium">Fale com nosso suporte 24h via chat.</p>
        </div>
      </div>

      <!-- Footer Com Link -->
      <footer class="mt-10 text-center z-10">
        <p class="text-on-surface-variant font-medium">
          Lembrou a senha? 
          <NuxtLink to="/login" class="text-primary-dim font-extrabold ml-1 hover:underline transition-all">
            Voltar para o Login
          </NuxtLink>
        </p>
      </footer>

  
    </main>

  </div>
</template>

<style scoped>
.font-headline { font-family: 'Plus Jakarta Sans', sans-serif; }
.font-body { font-family: 'Inter', sans-serif; }

.animate-fade-in {
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
