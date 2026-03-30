from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.produto import Produto
from models.loja import Loja

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
        capa="/assets/burguer_teste.jpg",
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

# 🚀 A Rota que o aplicativo de celular vai chamar
@app.get("/produtos")
def listar_produtos():
    return banco_de_produtos

@app.get("/lojas")
def listar_lojas():
    return banco_de_lojas

