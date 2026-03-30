<script setup lang="ts">
import { ref, computed } from 'vue'

const storeDetails = ref({
  name: "Bistro Pro",
  eta: "Pronto em 25-35 min"
})

const cartItems = ref([
  {
    id: 1,
    name: "Classic Burger",
    price: 29.90,
    description: "Pão brioche, carne 180g, cheddar e bacon.",
    quantity: 1,
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuCoGjSMXkI0Nh8UB0xd60kr14WUJmUvoCiNCni8rymiWeXPvqwCSrW0EldefV2cL6756g1INz9LGGJsEUPriIE5GFHnZERDV1wG2kcBf1AsoO0PxBJv4hVSGIa9ySw2RZD9zSJpsBBFKD1OXzbiR2LlQX0fms2iD9X7nP7woSKjlZx3ngmLxZSIFkSZjmlwZpl9sQVMm062GgHvG9tlbRiv_GxTKg8LiFNGGl3TPHXpItWzdyCyn4b89-nfXE4q_HlLqAZ7JQyfLJQ"
  },
  {
    id: 2,
    name: "Coca-Cola",
    price: 5.90,
    description: "Lata 350ml - Gelada",
    quantity: 1,
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuDnKgMcpxwP5QtHRWKzfdx6vYQZEqz9zx96B1BMYpaWtIt_F2CueAMLqmnCTi7sK3PuJWFw9e4-qzxs1zS-RN_b-iuKRCWSqI0HiFwB70a8ESwzgfBeHqEgvwRLy8tSCdI3U4LSi95ZZxZRsI5Pn3KlA7KM5hMAq00KhxfsbsMv0n-6DTnZmhmnzJpc0xoaCu2j2sl3QooS62i6yHYQ3iik43CicmzGllrMJcYL-foDy6oviZqzvKbJcbZkr2h2YaqgNDlSqQMq06I"
  }
])

const upsellItems = ref([
  {
    id: 1,
    name: "Batata Média",
    price: 9.90,
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuDoB4zL1oZ3Dj69vHSKuqKKQnx0WsF28TxLvdPhIsUsHlxQmcmzmA5s7E8e2g7GqEOwJpjmNMgyGAXQ-faUZTnJMxr9saH3YajyC0gmrO7UMHmA15a8kywbVHbVuY3q08x7q9w-iSPujGaAR2IkJX5xpk0dfdFD9ZnSmuDCMRMxnQZn8_sd_S_8xvo9e5lDb1et3OL9BJ8oKfXxW8KHT1X4p6IiOThhM71sUfE8JLTgEopXZUKwwUoZxjgWjT-qsRNCLlL2yMJgAy0"
  },
  {
    id: 2,
    name: "Brownie",
    price: 12.00,
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuBJpwbu-eorBzZ8ez3fOkx5PYdMdggnxtMVw3cRS1ad3ieIqvtBcw6uzduql0Gh4sGM0j0pumIvngmHWkLzdo3H9xF2LpKYGeePf4WBcXnC26O73RLcS17FAkEr7anJjAHGHMMQfClZB7Xz4Cb9-Qj1E7KX73bvwoO43eaRwyruPHjpVVXhPF1lqx4HlhrPZ6AvSyN3m9nX5FgR7HuMpaY1mtDvldUJbtjUptzfu3_yoU9dx59sa-29Yw8E8m_AiwqDvdz_Kj9if7U"
  },
  {
    id: 3,
    name: "Molho Extra",
    price: 3.50,
    image: "https://lh3.googleusercontent.com/aida-public/AB6AXuDhnWhro_ke0bQ56erUCwocXOMuwJOciDhg6OFhzDIxLR_VHprIxuKqKbYq9Y4X2uWwIb_YOlnsCB5Nu5gwyCXTPa_GqxXOumiLC5gIEJTIuUpsNKT1I9TemA3hcc7Vtb9CJeekON_69nMasZuKSiDBgkTI5VTe7o-ikH5RO1vkQhuC0BkWHu723lW9cVLdbg2RnaXKxyKNWxL3WQDASVKJuUueUFBqF1EYVhc6O3sJmBHJCJSHGFUfV44C5c_PSiXCCjXF21lxMFY"
  }
])

