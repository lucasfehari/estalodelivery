from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.produto import Produto
from models.loja import Loja
from datetime import datetime
from models.pedido import Pedido, itemPedido

app = FastAPI(title="API do Estalo")

# 🛡️ O Escudo CORS: Permite que o Nuxt (Front) converse com o Python (Back)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Na vida real colocamos o domínio do site, aqui liberamos tudo para teste
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 Nosso Banco de Dados Falso (Em memória)
banco_de_produtos = [
    Produto(
        id_produto=1,
        id_loja=101,
        nome="Classic Burger",
        descricao="Pão brioche, blend 180g, queijo cheddar e bacon.",
        preco=29.90,
        imagem="/assets/burguer_teste.jpg",
        local="Bistro Pro",
        avaliacao=4.8,
        tempo_entrega="15-25 MIN",
        avaliacao_total=142,
        categoria="Lanches",
        capa="../../assets/burguer_teste.jpg",
        promocao=True,
        preco_promocao=19.90,
        precisa_retirada=False,
        precisa_preparo=True,
        disponivel=True

    ),
    Produto(
        id_produto=2,
        id_loja=102,
        nome="Gold Burger",
        descricao="Pão brioche, blend 180g, queijo cheddar e bacon.",
        preco=29.90,
        imagem="/assets/burguer_teste.jpg",
        local="Bistro Pro",
        avaliacao=4.8,
        tempo_entrega="15-25 MIN",
        avaliacao_total=142,
        categoria="Lanches",
        capa="/assets/burguer_teste.jpg",
        promocao=True,
        preco_promocao=19.90,
        precisa_retirada=False,
        precisa_preparo=True,
        disponivel=True

    ),
    Produto(
        id_produto=3,
        id_loja=103,
        nome="Gold Burger",
        descricao="Pão brioche, blend 180g, queijo cheddar e bacon.",
        preco=29.90,
        imagem="/assets/burguer_teste.jpg",
        local="Bistro Pro",
        avaliacao=4.8,
        tempo_entrega="15-25 MIN",
        avaliacao_total=142,
        categoria="Lanches",
        capa="/assets/burguer_teste.jpg",
        promocao=True,
        preco_promocao=19.90,
        precisa_retirada=False,
        precisa_preparo=True,
        disponivel=True

    )
]

# 🏬 Banco de Lojas
banco_de_lojas = [
    Loja(
        id_loja=101,
        nome="Bistro Pro",
        categoria="Hamburgueria",
        avaliacao=4.8,
        tempo_medio_entrega="20-30 MIN",
        taxa_entrega=5.90,
        imagem_logo="/assets/logo_bistro.png",
        imagem_banner="/assets/banner_bistro.jpg",
        aberto=True
    ),
    Loja(
        id_loja=102,
        nome="Burguer King",
        categoria="Lanches",
        avaliacao=4.5,
        tempo_medio_entrega="15-25 MIN",
        taxa_entrega=4.50,
        imagem_logo="/assets/logo_bk.png",
        imagem_banner="/assets/banner_bk.jpg",
        aberto=True
    ),
    Loja(
        id_loja=103,
        nome="Mc Donalds",
        categoria="Fast Food",
        avaliacao=4.2,
        tempo_medio_entrega="10-20 MIN",
        taxa_entrega=3.50,
        imagem_logo="/assets/logo_mc.png",
        imagem_banner="/assets/banner_mc.jpg",
        aberto=True
    )
]

# 🚀 A Rota que o aplicativo de celular vai chamar
@app.get("/produtos")
def listar_produtos():
    return banco_de_produtos

@app.get("/lojas")
def listar_lojas():
    return banco_de_lojas

#cofre de vendas em memoria
banco_de_pedidos = []

@app.post("/pedidos")
def criar_pedido(novo_pedido: Pedido):
    subtotal_calculado = 0.0

    # 1. O Python lê cada item que o cliente quer comprar
    for itemPedido in novo_pedido.itens:
        # 2. Vai procurar o PREÇO REAL no nosso cofre de produtos
        for produto in banco_de_produtos:
            if produto.id_produto == itemPedido.id_produto:
                # 3. Faz a matemática: Preço do Lanche x Quantidade
                subtotal_calculado += produto.preco * itemPedido.quantidade

    # 4. Descobre a taxa de entrega da loja escolhida
    taxa = 0.0
    for loja in banco_de_lojas:
        if loja.id_loja == novo_pedido.id_loja:
            taxa = loja.taxa_entrega
  
    # 5. Preenche o recibo final (impedido de ser hackeado)
    novo_pedido.subtotal = round(subtotal_calculado, 2)
    novo_pedido.taxa_entrega = taxa
    novo_pedido.total_pedido = round(subtotal_calculado + taxa, 2)

    # 5.5. Regra de Negócio: Segurança financeira do caixa
    # Se o cliente pediu troco, o valor do troco NÃO PODE ser menor que a conta!
    if novo_pedido.forma_pagamento == 'DINHEIRO' and novo_pedido.troco_para is not None:
        if novo_pedido.troco_para < novo_pedido.total_pedido:
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail="O valor do troco não pode ser menor que o total do pedido.")

    # 6. Carimba a hora exata da compra e guarda no cofre
    novo_pedido.data_hora = datetime.now()
    banco_de_pedidos.append(novo_pedido)
    
    return {
        "mensagem": "Estalo feito! O seu pedido está a ser preparado.", 
        "recibo": novo_pedido
    }

