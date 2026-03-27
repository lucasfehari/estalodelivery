<script setup lang="ts">
// definePageMeta: metadados do Nuxt para esta rota específica
definePageMeta({
  layout: false, // Sem layout padrão — a tela de login é autossuficiente
})

// useRouter: navegação programática do Nuxt
const router = useRouter()

// Estado reativo do formulário
const form = reactive({
  email: '',
  senha: '',
})

// Controle de estado da UI
const carregando = ref(false)    // Bloqueia o botão durante a requisição
const senhaVisivel = ref(false)  // Alterna entre texto e password
const erroLogin = ref('')        // Mensagem de erro vinda do back-end

// Função principal de login — futuramente consumirá o FastAPI
async function handleLogin() {
  erroLogin.value = ''

  // Validação mínima no front antes de bater na API
  if (!form.email || !form.senha) {
    erroLogin.value = 'Preencha e-mail e senha para continuar.'
    return
  }

  carregando.value = true

  try {
    // TODO: Substituir por $fetch('/api/auth/login', { method: 'POST', body: form })
    // quando o back-end FastAPI estiver pronto.
    // Por enquanto, simula um delay de rede para demonstrar o loading state.
    await new Promise((resolve) => setTimeout(resolve, 1500))

    // Redireciona para o feed principal após login bem-sucedido
    await router.push('/')
  } catch (err: any) {
    // Exibe a mensagem de erro retornada pelo FastAPI (ex: "Credenciais inválidas")
    erroLogin.value = err?.data?.detail || 'Erro ao conectar. Tente novamente.'
  } finally {
    carregando.value = false
  }
}
</script>

