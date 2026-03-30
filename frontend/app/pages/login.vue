<script setup lang="ts">
/**
 * ARQUIVO: login.vue
 * PROJETO: Estalo (Quick Commerce)
 * DESCRIÇÃO: Tela de Login re-desenhada seguindo a nova identidade visual.
 *            Possui as tecnologias exigidas: Vue 3 (Composition API),
 *            Tailwind CSS e Nuxt 3.
 */

import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

// Usamos definePageMeta para garantir que a tela de login preencha a página toda 
// e não herde layouts indesejados (como navbars de usuários já logados).
definePageMeta({
  layout: false,
})

const router = useRouter()

// Injeção de dependências do cabeçalho da página de forma dinâmica via Nuxt (useHead).
// Isso carrega as fontes 'Plus Jakarta Sans' e 'Inter' sem poluir o estilo global.
useHead({
  link: [
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap'
    },
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap'
    }
  ],
  style: [
    // Preenche o ícone do google e configurações de grade base do material UI
    {
      innerHTML: `
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
      `
    }
  ]
})

// === ESTADO REATIVO DO FORMULÁRIO ===
// Mantemos os campos em um objeto 'reactive' para facilidade de envio no futuro ao FastAPI.
const form = reactive({
  email: '',
  senha: '',
})

// === CONTROLES DE ESTADO VISUAL ===
const carregando = ref(false)       // Bloqueia interações em botões enquanto comunica com o back-end
const senhaVisivel = ref(false)     // Variável responsável por alternar o tipo de input da senha ("password" / "text")
const erroLogin = ref('')           // Feedback visual de falhas para o cliente

/**
 * Função responsável por lidar com o Login.
 * Realiza as validações e futuramente chamará a API no FastAPI (`/api/auth/login`).
 */
async function handleLogin() {
  erroLogin.value = '' // Limpa erros passados.

  // 1. Validação simples no front-end para economizar requisições vazias pro banco
  if (!form.email || !form.senha) {
    erroLogin.value = 'Preencha e-mail e senha para continuar.'
    return
  }

  carregando.value = true // Entra em modo loading visual (UX fluid animation)

  try {
    // 2. Simulação de processamento de API.
    // TODO: Integrar com Pydantic / FastAPI -> $fetch('/api/auth/login', { body: form })
    await new Promise((resolve) => setTimeout(resolve, 1500))
    
    // 3. Sucesso: Redireciona o cliente para o feed principal da plataforma
    await router.push('/')
  } catch (err: any) {
    // 4. Captura erro via pydantic details e avisa o usuário (UX de erro limpa).
    erroLogin.value = err?.data?.detail || 'Credenciais inválidas. Tente novamente.'
  } finally {
    carregando.value = false // Libera os elementos desativados.
  }
}
</script>

