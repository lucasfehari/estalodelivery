<script setup lang="ts">
/**
 * ARQUIVO: cadastro.vue
 * PROJETO: Estalo (Quick Commerce)
 * DESCRIÇÃO: Tela de Criação de Conta utilizando componentes reutilizáveis (UiAppInput e UiAppButton).
 *            Construída com Vue 3 (Composition API) e Nuxt 3.
 */

import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

// Remove o layout principal padrão (navbars visíveis para usuários logados)
// a fim de exibir apenas o fluxo limpo de cadastro.
definePageMeta({
  layout: false,
})

const router = useRouter()

// Injeção dinâmica dos assets (tipografia/fonts) para garantir estilização 
useHead({
  link: [
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap'
    },
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap'
    }
  ],
  style: [
    {
      // Correção aplicada: uso de innerHTML ao invés de children conforme documentação do Nuxt (Unhead)
      innerHTML: `
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
      `
    }
  ]
})

// === ESTADO DO FORMULÁRIO (Reatividade) ===
const form = reactive({
  nome: '',
  celular: '',
  email: '',
  senha: '',
})

// === ESTADOS DE UI ===
const carregando = ref(false)

/**
 * Função responsável por submeter os dados para o back-end (FastAPI).
 * Por enquanto, simula um fake delay de requisição.
 */
async function handleCadastro() {
  if (!form.nome || !form.celular || !form.email || !form.senha) return

  carregando.value = true

  try {
    // TODO: Disparar fluxo de comunicação de API para salvar no banco (PostgreSQL) usando Pydantic/FastAPI
    // $fetch('/api/auth/register', { method: 'POST', body: form })
    await new Promise(resolve => setTimeout(resolve, 1500))

    // Após cadastro, redirecionar de forma fluida UX
    await router.push('/')
  } catch (error) {
    console.error("Erro durante criação de conta", error)
    // Aqui poderiamos acoplar um toaster alert
  } finally {
    carregando.value = false
  }
}

// Navegação rápida UX para voltar (back action)
function goBack() {
  router.back()
}
</script>

<template>
  <div class="bg-surface text-on-surface antialiased font-body min-h-[max(884px,100dvh)]">
    
    <!-- Top Navigation Shell (Voltar para Home ou Login) -->
    <nav class="fixed top-0 w-full z-50 bg-[#f6f6ff]/80 backdrop-blur-xl shadow-[0_40px_40px_-15px_rgba(39,46,66,0.04)]">
      <div class="flex items-center h-16 px-6 w-full max-w-screen-xl mx-auto">
        <button 
          @click="goBack"
          class="active:scale-95 transition-transform duration-200 hover:opacity-80 transition-opacity"
        >
          <span class="material-symbols-outlined text-[#6366f1] text-2xl" style="font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;">arrow_back</span>
        </button>
      </div>
    </nav>

    <!-- Estrutura Principal de Layout Flex Centralizada -->
    <main class="min-h-screen max-w-md mx-auto relative flex flex-col justify-center px-6 pt-20 pb-12 overflow-hidden">
      
      <!-- Elemento Decorativo Background Blur Animado -->
      <div class="absolute top-0 right-0 -z-10 w-64 h-64 bg-primary-container/10 rounded-full blur-[100px] pointer-events-none"></div>

      <!-- Cabecalho da Tela de Cadastro -->
      <header class="mt-8 mb-10 z-10">
        <h1 class="font-headline font-extrabold tracking-tighter text-[1.5rem] leading-tight text-on-surface">
          Criar conta
        </h1>
        <p class="text-on-surface-variant font-medium mt-3 mb-5 text-lg leading-relaxed">
          Preencha rápido para pedir o seu primeiro estalo.
        </p>
      </header>

      <!-- Formulário Componentizado (Ui Components App) -->
      <form class="space-y-5 z-10" @submit.prevent="handleCadastro">
        
        <UiAppInput 
          v-model="form.nome"
          label="Nome Completo"
          placeholder="Como o motoboy vai te chamar?"
          type="text"
          required
        />

        <UiAppInput 
          v-model="form.celular"
          label="Celular"
          placeholder="(00) 00000-0000"
          type="tel"
          required
        />

        <UiAppInput 
          v-model="form.email"
          label="E-mail"
          placeholder="seu@email.com"
          type="email"
          required
        />

        <!-- Componente inteligente 'UiAppInput' cuida da exibição/ocultação ("Olhinho") internamente -->
        <UiAppInput 
          v-model="form.senha"
          label="Senha"
          placeholder="Crie uma senha forte"
          type="password"
          required
        />

        <!-- Novo componente modularizado UiAppButton (carrega loader state nativo interno) -->
        <UiAppButton 
          type="submit" 
          :loading="carregando"
          label="Começar a usar"
          icon="arrow_forward"
        />

      </form>

      <!-- Rodapé Institucional com Navigation -->
      <footer class="mt-12 text-center z-10">
        <p class="text-on-surface-variant font-medium">
          Já tem uma conta? 
          <NuxtLink to="/login" class="text-on-surface font-extrabold hover:opacity-70 transition-opacity ml-1">
            Entrar
          </NuxtLink>
        </p>

        <!-- Terms of Service Box -->
        <div class="mt-10 p-5 bg-surface-container-low/50 rounded-lg">
          <p class="text-[11px] leading-relaxed text-on-surface-variant/70 text-center uppercase tracking-tighter">
            Ao criar sua conta, você concorda com nossos <br/>
            <span class="text-primary font-bold">Termos de Uso</span> e <span class="text-primary font-bold">Privacidade</span>.
          </p>
        </div>
      </footer>

      <!-- Floating Element for Depth -->
      <div class="fixed -bottom-10 -left-10 w-40 h-40 bg-secondary/5 rounded-full blur-[60px] pointer-events-none"></div>
    </main>

  </div>
</template>

<style scoped>
/* Scoped styles específicos da página (família de tipografias e resets se necessários já injetados) */
.font-headline { 
  font-family: 'Plus Jakarta Sans', sans-serif; 
}
.font-body { 
  font-family: 'Inter', sans-serif; 
}
</style>
