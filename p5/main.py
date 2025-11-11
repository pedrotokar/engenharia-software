from funcoes import history, TaskCommand, ExecutionHandler, ValidationHandler

#===============Questão 1===============
"""
Resposta do item (a) - justificativa

Na minha resolução, utilizarei a combinação dos padrões Chain of Responsability
e Command (2). Os handlers do padrão chain of responsability serão responsáveis
por efetivamente realizar as tarefas, enquanto o padrão command fornecerá uma
interface para executar os tipos de tarefa e para fazer log das tarefas.

As principais motivações por trás dessa escolha são os requisitos de inclusão de novos
tipos de tarefas e de mantimento do histórico de tarefas realizadas. 

O padrão Chain of responsability é adequado para a inclusão de novos tipos de tarefas, 
já que só será necessário criar uma nova subclasse de Handler que implemente um novo 
tipo de requisição e adicionar essa nova subclasse nas cadeias que ela for necessária. 

Já o padrão command é importante para atender de forma adequada o requisito do
histórico de tarefas. O método execute do comando, quando chamado, irá usar a cadeia
para tratar a execução e irá salvar o resultado e timestamp em uma cópia sua, que
é armazenada em um histórico. Assim, fica fácil de inspecionar o histórico para ver
execuções anteriores, e também de armazenar estados para possívelmente desfazer
alterações.

Os padrões contribuem para a legibilidade do código: como a execução das tarefas em
si é feita por Handlers, fica fácil para um programador encontrar onde é executada uma
tarefa em específico, pois ele terá que procurar apenas entre os handlers. A lógica
de armazenamento do histórico também é concentrada no comando, sendo desacoplada da 
execução da tarefa em si.

Apesar de não estar implementado aqui, esses padrões permitem que o requisito de
configuração dinâmica seja atendido, por meio da adição de parâmetros extra no
método `handle` ou da criação de um objeto `Request`, que armazenará parâmetros
de uma requisição. A classe comando também teria que ser alterada para levar
em conta esses parâmetros no momento do pedido.

Os padrões strategy e template method dificultariam a adição de novas tarefas, já que
o template method `execute` sempre realizaria os mesmos três passos, e a adição de novos
aumentaria a quantidade de métodos que o programador precisaria sobreescrever para
usar o template method. Eles também dificultariam o uso do histórico, já que a lógica
de logging teria que ser feita junto com a execução das tarefas, aumentando as
responsabilidades dos métodos.
Ainda assim, ainda seria fácil para um programador encontrar a definição dos algorítmos,
já que elas estariam concentradas em subclasses de TaskTemplate.

abaixo está o driver code do item (b) - implementação mínima
"""

# Criando a cadeia.
cadeia = ValidationHandler(ExecutionHandler())

# Comandos com requisições que podem ser tratadas pela cadeia
command = TaskCommand("[validation]", cadeia)
command_2 = TaskCommand("[execution]", cadeia)

# Nenhum handler trata requisições de import, isso serve para testar o comportamento
# do final da cadeia.
command_3 = TaskCommand("[import]", cadeia)

command.execute()
command_2.execute()
command.execute()
command_3.execute()

print("====LOG DOS COMANDOS====")
for command in history:
    print(command.timestamp, "|", command.handler_name, "| resultado: \"", command.result, "\"")