const deliveryFee = ref(5.99)

const subtotal = computed(() => {
  return cartItems.value.reduce((total, item) => total + (item.price * item.quantity), 0)
})

const totalOrderPrice = computed(() => subtotal.value + deliveryFee.value)

const formatPrice = (value: number) => {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)
}

const increaseQuantity = (id: number) => {
  const item = cartItems.value.find(i => i.id === id)
  if (item) item.quantity += 1
}

const decreaseQuantity = (id: number) => {
  const item = cartItems.value.find(i => i.id === id)
  if (item) {
    if (item.quantity > 1) {
      item.quantity -= 1
    } else {
      cartItems.value = cartItems.value.filter(i => i.id !== id)
    }
  }
}

const addUpsellToCart = (upsell: any) => {
  const existingItem = cartItems.value.find(i => i.name === upsell.name)
  if (existingItem) {
    existingItem.quantity += 1
  } else {
    cartItems.value.push({
      id: Date.now(),
      name: upsell.name,
      price: upsell.price,
      description: 'Adicionado como extra',
      quantity: 1,
      image: upsell.image
    })
  }
}

const handleCheckout = () => {
  console.log("Iniciando fluxo de fechamento para: Total =>", formatPrice(totalOrderPrice.value))
}
</script>

<template>
<div class="bg-surface font-body text-on-surface">
  <!-- Main Container -->
  <main class="min-h-screen max-w-md mx-auto relative bg-surface-container-low pb-40">
    <!-- TopAppBar Shared Component -->
    <header class="sticky top-0 w-full z-50 bg-surface-container-low backdrop-blur-2xl shadow-[0_40px_40px_-15px_rgba(39,46,66,0.04)] flex justify-between items-center px-8 py-4 w-full no-border tonal-shift bg-[#eef0ff] bg-surface-container-low">
      <button class="active:scale-95 duration-200 hover:opacity-80 transition-opacity">
        <span class="material-symbols-outlined text-[#6366f1]" data-icon="arrow_back">arrow_back</span>
      </button>
      <h1 class="font-['Plus_Jakarta_Sans'] font-extrabold tracking-tight text-[#272e42] text-primary text-lg">Checkout</h1>
      <button class="active:scale-95 duration-200 hover:opacity-80 transition-opacity" @click="cartItems = []">
        <span class="material-symbols-outlined text-[#6366f1]" data-icon="delete_outline">delete_outline</span>
      </button>
    </header>

    <!-- Store Header -->
    <section class="mt-4 px-8 py-6 bg-surface-container-lowest rounded-xl mx-4 flex justify-between items-center">
      <div>
        <h2 class="font-headline font-extrabold text-xl tracking-tight text-on-surface">{{ storeDetails.name }}</h2>
        <p class="text-on-surface-variant text-sm font-medium">{{ storeDetails.eta }}</p>
      </div>
      <a class="text-primary font-bold text-sm hover:underline" href="#">Ver cardápio</a>
    </section>

    <!-- Item List (Bento-ish Layers) -->
    <section class="mt-4 mx-4 space-y-3">
      <div v-if="cartItems.length === 0" class="text-center py-10 bg-surface-container-lowest rounded-xl">
          <p class="font-bold text-on-surface-variant font-headline">Seu carrinho está vazio.</p>
      </div>
      <div v-for="item in cartItems" :key="item.id" class="bg-surface-container-lowest p-6 rounded-xl flex items-center gap-5">
        <div class="relative w-24 h-24 flex-shrink-0">
          <img class="w-full h-full object-cover rounded-lg" :src="item.image" :alt="item.name" />
        </div>
        <div class="flex-grow flex flex-col gap-2">
          <div class="flex justify-between items-start">
            <h3 class="font-headline font-bold text-on-surface">{{ item.name }}</h3>
            <span class="font-bold text-on-surface">{{ formatPrice(item.price) }}</span>
          </div>
          <p class="text-on-surface-variant text-xs line-clamp-1">{{ item.description }}</p>
          <div class="flex items-center justify-between mt-2">
            <div class="flex items-center gap-4 bg-surface-container px-4 py-2 rounded-full">
              <span @click="decreaseQuantity(item.id)" class="material-symbols-outlined text-sm cursor-pointer select-none text-on-surface-variant">remove</span>
              <span class="font-bold text-sm text-on-surface">{{ item.quantity }}</span>
              <span @click="increaseQuantity(item.id)" class="material-symbols-outlined text-sm cursor-pointer select-none text-primary">add</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Upsell Section -->
    <section class="mt-10" v-show="cartItems.length > 0">
      <h2 class="font-headline font-extrabold text-lg px-8 mb-4 text-on-surface tracking-tight">Que tal adicionar?</h2>
      <div class="flex gap-4 overflow-x-auto hide-scrollbar px-8 pb-4">
        <div v-for="upsell in upsellItems" :key="upsell.id" class="min-w-[140px] bg-surface-container-lowest p-4 rounded-xl flex flex-col gap-2 shadow-sm">
          <img class="w-full h-24 object-cover rounded-lg" :src="upsell.image" :alt="upsell.name" />
          <p class="font-bold text-xs text-on-surface">{{ upsell.name }}</p>
          <div class="flex justify-between items-center mt-1">
            <span class="text-xs font-bold text-secondary">+ {{ formatPrice(upsell.price) }}</span>
            <div @click="addUpsellToCart(upsell)" class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-on-primary shadow-lg shadow-primary/20 active:scale-90 transition-transform cursor-pointer">
              <span class="material-symbols-outlined text-sm">add</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Summary Section -->
    <section class="mt-8 mx-4 p-8 bg-surface-container-lowest rounded-xl">
      <div class="space-y-4">
        <div class="flex justify-between items-center">
          <span class="text-on-surface-variant font-medium">Subtotal</span>
          <span class="text-on-surface font-semibold">{{ formatPrice(subtotal) }}</span>
        </div>
        <div class="flex justify-between items-center">
          <span class="text-on-surface-variant font-medium">Taxa de entrega</span>
          <span class="text-tertiary-fixed-dim font-bold">{{ deliveryFee > 0 ? formatPrice(deliveryFee) : 'Grátis' }}</span>
        </div>
        <div class="pt-4 mt-2 border-t border-surface-container flex justify-between items-center">
          <span class="font-headline font-extrabold text-lg text-on-surface">Total</span>
          <span class="font-headline font-extrabold text-2xl text-on-surface">{{ formatPrice(totalOrderPrice) }}</span>
        </div>
      </div>
    </section>

    <!-- Fixed Bottom Action Bar -->
    <footer class="fixed bottom-0 left-0 right-0 max-w-md mx-auto z-50 p-6" v-show="cartItems.length > 0">
      <div class="bg-surface-container-lowest/90 rounded-xl shadow-[0_-10px_40px_rgba(39,46,66,0.1)] p-4 flex flex-col gap-4">
        <button @click="handleCheckout" class="w-full h-16 rounded-full bg-primary text-white font-headline font-extrabold text-lg flex items-center justify-between px-8 active:scale-95 transition-all duration-200 shadow-xl shadow-primary/20">
          <span class="tracking-tight">Fazer Pedido</span>
          <div class="h-6 w-px bg-white/30"></div>
          <span>{{ formatPrice(totalOrderPrice) }}</span>
        </button>
      </div>
    </footer>

    <!-- BottomNavBar Shared Component Integration (Navigation Context) -->
    <nav class="fixed bottom-0 left-0 w-full flex justify-around items-center px-10 pb-8 pt-4 bg-surface-container-lowest/90 backdrop-blur-2xl shadow-[0_-10px_40px_rgba(39,46,66,0.06)] rounded-t-[3rem] z-40">
      <!-- Active State: Shopping Bag based on the checkout intent -->
    
      <!-- Inactive State -->
      <div class="flex flex-col items-center justify-center text-[#535b71] dark:text-[#9396ff] p-4 hover:scale-105 transition-transform active:scale-90 duration-200">
        <span class="material-symbols-outlined" data-icon="bolt">bolt</span>
      </div>
    </nav>
  </main>
</div>
</template>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>
