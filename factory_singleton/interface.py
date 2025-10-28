from abc import ABC, abstractmethod

#Produtos: janela e cursor. Definem a interface que janelas e cursores terão
#no geral, sem se preocupar com a interface gráfica.

class Janela(ABC):
    @abstractmethod
    def mover(self, posicao_antiga: tuple, posicao_nova: tuple) -> None: ...
    
    def desenhar(self, posicao: tuple) -> None:
        pass

class Cursor(ABC):
    @abstractmethod
    def desenhar(self, posicao: tuple, tipo_interacao: str) -> None: ...

#Produtos concretos para Qt. Essas implementações são só para exemplificar
#como funciona o padrão, e na prática não estão fazendo nada nem funcionam.

class JanelaQt(Janela):
    def mover(self, posicao_antiga, posicao_nova):
        # estado = mover_a_janela_qt(posicao_antiga, posicao_nova)
        # self.estado = estado
        print("Janela movida no Qt")
    
    def desenhar(self, posicao):
        # desenhar_a_janela_qt(posicao)
        print("Janela desenhada no Qt")

class CursorQt(ABC):
    def desenhar(self, posicao, tipo_interacao):
        # self.cursor_atual = tipo_interacao
        # desenhar_o_cursor_qt(posicao, tipo_interacao)
        print("Cursor desenhado no Qt")

#Produtos concretos para GTK. Mesma coisa aqui.

class JanelaGTK(Janela):
    def mover(self, posicao_antiga, posicao_nova):
        # estado = mover_a_janela_gtk(posicao_antiga, posicao_nova)
        # self.estado = estado
        print("Janela movida no GTK")
    
    def desenhar(self, posicao):
        # desenhar_a_janela_gtk(posicao)
        print("Janela desenhada no GTK")

class CursorGTK(ABC):
    def desenhar(self, posicao, tipo_interacao):
        # self.cursor_atual = tipo_interacao
        # desenhar_o_cursor_gtk(posicao, tipo_interacao)
        print("Cursor desenhado no GTK")

if __name__ == "__main__":
    cursor_1 = CursorQt()
    cursor_1.desenhar((0, 0), "clicavel")

    cursor_2 = CursorGTK()
    cursor_2.desenhar((0, 0), "clicavel")

    janela_1 = JanelaQt()
    janela_1.desenhar((0, 0))
    janela_1.mover((0, 0), (1, 1))

    janela_2 = JanelaGTK()
    janela_2.desenhar((0, 0))
    janela_2.mover((0, 0), (1, 1))
