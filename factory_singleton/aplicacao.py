import fabrica_abstrata
import documentos

from abc import ABC, abstractmethod
from os import getenv

class Aplicacao(ABC):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Criando instância da aplicação")
            if getenv("SISTEMA") == "Windows":
                cls._instance = object.__new__(_AplicacaoWindows)
            else:
                cls._instance = object.__new__(_AplicacaoMac)
        else:
            print("Já havia uma instância")
        return cls._instance

    #Factory method padrão
    @abstractmethod
    def novo_documento(self, nome: str) -> documentos.Documento: ...

    #Factory method parametrizado
    def nova_fabrica(self, interface_grafica) -> fabrica_abstrata.FabricaAbstrata:
        if interface_grafica == "qt":
            return fabrica_abstrata.FabricaQt()
        elif interface_grafica == "gnome":
            return fabrica_abstrata.FabricaGTK()
        else:
            raise ValueError("Interface gráfica inválida")

#Essas subclasses são privadas e em teoria não devem ser usadas pelo cliente,
#já que trarão comportamentos inesperados (tentar instanciar uma aplicação de
#mac pode retornar uma de windows, por exemplo). Em python prefixar com _ é 
#a convenção para marcar como uso interno.

class _AplicacaoMac(Aplicacao):
    def novo_documento(self, nome: str):
        return documentos.DocumentoMac(nome, "admin")

class _AplicacaoWindows(Aplicacao):
    def novo_documento(self, nome: str):
        return documentos.DocumentoWindows(nome, "D:/")

if __name__ == "__main__":
    #Criando app e vendo se está de acordo com a variável de ambiente
    app = Aplicacao()
    print(type(app))

    #Testando método fábrica específico pro sistema, de acordo com a subclasse
    app.novo_documento("resposta.py").ler()

    print("")

    #Testando a tentativa de sobreescrever a instância
    app_2 = Aplicacao()
    print(app_2 == app)

    #Testando instanciar as subclasses para ver se continua havendo singleton
    app_3 = _AplicacaoWindows()
    print(type(app_3))
    app_4 = _AplicacaoMac()
    print(type(app_4))
    #Na prática um cliente não usaria isso!

    print("")

    #Testando fábricas abstratas
    fabrica_qt = app.nova_fabrica("qt")
    print(type(fabrica_qt))
    fabrica_qt.criar_cursor().desenhar((0, 0), "nenhuma")
    fabrica_qt.criar_janela().desenhar((0, 0))

    print("")

    fabrica_gtk = app.nova_fabrica("gnome")
    print(type(fabrica_gtk))
    fabrica_gtk.criar_cursor().desenhar((0, 0), "nenhuma")
    fabrica_gtk.criar_janela().desenhar((0, 0))

    print("")

    fabrica_invalida = app.nova_fabrica("libdwaita")
