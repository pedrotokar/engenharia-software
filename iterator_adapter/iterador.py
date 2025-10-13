"""Esse módulo contém a implementação da coleção de instrumentos e do iterador
que funciona nela. Nesse arquivo poderiam ser adicionados mais iteradores para
percorrer a coleção/agregado de outra maneira."""

from adaptador import AdaptadorInstrumento, AdaptadorCSV, AdaptadorAPI, AdaptadorObjeto

class ColecaoInstrumentos:
    def __init__(self, *adaptadores: AdaptadorInstrumento):
        self._adaptadores = list(adaptadores)
        self._numero_modificacoes = 0

    @property
    def adaptadores(self) -> list[AdaptadorInstrumento]:
        return self._adaptadores

    @property
    def contador_modificacoes(self) -> int:
        return self._numero_modificacoes

    def adicionar_adaptador(self, adaptador: AdaptadorInstrumento):
        """Recebe um adaptador de instrumentos e adiciona na coleção"""
        self._adaptadores.append(adaptador)
        self._numero_modificacoes += 1
    
    def __repr__(self) -> str:
        return f"Coleção com {len(self._adaptadores)} adaptadores."

    def __iter__(self) -> "IteradorInstrumentos":
        return IteradorInstrumentos(self)

class IteradorInstrumentos:
    def __init__(self, colecao: ColecaoInstrumentos):
        self._colecao = colecao
        self._contador_modificacoes_fixo = colecao.contador_modificacoes
        self._items = []
        for adaptador in self._colecao.adaptadores:
            self._items.extend(adaptador.obter_dados())
        self._current_index = 0

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> "IteradorInstrumentos":
        return self

    def __next__(self) -> tuple:
        if self._contador_modificacoes_fixo != self._colecao.contador_modificacoes:
            raise RuntimeError("Coleção foi alterada, iterador não serve mais!")
        if self._current_index == len(self):
            raise StopIteration
        self._current_index += 1
        return self._items[self._current_index - 1]

#Aqui eu poderia definir mais iteradores que fazem alguma coisa diferente pra
#percorrer a coleção.

if __name__ == "__main__":
    from pprint import pprint
    from os.path import join
    adaptador_csv = AdaptadorCSV("data/baixos.csv")
    adaptador_api = AdaptadorAPI(join("data", "api"))

    colecao = ColecaoInstrumentos(adaptador_api, adaptador_csv)
    pprint(colecao)

    for instrumento in colecao:
        print(instrumento)
    
    print("")
    iterador = iter(colecao)
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))

    print("")
    colecao_parcial = ColecaoInstrumentos(adaptador_csv)
    iterador_parcial = iter(colecao_parcial)
    print(next(iterador_parcial))
    print(next(iterador_parcial))
    colecao_parcial.adicionar_adaptador(adaptador_api)
    print(next(iterador_parcial))
