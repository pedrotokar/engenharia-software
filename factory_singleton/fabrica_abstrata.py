import interface

from abc import ABC, abstractmethod

#Classe abstrata que define a interface que as fábricas de produtos deverão
#implementar. Cada fábrica concreta implementa esses métodos pensando em uma
#família de produtos que trabalharão melhor entre si do que com produtos de 
#outras famílias. Por isso é uma fabrica abstrata e não uma fábrica pra cada
#produto!
class FabricaAbstrata(ABC):
    @abstractmethod
    def criar_cursor(self) -> interface.Cursor: ...

    @abstractmethod
    def criar_janela(self) -> interface.Janela: ...

class FabricaQt(FabricaAbstrata):
    def criar_cursor(self) -> interface.CursorQt:
        print("Crianco cursor específico para Qt")
        return interface.CursorQt()
    
    def criar_janela(self) -> interface.JanelaQt:
        print("Crianco janela específica para Qt")
        return interface.JanelaQt()

class FabricaGTK(FabricaAbstrata):
    def criar_cursor(self) -> interface.CursorGTK:
        print("Crianco cursor específico para GTK")
        return interface.CursorGTK()
    
    def criar_janela(self) -> interface.JanelaGTK:
        print("Crianco janela específica para GTK")
        return interface.JanelaGTK()

if __name__ == "__main__":
    fabrica_qt = FabricaQt()

    janela_1 = fabrica_qt.criar_janela()
    janela_1.desenhar((0, 0))
    janela_1.mover((0, 0), (1, 1))

    cursor_1 = fabrica_qt.criar_cursor()
    cursor_1.desenhar((0, 0), "clicavel")

    fabrica_gtk = FabricaGTK()

    janela_2 = fabrica_gtk.criar_janela()
    janela_2.desenhar((0, 0))
    janela_2.mover((0, 0), (1, 1))

    cursor_2 = fabrica_gtk.criar_cursor()
    cursor_2.desenhar((0, 0), "arrastavel")
