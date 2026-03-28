<script setup>
// ─── Mock Data ───────────────────────────────────────────────────────────────

const categories = [
  { id: 1, emoji: '🍔', label: 'Lanches' },
  { id: 2, emoji: '🛒', label: 'Mercado' },
  { id: 3, emoji: '💊', label: 'Farmácia' },
  { id: 4, emoji: '🎧', label: 'Eletrônicos' },
  { id: 5, emoji: '🥤', label: 'Bebidas' },
  { id: 6, emoji: '🐾', label: 'Pet' },
  { id: 7, emoji: '🧁', label: 'Doces' },
  { id: 8, emoji: '⚡', label: 'Express' },
]

const banners = [
  {
    id: 1,
    bgClass: 'bg-red-500 shadow-red-500/20',
    tag: 'Oferta Especial',
    title: 'Cupom de <br/>R$ 10 OFF',
    subtitle: 'No seu primeiro pedido',
    type: 'image',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCcT-lDOqDhWaXvJbJyhqmFfVac55AZusXM9pD4S71btcx7EVrB3vUkIYB0bZ9UFMIK8LE4sLm84neiK5h3hWPHfu34xRhKvZTG9SY--TmNHh1Fwf-HRCrT-nY_j8z7v39gK5mzwMIOyIwh5EtYol1mrZ53QA1DSUw-N2974OdmppYZ0lEJLXVZLLadz9PZlUXI-juQql5ZQORYnRUChDXI1PgAm9KnocBianSgwIncRGnTSDFjqDE-5kfBmcBJV2KY_ZY3fVmlarI',
  },
  {
    id: 2,
    bgClass: 'bg-indigo-600 shadow-indigo-600/20',
    tag: 'Fast Delivery',
    title: 'Tudo em até <br/>15 min',
    subtitle: 'Entrega Grátis hoje',
    type: 'icon',
    icon: 'electric_bolt',
  },
]

const featuredProducts = [
  {
    id: 1,
    name: 'Classic Burger',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCkEPmDJpxNBh2AKmWnZZXPvhCyZdl-mogJO-c5L3HXJa8RYmOuYHDCScfUktKR411dRHcG8bf-fEvnl2V0hEiNKRsfjfVjNokSoBDqsKviQaQGAe3sbKEJ8dA-N-2IG8ayoqK2v5OtP9xbPPbtgFLwdUZasXCWeH6Bl94vPT9qjHInnRDpbEycNTn2ZCS69WXFChD29pz3aliKMEIQrN-0ruhk41N0VwrLg_pw6wbLkZZ9uQDAlp_Q30W7Hn78aNyEuGFqS-loCv4',
    deliveryTime: '15-25 min',
    price: 'R$ 19,90',
    originalPrice: 'R$ 29,90',
  },
  {
    id: 2,
    name: 'Salada Tropical',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBL7i86CQb55uIJCe4EoyoFgZstygeEXTCu5Z7GEHgPmt8ll_hmb0tO-jVAhiZNjzyQlnSnc4cfIzjMlMsqNx4fxEMCt9ASDWf-nDPGJRnIK2j95QKTzk0vjWLV48tTjPPlBxyG1MNTK43ue_6Uyy527_UyVGa4PTgU7vMfOetfTzb_5ULkEOteeX0deV23fGr9eL3Tglolkonkc9KxpmRpEVouBT0mMYpWazieU3SqLKdCKY0UAgQ6Iy7IGRJ8ES7zKJhSiHFuidw',
    deliveryTime: '10-20 min',
    price: 'R$ 24,50',
    originalPrice: 'R$ 32,00',
  },
  {
    id: 3,
    name: 'Pizza Brotinho',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAbWKyk81REuO6aOtktmpcCT_Fz_Ac-exomOsdG0FmVw7umPy5piVC5NuoRwYdwzhlnNe7K4PKFaDzhOVrBL6WG9Ejr8ivsFojDPk8VcXkG5s86-6vEkP5HQGnnzLgdHUjQxI7u9pHXapvG_w0HIN9L5dz77oUiIaFLqiscE3dcfe9Lk4KRlsF0N-P-klR8kojQRk8hbnBYShNlrjB3Ih2GrAi89FMmdaxrv8lwi2jrV_kC7aTGw9soLzIruF-BHy5-z8XbMf_WZTM',
    deliveryTime: '20-30 min',
    price: 'R$ 15,90',
    originalPrice: 'R$ 22,00',
  },
]

