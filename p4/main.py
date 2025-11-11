from funcoes import ConfigServiceSingleton, SQLiteFactory, PostgresFactory

#===============Questão 1===============
"""
Resposta do item 1 (a)

A alternativa 1 tem a vantagem de ser fácilmente utilizada sem a necessidade 
de implementar a lógica do singleton manualmente, já que a linguagem faz isso
pelo programador. Já na alternativa 2 e 3, é necessário que o programador 
implemente manualmente a lógica singleton, o que pode tomar tempo.

A alternativa 2 é a mais clara, já que não utiliza ferramentas específicas de 
Python e por isso pode ser facilmente interpretada por programadores de outra
linguagem. Ela também deixa claro que a classe se comporta como singleton em
qualquer ponto em que ela é recuperada. Já as alternativas 1 e 3 usam ferramentas
específicas de python e podem não deixar claro a existência da lógica singleton
em todos os pontos do código, o que é uma desvantagem.

Tanto a alternativa 2 quanto a 3 permitem a criação da instância de forma *lazy*, 
além da reinicialização dela, permitindo a realização de testes mais facilmente. 
Também evitam a poluição do espaço global de nomes, já que apenas o nome da classe 
já permite a recuperação da instância. A alternativa 1 dificulta os testes, já
que é necessário resetar o módulo importado, e a inicialização é feita no momento
do primeiro import, mas isso pode não ser claro para quem está lendo.

Por último, as alternativas 2 e 3 evitam a poluição do espaço global de nomes,
enquanto na alternativa 1 ele pode ser poluido a depender de como o import é feito
(`from modulo import *`).
 
A seguir se encontra o driver code do item (b)
"""
instancia = ConfigServiceSingleton()
print("Verificando se o construtor permite a criação de uma instância.")
print(instancia)
print(ConfigServiceSingleton._inst)

print("")

instancia = ConfigServiceSingleton.get_instance()
print("Criando uma instância pelo método de classe e verificando seu id.")
print(instancia, id(instancia))
print(id(ConfigServiceSingleton._inst))

print("")

instancia_2 = ConfigServiceSingleton.get_instance()
print("Chamando novamente o método e verificando o id do retorno e se é igual ao anterior.")
print(instancia_2, id(instancia_2))
print(id(ConfigServiceSingleton._inst))
print("Ids são iguais?", id(instancia) == id(instancia_2))

print("")

ConfigServiceSingleton._reset_for_tests()
instancia_3 = ConfigServiceSingleton.get_instance()
print("Testando se o reset de instâncias funcionou e uma nova instância foi criada.")
print(instancia_3, id(instancia_3))

print("")

#===============Questão 2===============
"""
Resposta do item 2 (a)

Um factory method é mais adequado para casos em que há diversas variações do
mesmo produto, e não há uma família de outros produtos para ser usada em conjunto
(ou há, mas não é necessário reforçar o uso de produtos da mesma família). 
A abstract factory é útil para agrupar diversos métodos de criação (ela é uma
coleção deles) e garantir que todos criarão produtos da mesma família.

O factory method é facilmente extendível, seja pela alteração do método original
para receber novos parâmetros ou pela criação de subclasses que extendam esse método
para aceitar novos tipos de produtos. A abstract factory é de fácil extensão quando
se deseja criar uma nova família, já que também bastará criar outra subclasse, mas
traz um problema quando se deseja criar um novo tipo de produto, já que todas as
subclasses deverão ser alteradas.

A abstract factory prioriza o desacoplamento, já que para trocar de família bastará
mudar qual subclasse é instanciada, preferencialmente em apenas um lugar do código.

A seguir se encontra o driver code do item (b)
"""

print("Criando fábrica de produtos da família postgres e testando suas saídas.")
factory = PostgresFactory()

repository = factory.create_repository()
print("Repository criado é do tipo", type(repository))
repository.start_connection("db12345@dbcluster:9999999")

print("")

cache_client = factory.create_cache_client()
print("Cache Client criado é do tipo", type(cache_client))
cache_client.add_to_cache("SELECT * FROM users;")

print("")
print("Criando fábrica de produtos da família SQLite e testando suas saídas.")
factory = SQLiteFactory()

repository = factory.create_repository()
print("Repository criado é do tipo", type(repository))
repository.start_connection("db12345@dbcluster:9999999")

print("")

cache_client = factory.create_cache_client()
print("Cache Client criado é do tipo", type(cache_client))
cache_client.add_to_cache("SELECT * FROM users;")

