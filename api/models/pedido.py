from pydantic import BaseModel, model_validator
from typing import List, Optional
from datetime import datetime

# Estrutura do Endereço de Entrega
class Endereco(BaseModel):
    rua: str
    numero: str
    bairro: str
    complemento: Optional[str] = ""
    cidade: str = ""       # Opcional para MVP, focando local
    estado: str = ""       # Opcional
    cep: Optional[str] = ""

# 1. A regra do que vai dentro da sacola
class itemPedido(BaseModel):
    id_produto: int
    quantidade: int
    preco: float = 0.0 # Opcional, pois o Python recalcula no servidor

#2 a regra do pedido final  (o pedido completo)
class Pedido(BaseModel):
    id_pedido: int
    id_cliente: int #quem pediu
    id_loja: int #de quem é a sacola
    itens: List[itemPedido] #a lista de itens (renomeado de 'produtos' para bater com o main.py)
    total: float = 0.0 # Opcional, o Python calcula
    status: str = "pendente" # A esteira de produção: pendente, preparando, a_caminho, entregue, cancelado
    data: str = "" # Opcional
    forma_pagamento: str = "" # PIX, CARTAO, DINHEIRO
    troco_para: Optional[float] = None
    endereco_entrega: Optional[Endereco] = None

    #valores financeiros (Opcionais na criação, pois o Python vai calcular)
    subtotal: float = 0.0
    taxa_entrega: float = 0.0
    total_pedido: float = 0.0
    data_hora: Optional[datetime] = None

    @model_validator(mode='after')
    def validar_troco(self):
        # Regra de negócio: Se não for dinheiro, não faz sentido ter "troco para"
        if self.forma_pagamento != 'DINHEIRO':
            self.troco_para = None
        
        # Opcional: Impedir troco menor que o valor do pedido
        # (Faremos essa conta completa na rota, mas aqui já garantimos a estrutura de dados)
        return self


