from funcoes import (cache_resultados, cache_limitado, 
                     ServicoTextoA, ServicoTextoB, AdapterA, AdapterB)

# ===================== Questão 1
print("=" * 20 + "Questão 1" + "=" * 20)
print("")

print("Item a)")
# Funções decoradas com cache resultados.
@cache_resultados
def soma(a: int, b: int) -> int:
    return a + b

@cache_resultados
def multiplicacao(a: int, b: int) -> int:
    return a * b

# O seguinte print averigua o dicionário com as execuções salvas
print("Cache antes de fazer as execuções: ")
print(soma.__closure__[1].cell_contents)

# Executando a função para salvar resultados
print("")
soma(5, 5)
soma(9, 9)
soma(13, 13)
soma(42, 42)
soma(5, 5)
print("")

print("Cache após algumas execuções: ")
print(soma.__closure__[1].cell_contents)

print("")
print("Averiguando que o cache de soma não interfere em multiplicação:")
print(multiplicacao.__closure__[1].cell_contents)

multiplicacao(9, 9)
multiplicacao(9, 9)

print("Cache de multiplicação após execução:")
print(multiplicacao.__closure__[1].cell_contents)

print("")
print("Item b)")

# Funções decoradas com cache limitado, cada uma com seu limite próprio
@cache_limitado(2)
def subtracao(a: int, b: int) -> int:
    return a - b

@cache_limitado(3)
def divisao(a: int, b: int) -> float:
    return a / b

print("Averiguando cache de subtração antes de executar: ")
print(subtracao.__closure__[3].cell_contents)

print("")
subtracao(42, 10)
subtracao(42, 20)
subtracao(42, 30)
subtracao(42, 40)
subtracao(42, 40)
print("")

print("Averiguando se o cache de subtração está respeitando o limite:")
print(subtracao.__closure__[3].cell_contents)

print("")
print("Averiguando se o cache de divisão foi afetado:")
print(divisao.__closure__[3].cell_contents)

print("")
divisao(42, 1)
divisao(42, 2)
divisao(42, 7)
divisao(42, 21)
divisao(42, 21)
print("")

print("Averiguando se o cache de divisão respeita o limite diferente de subtração:")
print(divisao.__closure__[3].cell_contents)

print("")

# ===================== Questão 2
print("=" * 20 + "Questão 2" + "=" * 20)

def strip(entrada: str) -> str:
    return str.strip(entrada)

def upper(entrada: str) -> str:
    return str.upper(entrada)

# Criando instâncias dos adapters para demonstrar suas funcionalidades
a = AdapterA(ServicoTextoA(), pre=strip, pos=upper)
b = AdapterB(ServicoTextoB())

# Averiguando se a interface executar está corretamente implementada para o
# adaptador A
print("Testando interface executar do adaptador A")
print(a.executar(" ola professor Rafael Pinho "))
print(a.executar(None))
print(a.executar(1234567890))
print("")

# Averiguando se a interface executar está corretamente implementada para o
# adaptador B
print("Testando interface executar do adaptador B")
print(b.executar("Eu adoro a EMAp."))
print(b.executar(None))
print(b.executar(1234567890))

