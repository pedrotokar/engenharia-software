"""Esse modulo contem implementacoes de classes que representam instrumentos
e lojas. Uma loja contem uma lista de objetos instrumento. Para o escopo da
atividade, esse é o objeto externo do domínio da aplicação."""

from enum import Enum

class TipoCaptacao(Enum):
    PASSIVA = 0
    ATIVA = 1

class Instrumento():
    def __init__(self, marca: str, modelo: str, preco: float, numero_cordas: int):
        self._marca = marca
        self._modelo = modelo
        self._preco = float(preco)
        self._len_cordas = numero_cordas

    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, marca: str):
        self._marca = marca

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, modelo: str):
        self._modelo = modelo

    @property
    def numero_cordas(self) -> int:
        return self._len_cordas

    @numero_cordas.setter
    def numero_cordas(self, numero_cordas: int):
        if numero_cordas < 1 or numero_cordas > 10 or not isinstance(numero_cordas, int):
            raise ValueError("Infelizmente não existem instrumentos com esse número de cordas")
        self._len_cordas = numero_cordas

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, preco: float):
        if preco <= 0 or not isinstance(preco, float):
            raise ValueError("Preço invalido para o instrumento")
        self._preco = preco

    def tocar(self, nota):
        raise NotImplementedError("Subclasse não implementou essse método.")

    def __repr__(self) -> str:
        return f"{self._marca} {self._modelo} com {self._len_cordas} cordas. Custando R${self._preco}."

    def __del__(self):
        print(f"deletando instrumento {self._marca} {self._modelo}")

class Baixo(Instrumento):
    def __init__(self, marca: str, modelo: str, preco: float, numero_cordas: int = 4, captacao: TipoCaptacao = TipoCaptacao.PASSIVA):
        super().__init__(marca, modelo, preco, numero_cordas)
        self._tipo_captacao = captacao

    @property
    def captacao(self) -> TipoCaptacao:
        return self._tipo_captacao

    def tocar(self, nota):
        print(f"Tocaram um {nota} muito grave num baixo {self._marca}.")

    def __repr__(self) -> str:
        return super().__repr__() + f" Captação {self._tipo_captacao.name}"

class Loja:
    def __init__(self, nome: str):
        self._nome = nome
        self._instrumentos = []
    
    @property
    def instrumentos(self) -> list[Instrumento]:
        return self._instrumentos

    def adicionar_instrumento(self, instrumento: Instrumento):
        self._instrumentos.append(instrumento)

    def __repr__(self) -> str:
        string = f"Loja {self._nome} com instrumentos: \n"
        for instrumento in self._instrumentos:
            string += str(instrumento) + "\n"
        return string

if __name__ == "__main__":
    baixo_0 = Baixo("Aria Pro II", "Magna Series", 500)
    baixo_1 = Baixo("Rickenbacker", "4003", 20000)
    baixo_2 = Baixo("Rickenbacker", "4003S", 1000)
    baixo_3 = Baixo("Aria Pro II", "SB-1000", 20000, captacao = TipoCaptacao.ATIVA)
    baixo_4 = Baixo("Giannini", "GB-205A Black", 2500, 5, TipoCaptacao.ATIVA)
    
    print("")
    baixo_0.tocar("do")
    baixo_1.tocar("re")
    baixo_2.tocar("mi")
    baixo_3.tocar("fa")
    baixo_4.tocar("sol")
    
    print("")
    print(baixo_0)
    print(baixo_1)
    print(baixo_2)
    print(baixo_3)
    print(baixo_4)

    print("")
    loja = Loja("nome")
    loja.adicionar_instrumento(baixo_0)
    loja.adicionar_instrumento(baixo_1)
    loja.adicionar_instrumento(baixo_2)
    loja.adicionar_instrumento(baixo_3)
    loja.adicionar_instrumento(baixo_4)
    print(loja)

