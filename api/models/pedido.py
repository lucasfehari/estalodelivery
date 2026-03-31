from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

#1. A regra do que vai dentro da sacola
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
        
    #valores financeiros (Opcionais na criação, pois o Python vai calcular)
    subtotal: float = 0.0
    taxa_entrega: float = 0.0
    total_pedido: float = 0.0
    data_hora: Optional[datetime] = None

