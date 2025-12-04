# Template methods

De certa maneira, os template methods podem ser comparados com o [strategy]
(strategy.md). Aqui,  existe um algorítmo implementado que tem passos 
fixos/partes invariantes e partes que podem variar, e se deseja assegurar que 
as partes invariantes sempre serão respeitadas. Se define então uma classe que
terá diversos métodos representando os passos variáveis (operações primitivas) 
e um método template, que irá orquestrar a execução desses passos.

Ou seja, a classe terá um método template concreto e diversos métodos abstratos,
que representam passos opcionais e obrigatórios do algorítmo geral que a classe
executa. É importante tentar sempre manter o número de operações primitivas deve
ser mantido baixo, para evitar que o uso do projeto seja difícil ou "tedioso".

![Esquema UML das classes envolvidas no template method](template_method.png)

As operações primitivas usadas pelos métodos template (e que são sobreescritas)
podem ser tanto **obrigatórias** quanto **opcionais**. As opcionais são chamadas
de ganchos/hooks, e geralmente antecedem e precedem alguma operação importante.
As operações obrigatórias são definidas como uma interface, e os ganchos podem ser
definidos como métodos que por omissão não irão executar nada. É importante 
que quem for implementar as operações saiba quais são opcionais e quais não são.

Os benefícios são semelhantes ao strategy: aplicando esse padrão de projeto,
as responsabilidades de uma função diminuirão e o programa será mais fácilmente
extendido no futuro, já que será fácil alterar passos de um algorítmo sem copiar
os passos invariantes.

