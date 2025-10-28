from abc import ABC, abstractmethod

# Produto e dois produtos concretos

class Documento(ABC):
    def __init__(self, nome: str):
        self._nome = nome
    
    @property
    def nome(self) -> str:
        return self._nome

    def renomear(self, novo_nome: str) -> None:
        self._nome = novo_nome
        print("Arquivo renomeado")
    
    @abstractmethod
    def ler(self) -> None: ...

class DocumentoMac(Documento):
    def __init__(self, nome: str, usuario: str):
        super().__init__(nome)
        self._usuario = usuario

    def ler(self):
        print(f"Lendo documento no Mac do usuário {self._usuario}")

class DocumentoWindows(Documento):
    def __init__(self, nome: str, drive: str):
        super().__init__(nome)
        self._drive = drive

    def ler(self):
        print(f"Lendo documento no Windows no drive {self._drive}")

if __name__ == "__main__":
    documento_mac = DocumentoMac("atividade.py", "pedro")
    print(documento_mac.nome)
    documento_mac.ler()

    documento_windows = DocumentoWindows("atividade.py", "C:/")
    print(documento_windows.nome)
    documento_windows.ler()
