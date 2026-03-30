from pydantic import BaseModel
from typing import List
from datetime import datetime

#1. A regra do que vai dentro da sacola
class itemPedido(BaseModel):
    id_produto: int
    quantidade: int
    preco: float #repare não pedimos o preço aqui! o python vai buscar o preço no banco depois!

#2 a regra do pedido final  (o pedido completo)
class Pedido(BaseModel):
    id_pedido: int
    id_cliente: int #quem pediu
    id_loja: int #de quem é a sacola
    produtos: List[itemPedido] #a lista de itens
    total: float #quanto deu no total
    status: str #status do pedido
    data: str    
        
#valores financeiros (Opcionais na criação, pois o Python vai calcular)
subtotal: float = 0.0
taxa_entrega: float = 0.0
total_pedido: float = 0.0


# A esteira de produção: pendente, preparando, a_caminho, entregue, cancelado

status:str = "pendente"
data_hora: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

