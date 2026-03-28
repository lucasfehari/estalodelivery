<script setup>
const pulseItems = [
  {
    id: 1,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuAAkVDA_AnfG2nTET4ZsoSPRdQJBn6jTOkrmK95OFpgsqRMks4XX8Bi5rTl_h4UmDEVWFy-ADZtk9w0Z0Uk31SgPW9xNPsiPSzakacB7-GqZS0OmuYdkZi4S8ChFVPAFhg3DWnpehaRyPhtdx6AVVnciIal4ou7HLqtrliFNm4O2Q4V84mUiQ0rqZUaDTDlnKX1F2DTCke0j3OkLArzNFYD7zWEEDlcAiX7ofAntwkdxEcHe5T9GnIxxfRdfvWl65ZnCQIk-5rzmjY',
    merchantName: 'Burger Master',
    merchantLogo: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBasMyCtMA9DNqUqib6EcZS2US4grjSAL21BPM1xz8RwA5ZVb1Znux5jKlM2oVsPWgooOJocEITP-Kushdsp6uUNTP9Mf1ld1_b9Y-UU5EHviwyJ6PCN9kD5fUne_PUaVOS-P8XRfbtiIGfVjYeXFDw6UprzhjFnMkA-aHUJH1FbsMX1IBO0jR7RXJwE-OBSIgOFSy-yebeCyTFDAICX40fVEPrnF8XptjrRo1psNxA-EzDMZFV6rBRWKk67Rqe6ZcbeqAP9LwH0AY',
    merchantBorderClass: 'border-primary-fixed',
    title: 'Juicy Burger Classic',
    description: 'Double Wagyu beef, truffle aioli, aged cheddar.',
    price: 'R$ 34,90',
    likesCount: '1.2k',
  },
  {
    id: 2,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDDJ9nHnRXRUNsgKHGe6SgYaFeOQRjO7uhCvKKI09Rr8qrg4hRP3MrEB6UejYpy8H1zcmxZ7S0M_Ao0anV3Qe9iufwT4iwKZ9PJXX0nbqvWGzUpWmf6I-HRHPQ07u3iq2fvCoD5cPiL4DFogD6YqSjA8UkxstU6uqeedfb2W7Do1z4AYszMoKrBcN8tHzCCr10PzakfPA_Du6wIYwsIgHFOov0UZwgkQ5qL4ezAhUqCygSAbmw9zT-wtW2mijlUjCeM3MvdZgahJqE',
    merchantName: 'Sushi Zen',
    merchantLogo: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBpzblUepQJ5tFuFMbYi8dt0-X3YQ38ano2SSnm8cUi4CfYR_vDNtRaWbF77PM1c7A0Yx4SePv3p-fvUwhcuEc9DO9XieUJ5foUESDimF0mesVIEjnbaQ320qS9Ei6QnhhJCgl6C2diz0prIg0Wy8p0Wm_wC3rGdgezoQe4VMYxQL450w4fvpSxU4AvgY711Mk4Z-7Xg5FFhh6WUgR1BbwKGKmSxjf33kAMKz5Iv9S0qH1HGq_PUU2-D_V_xxE7gcGprd9nRJF4-8U',
    merchantBorderClass: 'border-secondary-fixed',
    title: 'Fresh Sushi Platter',
    description: "24 pieces of chef's choice premium sashimi & rolls.",
    price: 'R$ 89,00',
    likesCount: '856',
  },
  {
    id: 3,
    image: 'https://lh3.googleusercontent.com/aida-public/AB6AXuCsD7N7ObQS-UYZrWEUA_FcoNVGewWg49P7xIOzFBmjhz9N05oh7nm3sLX8X9aorZdu_NwxFcnH9rvMbckThLDg_lFr_WhWTc1JN65ufSQ1qhywUYSlWtnH0dSE0vZ-6PUZJg0oKeuIS87zWwm_Z88GSIuD38m7bHheSUrTW6g700p-10geYje_n8p5vj6kLvI9MwRnZY-qHaS_k4UJfgFhZi2PIRLuJYC7Efj_LiDGmNAN9OFIVHuJozl0_IwSdh7k0eZ83werb1Q',
    merchantName: 'Tech Express',
    merchantLogo: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBNqJa-Vratdlb3KqB02BRq5N1O8DL4JtGOxpIB2ndkIMOPVbjzZ7eVLJb3fAEdnAdWO9pVpBspT4K3j9B9X0xXzLS5zXY1aMqB2FyrnjZRDgJ0Y0tP_JTkBbDk6EgogZmH26Ro7EcJlBw3dKzkiPvkpGBjsZWlNEgiPr-QaC0-iVHGoYhV7ldlOWJgPwQImjSM0pBbS2TkUJXWSYUJB4jPqpqDoM9ArzwWlUL48cfJjx-9YPnaK0r-RqHguLaBOzytQ1wpxoQ5Ccw',
    merchantBorderClass: 'border-tertiary-fixed',
    title: 'Elite Wireless Audio',
    description: '40h battery life, active noise canceling, spatial audio.',
    price: 'R$ 299,00',
    likesCount: '2.4k',
  },
]
</script>

<template>
  <div class="bg-black text-on-surface h-screen overflow-hidden">
    <!-- TopAppBar -->
    <header class="fixed top-0 w-full z-50 flex justify-between items-center px-6 h-20 bg-transparent">
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-white text-2xl">search</span>
      </div>
      <h1 class="font-headline font-extrabold tracking-tighter text-white text-xl">Estalos</h1>
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-white text-2xl">shopping_cart</span>
      </div>
    </header>

    <!-- Main Feed Container -->
    <main class="h-full w-full overflow-y-scroll snap-y snap-mandatory scrollbar-hide">
      <PulseItem
        v-for="item in pulseItems"
        :key="item.id"
        :item="item"
      />
    </main>
    <HomeBottomNavBar />
</div>
</template>

<style>
.scrollbar-hide::-webkit-scrollbar { display: none; }
.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
</style>
