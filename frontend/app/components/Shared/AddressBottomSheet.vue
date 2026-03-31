<script setup lang="ts">
import { useAddress } from '~/composables/useAddress'

const {
  isAddressSheetOpen,
  isNewAddressForm,
  savedAddresses,
  enderecoSelecionado,
  novoEndereco,
  closeAddressSheet,
  selectAddress,
  saveNewAddress
} = useAddress()
</script>

<template>
  <!-- Bottom Sheet Modal para Endereço -->
  <div v-if="isAddressSheetOpen" class="fixed inset-0 z-[100] flex flex-col justify-end">
    <!-- Backdrop Escurecido -->
    <div class="absolute inset-0 bg-black/40 backdrop-blur-sm transition-opacity" @click="closeAddressSheet"></div>
    
    <!-- Gaveta -->
    <div class="relative bg-surface-container-lowest w-full max-w-md mx-auto rounded-t-[2rem] pt-3 pb-8 px-6 shadow-2xl animate-in slide-in-from-bottom duration-300">
      <!-- Puxador (Handle) -->
      <div class="w-12 h-1.5 bg-gray-300 rounded-full mx-auto mb-6"></div>
      
      <div class="flex justify-between items-center mb-6">
        <h2 class="font-headline font-extrabold text-xl text-on-surface text-primary">Detalhes de Entrega</h2>
        <button @click="closeAddressSheet" class="p-2 rounded-full hover:bg-surface-container transition-colors">
          <span class="material-symbols-outlined text-sm text-on-surface-variant cursor-pointer">close</span>
        </button>
      </div>

      <!-- Conteúdo: Lista de Endereços -->
      <div v-show="!isNewAddressForm" class="space-y-4 max-h-[60vh] overflow-y-auto hide-scrollbar">
        <div 
          v-for="addr in savedAddresses" :key="addr.id"
          @click="selectAddress(addr)"
          class="flex items-start gap-4 p-4 rounded-xl border-2 transition-all cursor-pointer"
          :class="enderecoSelecionado?.id === addr.id ? 'border-primary bg-primary/5' : 'border-gray-100 bg-white hover:border-gray-200'"
        >
          <span class="material-symbols-outlined text-primary mt-1" v-if="addr.descricao === 'Casa'">home</span>
          <span class="material-symbols-outlined text-primary mt-1" v-else-if="addr.descricao === 'Trabalho'">work</span>
          <span class="material-symbols-outlined text-primary mt-1" v-else>location_on</span>
          
          <div class="flex flex-col">
            <span class="font-bold text-sm text-on-surface">{{ addr.descricao }}</span>
            <span class="text-xs text-on-surface-variant mt-1">{{ addr.rua }}, {{ addr.numero }}</span>
            <span class="text-xs text-on-surface-variant" v-if="addr.complemento">{{ addr.complemento }}</span>
          </div>
          
          <span class="material-symbols-outlined text-primary ml-auto" v-if="enderecoSelecionado?.id === addr.id">check_circle</span>
        </div>

        <button @click="isNewAddressForm = true" class="w-full py-4 mt-2 border-2 border-dashed border-primary/40 rounded-xl text-primary font-bold flex items-center justify-center gap-2 hover:bg-primary/5 transition-colors cursor-pointer">
          <span class="material-symbols-outlined">add</span>
          Cadastrar Novo Endereço
        </button>
      </div>

      <!-- Conteúdo: Novo Endereço Form -->
      <div v-show="isNewAddressForm" class="max-h-[65vh] overflow-y-auto hide-scrollbar pb-6 space-y-4 animate-in slide-in-from-right-8 duration-300">
        <button @click="isNewAddressForm = false" class="text-primary text-sm font-bold flex items-center gap-1 mb-2 hover:opacity-80 cursor-pointer">
           <span class="material-symbols-outlined text-sm">arrow_back</span> Voltar
        </button>

        <div class="grid grid-cols-1 gap-4">
          <div>
             <label class="text-xs font-bold text-gray-500 mb-1 block">Nome do Local (Ex: Casa, Escritório)</label>
             <input v-model="novoEndereco.descricao" type="text" placeholder="Apelido..." class="w-full bg-gray-100 border-none rounded-xl py-3 px-4 focus:ring-2 focus:ring-primary outline-none">
          </div>
          <div class="grid grid-cols-[2fr_1fr] gap-3">
            <div>
               <label class="text-xs font-bold text-gray-500 mb-1 block">Rua</label>
               <input v-model="novoEndereco.rua" type="text" placeholder="Nome da rua" class="w-full bg-gray-100 border-none rounded-xl py-3 px-4 focus:ring-2 focus:ring-primary outline-none">
            </div>
            <div>
               <label class="text-xs font-bold text-gray-500 mb-1 block">Número</label>
               <input v-model="novoEndereco.numero" type="number" placeholder="123" class="w-full bg-gray-100 border-none rounded-xl py-3 px-4 focus:ring-2 focus:ring-primary outline-none">
            </div>
          </div>
          <div class="grid grid-cols-[1fr_2fr] gap-3">
            <div>
               <label class="text-xs font-bold text-gray-500 mb-1 block">Bairro</label>
               <input v-model="novoEndereco.bairro" type="text" placeholder="Ex: Centro" class="w-full bg-gray-100 border-none rounded-xl py-3 px-4 focus:ring-2 focus:ring-primary outline-none">
            </div>
            <div>
               <label class="text-xs font-bold text-gray-500 mb-1 block">Complemento</label>
               <input v-model="novoEndereco.complemento" type="text" placeholder="Apto, Bloco..." class="w-full bg-gray-100 border-none rounded-xl py-3 px-4 focus:ring-2 focus:ring-primary outline-none">
            </div>
          </div>
        </div>
        
        <button @click="saveNewAddress" class="w-full mt-6 py-4 bg-primary text-white font-extrabold rounded-xl shadow-lg shadow-primary/20 active:scale-95 transition-all cursor-pointer">
          Salvar Endereço
        </button>
      </div>
    </div>
  </div>
</template>