<template>
  <!--
    Layout geral: fundo escuro degradê do Estalo.
    min-h-screen garante que cobre a tela inteira mesmo sem conteúdo.
    Usamos flex para centralizar verticalmente e horizontalmente.
  -->
  <div
    class="min-h-screen flex items-center justify-center bg-gradient-to-br from-zinc-950 via-zinc-900 to-zinc-950 px-5 py-10"
  >
    <!--
      Card de login:
      - max-w-sm: largura máxima ideal para mobile-first (~384px)
      - backdrop-blur + bg-white/5: efeito glassmorphism sutil
      - ring-1/ring-white/10: borda fina para dar profundidade sem poluir
      - animate-fade-in: animação de entrada suave (definida no tailwind.config)
    -->
    <div
      class="w-full max-w-sm rounded-3xl bg-white/5 backdrop-blur-xl ring-1 ring-white/10 p-8 shadow-2xl"
    >

      <!-- ====== CABEÇALHO / BRANDING ====== -->
      <div class="mb-10 text-center">
        <!--
          Logo "Estalo" em texto:
          - Degradê laranja→rosa→roxo remete à energia, velocidade e modernidade
          - Texto grande e bold para impacto visual imediato
          - bg-clip-text + text-transparent: técnica para aplicar gradiente no texto
        -->
        <h1
          class="text-5xl font-black tracking-tighter bg-gradient-to-r from-orange-400 via-rose-400 to-violet-500 bg-clip-text text-transparent"
        >
          estalo
        </h1>
        <!-- Tagline da marca, extraída da documentação do projeto -->
        <p class="mt-2 text-sm text-zinc-400 font-medium tracking-wide">
          A sacola da cidade ⚡
        </p>
      </div>

      <!-- ====== FORMULÁRIO DE LOGIN ====== -->
      <!--
        @submit.prevent: previne o comportamento padrão do HTML de recarregar a página
        e chama nossa função handleLogin assíncrona.
      -->
      <form class="space-y-5" @submit.prevent="handleLogin">

        <!-- CAMPO: E-mail -->
        <div class="group">
          <label
            for="email"
            class="block text-xs font-semibold text-zinc-400 uppercase tracking-widest mb-2"
          >
            E-mail
          </label>
          <!--
            Ring colorida ao focar: reforça o branding laranja do Estalo.
            transition-all garante que a animação da borda seja suave.
          -->
          <input
            id="email"
            v-model="form.email"
            type="email"
            placeholder="voce@email.com"
            autocomplete="email"
            class="w-full rounded-xl bg-white/[0.07] border border-white/10 px-4 py-3.5 text-sm text-white placeholder-zinc-600 outline-none transition-all duration-200 focus:border-orange-500/70 focus:ring-2 focus:ring-orange-500/20"
          />
        </div>

        <!-- CAMPO: Senha -->
        <div class="group">
          <div class="flex items-center justify-between mb-2">
            <label
              for="senha"
              class="block text-xs font-semibold text-zinc-400 uppercase tracking-widest"
            >
              Senha
            </label>
            <!-- Link "Esqueci a senha" — rota será criada futuramente -->
            <a
              href="#"
              class="text-xs text-orange-400 hover:text-orange-300 transition-colors duration-200"
            >
              Esqueci a senha
            </a>
          </div>
          <!-- Wrapper relativo para posicionar o ícone de ver/ocultar senha inside do input -->
          <div class="relative">
            <input
              id="senha"
              v-model="form.senha"
              :type="senhaVisivel ? 'text' : 'password'"
              placeholder="••••••••"
              autocomplete="current-password"
              class="w-full rounded-xl bg-white/[0.07] border border-white/10 px-4 py-3.5 pr-12 text-sm text-white placeholder-zinc-600 outline-none transition-all duration-200 focus:border-orange-500/70 focus:ring-2 focus:ring-orange-500/20"
            />
            <!--
              Botão de olhinho: alterna senhaVisivel entre true/false.
              type="button" é obrigatório para NÃO submeter o formulário ao clicar.
            -->
            <button
              type="button"
              class="absolute right-3.5 top-1/2 -translate-y-1/2 text-zinc-500 hover:text-zinc-300 transition-colors duration-200"
              :aria-label="senhaVisivel ? 'Ocultar senha' : 'Mostrar senha'"
              @click="senhaVisivel = !senhaVisivel"
            >
              <!-- Ícone "olho aberto" — exibe quando senha está oculta -->
              <svg
                v-if="!senhaVisivel"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.8"
                stroke="currentColor"
                class="w-5 h-5"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.964-7.178Z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
              </svg>
              <!-- Ícone "olho riscado" — exibe quando senha está visível -->
              <svg
                v-else
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.8"
                stroke="currentColor"
                class="w-5 h-5"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88" />
              </svg>
            </button>
          </div>
        </div>

        <!-- FEEDBACK DE ERRO: só aparece quando erroLogin tem conteúdo -->
        <Transition name="fade">
          <div
            v-if="erroLogin"
            class="flex items-center gap-2.5 rounded-xl bg-rose-500/10 border border-rose-500/20 px-4 py-3"
          >
            <!-- Ícone de alerta inline -->
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-4 h-4 text-rose-400 shrink-0">
              <path fill-rule="evenodd" d="M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0Zm-8-5a.75.75 0 0 1 .75.75v4.5a.75.75 0 0 1-1.5 0v-4.5A.75.75 0 0 1 10 5Zm0 10a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z" clip-rule="evenodd" />
            </svg>
            <p class="text-xs text-rose-400 font-medium">{{ erroLogin }}</p>
          </div>
        </Transition>

        <!-- BOTÃO PRINCIPAL DE LOGIN -->
        <!--
          :disabled="carregando": desabilita o botão durante a requisição, evitando duplo clique.
          O degradê do botão segue a identidade visual do logo Estalo.
        -->
        <button
          type="submit"
          :disabled="carregando"
          class="relative w-full mt-2 rounded-xl py-3.5 text-sm font-bold text-white bg-gradient-to-r from-orange-500 via-rose-500 to-violet-600 shadow-lg shadow-orange-500/20 transition-all duration-300 hover:shadow-orange-500/40 hover:scale-[1.02] active:scale-[0.98] disabled:opacity-60 disabled:cursor-not-allowed disabled:hover:scale-100 overflow-hidden"
        >
          <!-- Estado normal do botão -->
          <span v-if="!carregando" class="flex items-center justify-center gap-2">
            Entrar no Estalo
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-4 h-4">
              <path fill-rule="evenodd" d="M3 10a.75.75 0 0 1 .75-.75h10.638L10.23 5.29a.75.75 0 1 1 1.04-1.08l5.5 5.25a.75.75 0 0 1 0 1.08l-5.5 5.25a.75.75 0 1 1-1.04-1.08l4.158-3.96H3.75A.75.75 0 0 1 3 10Z" clip-rule="evenodd" />
            </svg>
          </span>

          <!-- Estado de loading: spinner animado enquanto aguarda o back-end -->
          <span v-else class="flex items-center justify-center gap-2">
            <svg class="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 0 1 8-8V0C5.373 0 0 5.373 0 12h4z" />
            </svg>
            Entrando...
          </span>
        </button>
      </form>

      <!-- ====== DIVISOR ====== -->
      <div class="my-7 flex items-center gap-4">
        <div class="h-px flex-1 bg-white/10" />
        <span class="text-xs text-zinc-600 font-medium">ou</span>
        <div class="h-px flex-1 bg-white/10" />
      </div>

      <!-- ====== LINK PARA CADASTRO ====== -->
      <p class="text-center text-xs text-zinc-500">
        Novo por aqui?
        <!--
          NuxtLink: componente do Nuxt para navegação SPA sem reload de página.
          Rota /cadastro será criada futuramente.
        -->
        <NuxtLink
          to="/cadastro"
          class="ml-1 font-semibold text-orange-400 hover:text-orange-300 transition-colors duration-200"
        >
          Criar conta grátis
        </NuxtLink>
      </p>

    </div>
  </div>
</template>

<style scoped>
/*
  Animação de fade para o bloco de erro.
  Usamos <Transition name="fade"> no template, então o Vue
  procura automaticamente pelas classes .fade-enter-* e .fade-leave-*.
*/
.fade-enter-active,
.fade-leave-active {
  transition: all 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
