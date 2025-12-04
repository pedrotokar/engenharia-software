# Command

O padrão command é usado para desacoplar a execução de ações no sistema das classes
que representam esse sistema. Assim, a classe pode saber que precisa responder a um
imput com a execução de um comando, mas não precisa saber como exatamente executar
esse comando. Esse desacoplamento é poderoso e evita que classes precisem saber
fazer uma operação específica, ao mesmo tempo em que permite que uma operação
seja reutilizada em vários contextos.

O padrão envolve uma interface comando, que define um método para execução. A
partir dele, diversos comandos concretos são criados, efetivamente implementando
o método de execução. Os comandos instanciados são parte de uma relação de
agregação com uma classe que irá usar a interface de execução (invoker), e podem
ser associados a diferentes classes que irão ser manipuladas pelo comando
(receptor). O tempo de vida do invoker não precisa estar relacionado com o tempo
de vida do comando.

![Esquema UML das classes envolvidas no comando](command.png)

É possível ver o padrão comando como uma transposição de `callbacks` (funções
registradas que são chamadas posteriormente por um componente) de programas
imperativos/procedurais para programas orientados à objeto. O padrão torna fácil
criar novos comandos que fazem novas funções e podem ser usados intercambiavelmente
com outros, assim como seria possível escrever mais funções callback.

É importante pensar bem na forma como o commando e o receptor irão se relacionar.
O comando pode ou simplesmente invocar um método do receptor ou apenas acessar
e modificar dados necessários nele, mas usando uma lógica implementada dentro de
si (no extremo desse caso, podem haver comandos sem receptor). É preciso pensar
bem em qual é o melhor lugar para se implementar a ação em si, levando em conta
a complexidade da classe receptor. Em algumas situações, o comando pode inclusive
fazer uma busca por seu receptor em alguma estrutura de dados global.

Uma grande vantagem do padrão é permitir que o sistema tenha "memória" das últimas
ações realizadas. É possível armazenar uma lista com cópias de comandos
utilizados, e com ela inspecionar o histórico de ações, tanto para reaplicá-las em
uma outra execução zerada do sistema ou para revertê-las. Para poder reverter, é
necessário que os comandos tenham um método de desafazer, e que armazenem dentro 
de si potênciais variáveis de estado que podem ter sido perdidas com o comando.

Uma outra possível classe que se adequa no padrão é a macro comando, que nada
mais é que uma coleção ordenada de comandos que podem ser executados em sequência.
Algumas aplicações permitem, inclusive, a criação de diferentes macros pelo usuário
do sistema.

Uma última vantagem do projeto é sua aplicabilidade em sistemas concorrentes: um
sistema que recebe paralelamente diversos comandos (por exemplo um esquema
servidor - clientes) pode definir lógicas para saber como enfileirar e ordenar
comandos recebidos em tempos diferentes, e então executar em ordem correta as
operações.
