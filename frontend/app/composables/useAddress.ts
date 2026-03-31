// frontend/app/composables/useAddress.ts
import { useState } from '#imports'

export const useAddress = () => {
  // Estado global para controlar se a gaveta está aberta ou não
  const isAddressSheetOpen = useState<boolean>('isAddressSheetOpen', () => false)
  
  // Estado para controlar qual aba da gaveta está visível (Lista vs Novo)
  const isNewAddressForm = useState<boolean>('isNewAddressForm', () => false)

  // Lista mockada de endereços (poderia vir de uma API no futuro)
  const savedAddresses = useState('savedAddresses', () => [
    {
      id: 1,
      descricao: "Casa",
      rua: "Rua das Flores", // Valor default do template antigo
      numero: "123",
      bairro: "Centro",
      cidade: "São Paulo",
      estado: "SP",
      cep: "01000-000",
      complemento: "Apto 42"
    },
    {
      id: 2,
      descricao: "Trabalho",
      rua: "Avenida Paulista",
      numero: "1000",
      bairro: "Bela Vista",
      cidade: "São Paulo",
      estado: "SP",
      cep: "01310-100",
      complemento: "Andar 15"
    }
  ])

  // Endereço selecionado (inicia sempre com o primeiro)
  const enderecoSelecionado = useState<any>('enderecoSelecionado', () => savedAddresses.value[0] || null)

  // Modelo reativo para o novo formulário
  const novoEndereco = useState('novoEndereco', () => ({
    descricao: "",
    rua: "",
    numero: "",
    bairro: "",
    complemento: "",
    cidade: "São Paulo", // Default MVP
    estado: "SP",        // Default MVP
    cep: ""
  }))

  // Ações globais (Métodos)
  const selectAddress = (addr: any) => {
    enderecoSelecionado.value = addr
    isAddressSheetOpen.value = false
  }

  const saveNewAddress = () => {
    if (!novoEndereco.value.rua || !novoEndereco.value.numero) {
      alert("Preencha Rua e Número.")
      return
    }
    
    const newId = savedAddresses.value.length + 1
    const addressToSave = { ...novoEndereco.value, id: newId }
    
    if (!addressToSave.descricao) addressToSave.descricao = "Outro"

    savedAddresses.value.push(addressToSave)
    selectAddress(addressToSave)
    isNewAddressForm.value = false
    
    // Limpar o formulário para o próximo uso
    novoEndereco.value = {
      descricao: "", rua: "", numero: "", bairro: "", 
      complemento: "", cidade: "São Paulo", estado: "SP", cep: ""
    }
  }

  const openAddressSheet = () => {
    isAddressSheetOpen.value = true
  }

  const closeAddressSheet = () => {
    isAddressSheetOpen.value = false
    isNewAddressForm.value = false // Sempre que fechar, resetar a aba para a lista
  }

  return {
    isAddressSheetOpen,
    isNewAddressForm,
    savedAddresses,
    enderecoSelecionado,
    novoEndereco,
    openAddressSheet,
    closeAddressSheet,
    selectAddress,
    saveNewAddress
  }
}