<template>
  <!-- Main Container: Fundo dinâmico ditado pelas cores Tailwind extendidas -->
  <div class="bg-surface text-on-surface antialiased relative overflow-hidden flex flex-col justify-center min-h-[max(884px,100dvh)] font-body">
    
    <!-- Elementos decorativos (Visual Background Accents - Efeito Aurora/Glass) -->
    <!-- São fixos, não bloqueiam cliques pointer-events-none e ficam atrás do formulário (-z-10) -->
    <div class="fixed top-0 left-0 w-full h-full pointer-events-none z-0 overflow-hidden">
      <!-- Glow superior esquerdo (Primário) -->
      <div class="absolute -top-[10%] -left-[10%] w-[50%] h-[50%] rounded-full bg-primary/5 blur-[100px]"></div>
      <!-- Glow inferior direito (Secundário) -->
      <div class="absolute -bottom-[10%] -right-[10%] w-[50%] h-[50%] rounded-full bg-secondary/5 blur-[100px]"></div>
    </div>

    <!-- Interface Principal (Mobile-First de fato - max-w-md centralizado) -->
    <main class="w-full max-w-md mx-auto relative flex flex-col justify-center px-8 py-12 z-10">
      
      <!-- Cabeçalho / Branding -->
      <header class="flex flex-col items-center text-center mb-12">
        <div class="w-16 h-16 bg-primary-container flex items-center justify-center rounded-xl mb-6 shadow-sm">
          <!-- Ícone do Estalo: "bolt" preenchido -->
          <span class="material-symbols-outlined text-primary text-4xl" data-weight="fill" style="font-variation-settings: 'FILL' 1;">bolt</span>
        </div>
        <!-- Utilizando 'font-headline' com font 'Plus Jakarta Sans' conforme sua solicitação -->
        <h1 class="text-3xl font-extrabold text-on-background tracking-tighter mb-2 font-headline">Fome de quê?</h1>
        <p class="text-on-surface-variant font-medium">Entre num estalo</p>
      </header>

      <!-- Snackbar/Caixa de Mensagem de Erro -->
      <Transition name="fade">
        <div
          v-if="erroLogin"
          class="flex items-center gap-2.5 rounded-2xl bg-error-container/20 border border-error/20 px-4 py-3 mb-6"
        >
          <span class="material-symbols-outlined text-error text-xl">error</span>
          <p class="text-sm text-error font-medium">{{ erroLogin }}</p>
        </div>
      </Transition>

      <!-- Formulário de Autenticação -->
      <section class="space-y-6 pb-2">
        <!-- O modificador .prevent previne o comportamento de reload padrão do form HTML -->
        <form @submit.prevent="handleLogin" class="flex flex-col space-y-4">
          
          <!-- Box E-mail -->
          <div class="relative group">
            <input 
              v-model="form.email"
              class="w-full h-14 bg-surface-container-low border-none rounded-2xl px-6 font-medium text-on-surface placeholder:text-outline focus:ring-2 focus:ring-primary/20 transition-all outline-none" 
              placeholder="E-mail" 
              type="email"
              required
            />
          </div>
          
          <!-- Box Senha com alternador de visibilidade ("Olhinho") -->
          <div class="relative group">
            <input 
              v-model="form.senha"
              :type="senhaVisivel ? 'text' : 'password'"
              class="w-full h-14 bg-surface-container-low border-none rounded-2xl px-6 pr-14 font-medium text-on-surface placeholder:text-outline focus:ring-2 focus:ring-primary/20 transition-all outline-none" 
              placeholder="Senha" 
              required
            />
            <!-- Botão de "ver senha" (Absolute, centralizado verticalmente do lado direito) -->
            <button
              type="button"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-outline hover:text-on-surface transition-colors focus:outline-none"
              tabindex="-1"
              @click="senhaVisivel = !senhaVisivel"
            >
              <span class="material-symbols-outlined select-none">
                {{ senhaVisivel ? 'visibility_off' : 'visibility' }}
              </span>
            </button>
          </div>
          
          <!-- Ações auxiliares do formulário -->
          <div class="flex justify-end px-1 pt-1 pb-2">
            <NuxtLink to="/esqueci-senha" class="text-sm font-semibold text-primary-dim hover:text-primary transition-colors">
              Esqueceu a senha?
            </NuxtLink>
          </div>

          <!-- Botão Principal de Submissão -->
          <button 
            type="submit"
            :disabled="carregando"
            class="flex items-center justify-center w-full h-14 bg-inverse-surface text-surface-bright font-bold rounded-full active:scale-95 transition-transform duration-200 shadow-lg shadow-on-background/10 disabled:opacity-70 disabled:active:scale-100"
          >
            <!-- Caso não esteja em loading: -->
            <template v-if="!carregando">
              Entrar
            </template>
            <!-- Spinner caso esteja esperando o backend FastAPI: -->
            <template v-else>
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Entrando...
            </template>
          </button>
        </form>
      </section>

      <!-- Logins com Redes Sociais -->
      <section class="mt-8">
        <!-- Divisor Customizado -->
        <div class="relative flex items-center justify-center mb-8">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full h-[1px] bg-outline-variant/30"></div>
          </div>
          <span class="relative px-4 bg-surface text-sm font-medium text-on-surface-variant">ou continue com</span>
        </div>
        
        <div class="grid grid-cols-2 gap-4">
          <!-- Botão Google -->
          <button type="button" class="flex items-center justify-center h-14 bg-surface-container-lowest border border-outline-variant/20 rounded-full hover:bg-surface-container-low transition-colors active:scale-95 duration-200">
            <Icon name="logos:google-icon" class="w-5 h-5 mr-3" />
            <span class="font-semibold text-sm">Google</span>
          </button>
          <!-- Botão Apple -->
          <button type="button" class="flex items-center justify-center h-14 bg-surface-container-lowest border border-outline-variant/20 rounded-full hover:bg-surface-container-low transition-colors active:scale-95 duration-200">
            <Icon name="logos:apple" class="w-5 h-5 mr-3" />
            <span class="font-semibold text-sm">Apple</span>
          </button>
        </div>
      </section>

      <!-- Rodapé / CTA para Cadastro -->
      <footer class="mt-12 text-center">
        <p class="text-on-surface-variant font-medium">
          Ainda não tem conta? 
          <NuxtLink to="/cadastro" class="text-primary font-bold ml-1 hover:underline">Cadastre-se</NuxtLink>
        </p>
      </footer>

      <!-- Detalhe Visual do Fundo (Borda da Marca) -->
      <div class="mt-16 flex justify-center opacity-20">
        <div class="h-1 w-12 bg-outline-variant rounded-full"></div>
      </div>
    </main>
  </div>
</template>

<style scoped>
/*
 * === TRANSIÇÕES ===
 * A classe "fade" possibilita um visual de fade-in e slide para mensagens de alerta.
 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
