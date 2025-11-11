from abc import ABC, abstractmethod
from datetime import datetime

# O próprio python irá tratar o histórico como singleton, então só existirá um.
# Dependendo da aplicação, faria sentido ter mais de um histórico. Nesse exemplo,
# apenas um deve existir, e por isso o comportamento de singleton é desejado.
history = []

#--- Padrão chain of responsability

class Handler(ABC):
    """Classe abstrata que representa um elemento da cadeia de responsabilidades.
    Todas as classes que implementarem a interface handle devem ser capazes de
    tratar pelo menos um tipo de requisição."""

    def __init__(self, successor: "Handler" = None) -> None:
        """Inicializa o handler, com a opção de adicionar um sucessor.
        
        Parameters
        ----------
        successor: Handler
            Qual o próximo handler da cadeia."""
        self.successor = successor
    
    @abstractmethod
    def handle(self, request: str) -> str:
        """Método usado pelo cliente para passar uma requisição para a
        cadeia. A implementação padrão passa a requisição para frente, e
        pode ser usada por subclasses para quando elas não puderem tratar
        uma requisição.
        
        Parameters
        ----------
        request: str
            O tipo de requisição sendo tratada.
        
        Returns
        -------
        str: o resultado do tratamento"""

        if self.successor:
            return self.successor.handle(request)
        else:
            return f"Não foi possível tratar a solicitação {request}."
    
class ValidationHandler(Handler):
    """Handler que sabe tratar requisições de validação."""

    def handle(self, request: str) -> str:
        """Se a requisição for de validação, trata ela, caso contrário
        passa para o próximo item da cadeia.
        
        Parameters
        ----------
        request: str
            O tipo de requisição sendo tratada.
        
        Returns
        -------
        str: o resultado do tratamento"""

        if request == "[validation]":
            return "Tratei requisição do tipo validation"
        else:
            return super().handle(request)

class ExecutionHandler(Handler):
    """Handler que sabe tratar requisições de execução."""

    def handle(self, request: str) -> str:
        """Se a requisição for de execução, trata ela, caso contrário
        passa para o próximo item da cadeia.
        
        Parameters
        ----------
        request: str
            O tipo de requisição sendo tratada.
        
        Returns
        -------
        str: o resultado do tratamento"""
        
        if request == "[execution]":
            return "Tratei requisição do tipo execution"
        else:
            return super().handle(request)


#--- Padrão command

class TaskCommand():
    """Classe que representa um comando do sistema. Uma instância dessa classe
    terá como parâmetro o tipo de requisição que fará para a cadeia de responsabilidades 
    e uma referência para o inicio dela, que poderá ter passos que tratem o tipo de
    requisição associada ao comando."""
    def __init__(self, handler_name: str, chain_start: Handler) -> None:
        """Inicializa o comando, com sua requisição e uma referência pra cadeia
        de responsabilidades
        
        Parameters
        ----------
        handler_name: str
            O tipo de requisição que o comando fará para a cadeia.
        chain_start: Handler
            O início da cadeia que poderá tratar requisições do comando.
        """
        self.chain_start = chain_start
        self.handler_name = handler_name
        self._timestamp = None
        self._result = None

    # O encapsulamento previne que essas informações sejam modificadas no log.
    @property
    def result(self) -> str:
        """Resultado de um comando já executado"""
        return self._result

    @property    
    def timestamp(self) -> datetime:
        """Timestamp de um comando já executado"""
        return self._timestamp

    def execute(self):
        """Executa a requisição associada ao comando e salva no log uma cópia
        que contém as informações e resultados da execução."""
        # Terceiriza para a cadeia a execução do comando
        result = self.chain_start.handle(self.handler_name)

        # Armazena o estado da execução e salva em uma cópia, para mandar pro histórico
        copy = TaskCommand(self.handler_name, self.chain_start)
        copy._timestamp = datetime.now()
        copy._result = result
        history.append(copy)
    


