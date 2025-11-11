from functools import wraps
from abc import ABC, abstractmethod

# Questão 1

def cache_resultados(func):
    """Decora uma função, adicionando a ela capacidades de cache.
    Isso significa que os resultados das chamadas serão salvos de acordo
    com os argumentos posicionais passados para a função, de forma que
    ela não precise ser executada duas vezes com os mesmos argumentos.
    """
    resultados_salvos = dict() # Dicionario para salvar as saídas
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in resultados_salvos.keys(): # Verifica se os argumentos foram registrados
            print(f"=> Chamada de {func.__name__} com argumentos {args} retirada do cache, sem recalcular")
            return resultados_salvos[args]
        else:
            print(f"=> Chamada de {func.__name__} com argumentos {args} salva no cache")
            resultado = func(*args)
            resultados_salvos[args] = resultado
            return resultado

    return wrapper

def cache_limitado(max_tamanho: int):
    """Decora uma função, adicionando a ela capacidades de cache, com um limite
    para o número de resultados salvos da função.
    Isso significa que os resultados das chamadas serão salvos de acordo
    com os argumentos posicionais passados para a função, de forma que
    ela não precise ser executada duas vezes com os mesmos argumentos.
    Caso o limite de resultados seja atingido, o registro mais antigo será
    removido do cache.

    Parameters
    ----------
    max_tamanho: int
        O número máximo de registros a se manter.
    """

    def cache_resultados(func):
        resultados_salvos = dict()
        numero_registros = 0 # Contador de resultados salvos
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args in resultados_salvos.keys():
                print(f"=> Chamada de {func.__name__} com argumentos {args} retirada do cache, sem recalcular")
                return resultados_salvos[args]
            else:
                resultado = func(*args)
                resultados_salvos[args] = resultado

                # Acessa com nonlocal para poder alterar a variável
                nonlocal numero_registros 
                if numero_registros == max_tamanho:
                    # Obtém o primeiro registro e remove ele. Os dicionários em python
                    # A partir de certa versão lembram da ordem de adição de chaves
                    print(f"=> Chamada de {func.__name__} com argumentos {args} salva no cache. Um registro antigo foi apagado.")
                    primeiro_registro = list(resultados_salvos.keys())[0]
                    resultados_salvos.pop(primeiro_registro)
                else:
                    print(f"=> Chamada de {func.__name__} com argumentos {args} salva no cache")
                    numero_registros += 1
                
                return resultado

        return wrapper
    return cache_resultados


# Questão 2

# Funções fornecidas pelo enunciado
class ServicoTextoA:
    """Serviço de texto que adiciona conteúdo a textos."""
    def processar(self, texto: str) -> str:
        return f"[A]{texto}"

class ServicoTextoB:
    """Serviço de texto que inverte textos."""
    def run(self, payload: dict) -> dict:
        data = payload.get("data", "")
        return {"resultado": str(data)[::-1]}

# Contrato/interface esperado pelo cliente
class Executavel(ABC):
    """Classe abstrada que especifica a interface `executar`.
    Subclasses deverão implementar essa interface."""

    @abstractmethod
    def executar(self, entrada: str) -> str:
        pass

class AdapterA(Executavel):
    """Classe que adapta as funcionalidades de `ServicoTextoA` para funcionarem
    com a interface/contrato `Executavel`."""
    def __init__(self, servico_a: ServicoTextoA, pre = None, pos = None):
        """Inicializa a classe.
        
        Parameters
        ----------
        servico_a: ServicoTextoA
            Uma instância de ServicoTextoA, cujas funcionalidades serão utilizadas.
        pre: function
            Uma função de pré-processamento para as entradas do método `executar`.
        pos:
            Uma função de pós-processamento para as saídas do método `executar`.
        """
        self._adaptee = servico_a
        self._pre = pre
        self._pos = pos
    
    def executar(self, entrada: str) -> str:
        """Executa as operações definidas pelo ServicoTextoA com a interface
        `executar`. Aplica pré e pós processamento, se tiverem sido definidos
        na criação da instância.
        
        Parameters
        ----------
        entrada: str
            String para ser processada
        
        Returns
        -------
        str: String processada pelo ServicoTextoA.
        """
        # Aplicando tratamento do tipo da entrada
        if entrada is None:
            entrada = ""
        elif not isinstance(entrada, str):
            entrada = str(entrada)

        # Aplicando pré processamento
        if callable(self._pre):
            entrada_normalizada = self._pre(entrada)
        else:
            entrada_normalizada = entrada
        
        # Usando a funcionalidade provida por ServicoTextoA
        saida = self._adaptee.processar(entrada_normalizada)

        # Aplicando pós processamento
        if callable(self._pos):
            return self._pos(saida)
        else:
            return saida

class AdapterB(Executavel):
    """Classe que adapta as funcionalidades de `ServicoTextoB` para funcionarem
    com a interface/contrato `Executavel`."""
    def __init__(self, servico_b: ServicoTextoB, pre = None, pos = None):
        """Inicializa a classe.
        
        Parameters
        ----------
        servico_b: ServicoTextoB
            Uma instância de ServicoTextoA, cujas funcionalidades serão utilizadas.
        pre: function
            Uma função de pré-processamento para as entradas do método `executar`.
        pos:
            Uma função de pós-processamento para as saídas do método `executar`.
        """
        self._adaptee = servico_b
        self._pre = pre
        self._pos = pos
    
    def executar(self, entrada: str) -> str:
        """Executa as operações definidas pelo ServicoTextoB com a interface
        `executar`. Aplica pré e pós processamento, se tiverem sido definidos
        na criação da instância.
        
        Parameters
        ----------
        entrada: str
            String para ser processada
        
        Returns
        -------
        str: String processada pelo ServicoTextoB.
        """

        # Aplicando tratamento do tipo da entrada
        if entrada is None:
            entrada = ""
        elif not isinstance(entrada, str):
            entrada = str(entrada)

        # Aplicando pré processamento
        if callable(self._pre):
            entrada_normalizada = self._pre(entrada)
        else:
            entrada_normalizada = entrada
        
        # Adaptando o input e usando a funcionalidade provida por ServicoTextoB
        dict_entrada = {"data": entrada_normalizada}
        saida = self._adaptee.run(dict_entrada)

        # Tratando saída do serviço
        if not isinstance(saida, dict):
            return ""
        elif "resultado" not in saida.keys():
            return ""
        elif not isinstance(saida["resultado"], str):
            return ""

        # Aplicando pós processamento
        if callable(self._pos):
            return self._pos(saida["resultado"])
        else:
            return saida["resultado"]
