from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.produto import Produto

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
        imagem="url_da_imagem_burger.jpg",
        local="Bistro Pro",
        avaliacao=4.8,
        tempo_entrega="15-25 MIN",
        avaliacao_total=142,
        categoria="Lanches",
        capa="url_da_capa.jpg",
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