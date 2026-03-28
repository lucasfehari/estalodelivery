from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int
    id_loja: int
    nome: str
    descricao: str
    preco: float
    imagem: str
    local: str
    avaliacao: float
    tempo_entrega: str
    avaliacao_total: int
    categoria: str
    capa: str
    promocao: bool
    preco_promocao: float
    precisa_retirada: bool
    precisa_preparo: bool
    disponivel: bool
    