from pydantic import BaseModel

class Loja(BaseModel):
    id_loja: int
    nome: str
    categoria: str # Ex: "Hamburgueria", "Farmácia", "Eletrônicos"
    avaliacao: float
    tempo_medio_entrega: str
    taxa_entrega: float
    imagem_logo: str
    imagem_banner: str
    aberto: bool # O "interruptor" para o lojista fechar a loja no fim do dia