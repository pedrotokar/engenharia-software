"""Esse módulo contém a implementação dos adaptadores. Cada adaptador converte
o formato do instrumento de um determinado armazenamento para um formato comum,
em tuplas. Todos os adaptadores implementam um método `obter_dados` que retorna
uma lista com essas tuplas padronizadas. Dessa forma, um cliente pode usar
qualquer adaptador, que por sua vez estará ligado a diferentes fontes de dados."""

from loja import Loja, Baixo, TipoCaptacao
from abc import ABC, abstractmethod
from os.path import join
from glob import glob
import json

class CollectionAdapter(ABC):
    """Classe abstrata de adaptador que implementa o método que o cliente 
    (agregado/coleção) quer."""
    def __init__(self):
        pass
    
    @abstractmethod
    def obter_dados(self) -> list[tuple]:
        """Retorna uma lista de tuplas, cada tupla representando um instrumento."""
        pass
    
class ObjectAdapter(CollectionAdapter):
    """Essa classe implementa a interface de CollectionAdapter e por meio de uma
    associação simples, "traduz" as saídas da classe de loja para o formato das
    tuplas."""
    def __init__(self, loja):
        super().__init__()
        self._loja = loja

    #Aqui a tradução é efetivamente feita
    def obter_dados(self) -> list[tuple]:
        retorno = []
        for instrumento in self._loja.instrumentos:
            captacao = 0 if instrumento.captacao == TipoCaptacao.PASSIVA else 1
            tupla = (
                instrumento.marca,
                instrumento.modelo,
                float(instrumento.preco),
                instrumento.numero_cordas,
                captacao
            )
            retorno.append(tupla)
        return retorno

#Essa classe implementa a interface de CollectionAdapter e *aqui deveria ser uma
#associação mas estou economizando tempo* "traduz" as saídas de um objeto csv para
#essa interface
class CSVAdapter(CollectionAdapter):
    def __init__(self, arquivo):
        self._arquivo = arquivo

    def obter_dados(self) -> list[tuple]:
        retorno = []
        with open(self._arquivo, "r", encoding = "utf-8") as handler:
            next(handler)
            for linha in handler:
                campos = linha.split(",")
                campos[2] = float(campos[2])
                campos[3] = int(campos[3])
                campos[4] = int(campos[4])
                retorno.append(tuple(campos))
        return retorno

class APIAdapter(CollectionAdapter):
    def __init__(self, diretorio):
        self._diretorio = diretorio
    
    def obter_dados(self) -> list[tuple]:
        retorno = []
        for arquivo in glob(join(self._diretorio, "*.json")):
            with open(arquivo, "r", encoding = "utf-8") as handler:
                dicionario = json.load(handler)
            marca, modelo = dicionario["nome"].split(" - ")
            tupla = (
                marca,
                modelo,
                float(dicionario["valor"]),
                int(dicionario["n_cordas"]),
                0 if dicionario["tipo_captacao"] == "passiva" else 1
            )
            retorno.append(tupla)
        return retorno

if __name__ == "__main__":
    from pprint import pprint

    baixo_0 = Baixo("Tagima", "Woodstock TW-73", 1800)
    baixo_1 = Baixo("Fender", "American Ultra Precision", 15000)
    baixo_2 = Baixo("Ibanez", "BTB866SC", 9500, 6, TipoCaptacao.ATIVA)
    baixo_3 = Baixo("Music Man", "StingRay Special HH", 22000, 5, TipoCaptacao.ATIVA)
    baixo_4 = Baixo("Sire", "Marcus Miller V7", 4500, 5, TipoCaptacao.ATIVA)

    loja = Loja("nome")
    loja.adicionar_instrumento(baixo_0)
    loja.adicionar_instrumento(baixo_1)
    loja.adicionar_instrumento(baixo_2)
    loja.adicionar_instrumento(baixo_3)
    loja.adicionar_instrumento(baixo_4)

    adaptador_loja = ObjectAdapter(loja)
    pprint(adaptador_loja.obter_dados())

    adaptador_csv = CSVAdapter("data/baixos.csv")
    pprint(adaptador_csv.obter_dados())

    adaptador_api = APIAdapter(join("data", "api"))
    pprint(adaptador_api.obter_dados())
