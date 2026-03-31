<script setup lang="ts">
const goBack = () => {
    navigateTo('/inicio') // Redireciona para o início ou use useRouter().back()
}
</script>

<template>
  <div class="bg-surface font-body text-on-surface min-h-screen pb-32">
    <!-- TopAppBar -->
    <header class="fixed top-0 w-full z-50 bg-[#f6f6ff]/80 dark:bg-[#1a1a2e]/80 backdrop-blur-xl shadow-[0_40px_40px_rgba(39,46,66,0.04)]">
      <div class="flex justify-between items-center px-6 h-16 w-full max-w-md mx-auto">
        <button @click="goBack" class="text-[#4647d3] dark:text-[#9396ff] scale-95 active:scale-90 transition-transform hover:opacity-80">
          <span class="material-symbols-outlined">arrow_back</span>
        </button>
        <h1 class="font-headline font-extrabold tracking-tight text-on-surface dark:text-white text-lg">Pedido Confirmado</h1>
        <button class="text-[#4647d3] dark:text-[#9396ff] scale-95 active:scale-90 transition-transform hover:opacity-80">
          <span class="material-symbols-outlined">more_vert</span>
        </button>
      </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-md mx-auto pt-16">
      <!-- Success Header -->
      <section class="bg-surface-container-lowest px-6 py-12 rounded-b-xl shadow-[0_10px_40px_rgba(39,46,66,0.04)] text-center relative z-10">
        <div class="w-24 h-24 rounded-full flex items-center justify-center mx-auto mb-6 bg-surface-container-low text-primary overflow-hidden relative">
          <!-- Success Pulse Aesthetic -->
          <div class="absolute inset-0 bg-primary/10 animate-pulse"></div>
          <span class="material-symbols-outlined text-5xl relative z-10" style="font-variation-settings: 'FILL' 1;">check_circle</span>
        </div>
        <h2 class="text-3xl font-extrabold text-on-surface tracking-tight mb-2 font-headline">Pedido Confirmado</h2>
        <p class="text-on-surface-variant font-medium">O Bistro Pro já recebeu o seu pedido.</p>
        <div class="mt-8 inline-flex items-center gap-3 bg-surface-container-high rounded-full px-6 py-3 font-bold text-primary">
          <span class="material-symbols-outlined text-sm">schedule</span>
          <span>Previsão: 15 - 25 min</span>
        </div>
      </section>

      <!-- Status Tracker (Bento-inspired Card) -->
      <section class="bg-surface-container-lowest rounded-xl p-8 mt-6 shadow-[0_10px_40px_rgba(39,46,66,0.02)] mx-4">
        <h3 class="font-extrabold font-headline text-xl text-on-surface mb-8 flex items-center gap-2">
          Acompanhe a entrega
        </h3>
        <div class="space-y-8 relative">
          <!-- Progress Line -->
          <div class="absolute left-[11px] top-2 bottom-2 w-0.5 bg-surface-container-high"></div>
          <div class="absolute left-[11px] top-2 h-[25%] w-0.5 bg-primary"></div>
          
          <!-- Step 1: Completed -->
          <div class="flex items-start gap-6 relative">
            <div class="w-6 h-6 rounded-full bg-primary flex items-center justify-center z-10 shadow-lg shadow-primary/20">
              <span class="material-symbols-outlined text-white text-[14px]" style="font-variation-settings: 'FILL' 1;">check</span>
            </div>
            <div>
              <p class="text-on-surface font-bold text-lg leading-tight">Pedido Confirmado</p>
              <p class="text-on-surface-variant text-sm">12:45 • Recebido pelo restaurante</p>
            </div>
          </div>
          
          <!-- Step 2: Active -->
          <div class="flex items-start gap-6 relative">
            <div class="w-6 h-6 rounded-full bg-surface-container-lowest border-[6px] border-primary flex items-center justify-center z-10 ring-4 ring-primary/10"></div>
            <div>
              <p class="text-primary font-extrabold text-lg leading-tight">Preparando o seu pedido</p>
              <p class="text-on-surface-variant text-sm">O chef está cuidando de tudo</p>
            </div>
          </div>
          
          <!-- Step 3: Future -->
          <div class="flex items-start gap-6 relative">
            <div class="w-6 h-6 rounded-full bg-surface-container-lowest border-2 border-outline-variant z-10"></div>
            <div>
              <p class="text-on-surface-variant font-semibold text-lg leading-tight">A caminho</p>
              <p class="text-on-surface-variant/60 text-sm">Aguardando saída para entrega</p>
            </div>
          </div>
          
          <!-- Step 4: Future -->
          <div class="flex items-start gap-6 relative">
            <div class="w-6 h-6 rounded-full bg-surface-container-lowest border-2 border-outline-variant z-10"></div>
            <div>
              <p class="text-on-surface-variant font-semibold text-lg leading-tight">Entregue</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Quick Summary Card -->
      <section class="bg-surface-container-lowest rounded-xl p-8 mt-4 shadow-[0_10px_40px_rgba(39,46,66,0.02)] mx-4 mb-24 flex items-center justify-between group hover:bg-surface-container-low transition-colors duration-300">
        <div class="flex gap-4 items-center">
          <div class="w-16 h-16 rounded-lg bg-surface-container-high overflow-hidden">
            <img alt="Classic Burger" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC4peNWYhpzIKXjhhFPK4g2l6ApPy9Ued99hISEiGqL-wwBf8XhYN1hSFzKez91NXjVkCOFRweFKpzGTImlFFdyUpIPBkQhToY4C3aKWriwOvOvnoNLPvv8TCTDIMIujdbGupPEexuTiUvOWhoV2VtqtAnmO-SjVjNM7Bpq-LmaVUBHtnZ2vfVHTibQQuKRT02AORzpz-OWCh5stuD0e11ktKXL681K-yHwocD215G6DR3TjGA-1VqowWcNbV5aBm3PDY6uxNRVElk"/>
          </div>
          <div>
            <span class="text-xs font-bold text-outline uppercase tracking-widest">Pedido #1024</span>
            <h4 class="font-extrabold text-on-surface text-lg leading-tight mt-1">2x Classic Burger</h4>
            <p class="font-bold text-primary text-md">Total: R$ 65,79</p>
          </div>
        </div>
        <span class="material-symbols-outlined text-outline-variant group-hover:text-primary transition-colors">chevron_right</span>
      </section>
    </main>

    <!-- Bottom Navigation Component (Identity & NavMenu) -->
    <LayoutNavbar />
  </div>
</template>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}
</style>