const premiumStores = [
  {
    id: 1,
    name: 'Bistro Pro',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDP2UqbDBYcL6-Ur1w96yPZSPfCPA2d4riKbsKHZqPRLni5uNc6p9Aus7XAr5hFZa-jwEyRYiUiOOX0zFYXqzz5kavu_YQNpdhpquf8sC3Mgj7DdV3-SKkuW-4UU5NCxIeqbjHxyIR2Ua7An9eBqCQ586p2sHuEOnv0DpbgjYQKZR5bHR3InsY6rOT8CMnrVU9B-G2mQ0uH9-PSPvRSWnBDGvi_S20zRaRD47gMtYCDvyXspHLFWmJ5S1xiAXwJsRcvmBDEsKihRUo',
  },
  {
    id: 2,
    name: 'Sushi Way',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAU9Pl7YFuNd26nHe_875oq0gd1LZJqLt5bdaqdsKlcNPTDUprvYRDVgUuz1QktJadFTyJfjbOeFHdrqqyCllUmXS64O-tMoC5kf7VEsnQZIGjnCIAV8D2_fC74hibuZNcwfU-S88j1qlDNBLvBLlEcAF-bpvNBiTm0szgX332eRZHn0Kl9H_IWbmZ7FbkbxICLPq0nOqUKbZC1d25DVkfLfWH07jnIOHvHLCa7zmRp4tlDu1sJKNbZ-JnUhOWhYttPWc4a-zqDweg',
  },
  {
    id: 3,
    name: 'Urban Tech',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAOvYRv9mwLyzwMILw5DCoHg-gJxLZw7CvuQb3pcGJpblnvTCo5stgBAVrGmyP2RhakkYhxo7OX4k-odAzCzvASyvmPZ1nVxeaGTXE4HAbUXh1UcFxBHkOnJUuP51TQV7wqVeUE2OjVJz3w_GDEX1dmJ0eBTlP18jf7zJcgJPebb5i3OLYB8gDCqspCGqJnt2oeJcCej0iK_oJmij_9mgOtqs5kQ5CZZztJ4bgnjN8LRKbbl-igNPDt7ahiMdmq9LRjP4ldRcubhHg',
  },
  {
    id: 4,
    name: 'Star Coffee',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCg4lHeU57hIvyxn4UVRBxTmnMUN6hMAZRhQODEIW4HSR4FSYdgD8xux0aRW6zLkze3BX3hl9JYfoilmwWAl0mZs3jpM_B_R_2zz1SGBdeNDtX0P2M9xXxO17MDGOWbKE-wX8rGuVfLPF2qogRX3tUjlBg20mJ1hJwMhI22QErMe_-HGuEZDD_mu7ypnsrA-BjWx1k9ZPY8iYCHZtXAXwMNwjxlvv0ROnPOthRS9bqloXax2hzTAVt-iYR3wD6qCMUC1xxTJdPb_qw',
  },
  {
    id: 5,
    name: 'Boutique',
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAa5WoLFmu2Wf0HGDgb2M_UcsYZL3ZFeRGLckJG00Vp8P911dLkhu33d2H7sADIcKj7zE77n2mRwC2rMv1RapAanHoiIakaPYvzujfWEZGTBp_Uy4qtV2UX3rl8_9fRdphDhwb-45dU6rpdtvhjoagejabn3fMZaTka9p5xkStFxNOkoUI47tkIGpLZ_xB-Ec9SMs-ilTH3nkp2kItjEVs39ZkbLFXZ85jL4s47oE4alUzmGxFtFKhBYqpfVMlwj80VEJ5GYM223nk',
  },
]


const user = {
  name: 'Lucas',
}
</script>

<template>
  <!-- Header -->
  <HomeHeader />

  <!-- Main Content -->
  <main class="pt-20 pb-28 px-5 space-y-8">
    <!-- Hello User -->
    <HomeHello :user="user" />
    <!-- Search -->
    <HomeSearch />

    <!-- Categories Grid -->
    <HomeCategories :categories="categories" />

    <!-- Banners Carousel -->
    <HomeBanners :banners="banners" />

    <!-- Featured Products -->
    <HomeProducts :products="featuredProducts" />

    <!-- Premium Stores -->
    <HomeStores :stores="premiumStores" />
  </main>

  <!-- Bottom Navigation -->
  <LayoutNavbar />

  <!-- Action Buttons (FABs) -->
  <HomeActionButtons />
</template>
