import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCarrinhoStore = defineStore('carrinho', () => {
  // 1. O Estado (A Mochila)
  const itens = ref([])

  // 2. Os Getters (As Calculadoras)
  const totalItens = computed(() => {
    return itens.value.reduce((total, item) => total + item.quantidade, 0)
  })

  // 3. As Actions (As Ações)
  const adicionarAoCarrinho = (produto) => {
    const itemExistente = itens.value.find((item) => item.id === produto.id)

    if (itemExistente) {
      // Se já existe, só soma +1
      itemExistente.quantidade += 1
    } else {
      // Se é novo, coloca na mochila com quantidade 1
      itens.value.push({ ...produto, quantidade: 1 })
    }
  }

  const removerDoCarrinho = (id_produto) => {
    itens.value = itens.value.filter((item) => item.id !== id_produto)
  }

  // 4. O que a loja devolve para o resto do app poder usar
  return {
    itens,
    totalItens,
    adicionarAoCarrinho,
    removerDoCarrinho
  }
})
