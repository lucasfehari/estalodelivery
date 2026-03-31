<script setup lang="ts">
import { ref } from 'vue'

const goBack = () => {
  useRouter().back()
}

// pix | maquininha | dinheiro
const selectedPayment = ref('pix')
const trocoPara = ref('')

const finalizeOrder = () => {
  // Integre a chamada da API do pedido aqui caso decida mover do carrinho.vue
  navigateTo('/pedido-confirmado')
}
</script>

<template>
  <div class="bg-surface font-body text-on-surface min-h-screen pb-32">
    <!-- Top AppBar Component -->
    <header class="fixed top-0 w-full z-50 bg-[#f6f6ff]/80 backdrop-blur-xl shadow-[0px_40px_40px_rgba(39,46,66,0.04)]">
      <div class="flex items-center justify-between px-6 py-4 w-full max-w-md mx-auto">
        <div class="flex items-center gap-4">
          <span @click="goBack" class="material-symbols-outlined text-[#4647d3] active:scale-95 transition-transform duration-200 cursor-pointer">arrow_back</span>
          <h1 class="font-headline font-extrabold tracking-tighter text-xl text-[#272e42]">Checkout</h1>
        </div>
        <div class="w-6"></div> <!-- Spacer for center alignment logic -->
      </div>
    </header>

    <main class="pt-24 pb-32 px-4 max-w-md mx-auto">
      <!-- Payment Section Container -->
      <section class="bg-surface-container-lowest p-6 rounded-xl shadow-[0px_40px_40px_rgba(39,46,66,0.04)]">
        <h2 class="font-headline font-extrabold text-lg text-on-surface mb-6 tracking-tight">Pagar na entrega</h2>
        <div class="space-y-3">
          
          <!-- Option 1: PIX -->
          <div 
            @click="selectedPayment = 'pix'"
            :class="selectedPayment === 'pix' ? 'border-2 border-on-surface bg-surface-container-low' : 'border border-outline-variant/30 bg-surface-container-lowest hover:bg-surface-container-low/50'"
            class="rounded-lg p-5 flex items-center justify-between transition-all duration-200 active:scale-[0.98] cursor-pointer"
          >
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 rounded-full bg-primary flex items-center justify-center">
                <span class="material-symbols-outlined text-white" style="font-variation-settings: 'FILL' 0;">qr_code_2</span>
              </div>
              <div>
                <p class="font-headline font-bold text-on-surface leading-tight">PIX</p>
                <p class="text-on-surface-variant text-xs font-medium">(Pagamento rápido)</p>
              </div>
            </div>
            <div 
              v-if="selectedPayment === 'pix'"
              class="w-6 h-6 rounded-full bg-on-surface flex items-center justify-center"
            >
              <span class="material-symbols-outlined text-white text-sm" style="font-variation-settings: 'FILL' 1;">check</span>
            </div>
            <div v-else class="w-6 h-6 rounded-full border-2 border-outline-variant/50"></div>
          </div>

          <!-- Option 2: Maquininha -->
          <div 
            @click="selectedPayment = 'maquininha'"
            :class="selectedPayment === 'maquininha' ? 'border-2 border-on-surface bg-surface-container-low' : 'border border-outline-variant/30 bg-surface-container-lowest hover:bg-surface-container-low/50'"
            class="rounded-lg p-5 flex items-center justify-between transition-all duration-200 active:scale-[0.98] cursor-pointer"
          >
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 rounded-full bg-surface-container-high flex items-center justify-center">
                <span :class="selectedPayment === 'maquininha' ? 'text-primary' : 'text-on-surface-variant'" class="material-symbols-outlined">credit_card</span>
              </div>
              <div>
                <p class="font-headline font-bold text-on-surface leading-tight">Maquininha</p>
                <p class="text-on-surface-variant text-xs font-medium">(Crédito/Débito)</p>
              </div>
            </div>
            <div 
              v-if="selectedPayment === 'maquininha'"
              class="w-6 h-6 rounded-full bg-on-surface flex items-center justify-center"
            >
              <span class="material-symbols-outlined text-white text-sm" style="font-variation-settings: 'FILL' 1;">check</span>
            </div>
            <div v-else class="w-6 h-6 rounded-full border-2 border-outline-variant/50"></div>
          </div>

          <!-- Option 3: Dinheiro -->
          <div 
            @click="selectedPayment = 'dinheiro'"
            :class="selectedPayment === 'dinheiro' ? 'border-2 border-on-surface bg-surface-container-low' : 'border border-outline-variant/30 bg-surface-container-lowest hover:bg-surface-container-low/50'"
            class="rounded-lg p-5 flex flex-col gap-4 transition-all duration-200 active:scale-[0.98] cursor-pointer"
          >
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-full bg-surface-container-high flex items-center justify-center">
                  <span :class="selectedPayment === 'dinheiro' ? 'text-primary' : 'text-on-surface-variant'" class="material-symbols-outlined">payments</span>
                </div>
                <div>
                  <p class="font-headline font-bold text-on-surface leading-tight">Dinheiro</p>
                </div>
              </div>
              <div 
                v-if="selectedPayment === 'dinheiro'"
                class="w-6 h-6 rounded-full bg-on-surface flex items-center justify-center"
              >
                <span class="material-symbols-outlined text-white text-sm" style="font-variation-settings: 'FILL' 1;">check</span>
              </div>
              <div v-else class="w-6 h-6 rounded-full border-2 border-outline-variant/50"></div>
            </div>
            
            <!-- Change Input (Mostra apenas se Dinheiro estiver selecionado) -->
            <div class="pl-16" v-show="selectedPayment === 'dinheiro'">
              <div class="relative">
                <input 
                  v-model="trocoPara"
                  @click.stop
                  class="w-full bg-surface border-none rounded-lg px-4 py-3 text-sm font-medium placeholder:text-on-surface-variant/60 focus:ring-2 focus:ring-primary/20 text-on-surface focus:outline-none transition-shadow" 
                  placeholder="Troco para quanto?" 
                  type="text"
                />
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- Summary Section (Contextual) -->
      <div class="mt-8 p-6 bg-primary-container/10 rounded-xl border-none">
        <div class="flex justify-between items-center">
          <span class="font-body font-medium text-on-surface-variant">Total a pagar</span>
          <!-- Temporariamente fixo, você pode integrar com seu carrinho (Pinia ou ref) -->
          <span class="font-headline font-extrabold text-2xl text-on-surface tracking-tighter">R$ 84,90</span>
        </div>
        <button 
          @click="finalizeOrder"
          class="w-full mt-6 bg-primary text-white font-headline font-bold py-4 rounded-full shadow-[0px_10px_20px_rgba(70,71,211,0.2)] active:scale-95 transition-all text-lg"
        >
          Finalizar Pedido
        </button>
      </div>
    </main>

    <!-- Bottom Navigation Component -->
    <LayoutNavbar />
  </div>
</template>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  display: inline-block;
  line-height: 1;
}
</style>
