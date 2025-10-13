# Atividade - adaptadores e iteradores

O diretório atual contém a resolução (parcial, pois não foram implementados
testes e o código não foi completamente documentado) da atividade guiada sobre
adaptadores e iteradores.

## Padrões utilizados na atividade

### Iterador

O padrão iterador serve para abstrair de uma coleção (ou agregado) a forma como
ela é percorrida. Ou seja: a implementação da coleção não precisa se preocupar
em como um possível cliente vai percorrer os elementos dela, e nem em armazenar
algum estado de elemento atual ou próximo elemento.

Para isso, se cria uma classe Iterador, que é ligada à coleção por meio de uma
composição. Essa classe vai internamente ter acesso as interfaces da coleção
e por cima delas vai poder implementar uma lógica para percorrer ela. O iterador
geralmente implementa métodos para avançar e voltar na coleção e para obter o 
elemento atual, mas isso depende um pouco da linguagem de programação e de como o
cliente espera iterar.

Algo importante a se destacar é que o iterador fica inválido a partir do momento
em que houver uma alteração na coleção associada a ele. A lógica interna dele
deve levar isso em conta.

Em Python, um objeto iterável (ou seja, que tem uma classe de iterador que pode
percorrê-lo) implementa o método `__iter__`, que retorna uma instância do
iterador. Já o iterador implementa o método `__next__`, que retorna um elemento
da coleção e atualiza a lógica interna para saber qual o próximo. É esse método
`__next__` que deve realizar a verificação do estado da coleção, para saber
se é a mesma.

Se algum algorítmo para percorrer a coleção seja implementada nela mesmo e um 
iterador apenas manter o estado da percorrência, esse iterador pode ser chamado
de cursor.

![Esquema UML das classes envolvidas em um iterador](iterador.png)

### Adaptador

Os adaptadores são um padrão de projeto pensado para o caso em que se deseja
utilizar uma classe em um projeto, mas essa classe (_adaptee_) não implementa as
interfaces esperadas pelo cliente. Eles cumprem o papel de implementar essas
interfaces, utilizando e manipulando as interfaces do objeto que se deseja
utilizar.

Existem duas ideias para implementar adaptadores: adaptadores de classe e 
adaptadores de objeto.

Os adaptadores de classe funcionam com herança múltipla: eles herdam tanto
de uma classe que implementa a interface desejada quanto da classe original que
se deseja adaptar. Logo, eles fazem tudo o que a classe original faria, com a adição da interface nova.

![Esquema UML das classes envolvidas em um adaptador de classe](adaptador_classe.png)

Os adaptadores de objeto funcionam herdando apenas da classe que implementa a
interface desejada. Por meio de uma composição, eles armazenam uma instância
da classe original (_adaptee_) e então conseguem usar ela e seus métodos para
implementar a interface desejada. Essa aplicação tem a vantagem de poder adaptar
classes que herdam da classe adaptada.

![Esquema UML das classes envolvidas em um adaptador de objeto](adaptador_objeto.png)

A escolha depende principalmente de dois fatores: se haverão múltiplas subclasses
da classe adaptada e se será necessário alterar métodos e comportamentos internos
da classe adaptada. No primeiro caso, o uso de adaptadores de objeto é melhor e
no segundo caso, o uso de adaptadores de classe é melhor.

Também é possível fazer adaptadores de dois sentidos, que herdarão das duas
classes e oferecerão as interfaces das duas.

## Decisões tomadas na atividade

Para o projeto, utilizei adaptadores para implementar uma interface `obter_dados`.
Cada subclasse da classe abstrata `AdaptadorInstrumento` implementa esse método, e
a subclasse `AdaptadorObjeto` é associada à uma instância de `Loja`, fazendo o
papel de adaptar as funcionalidades da classe `Loja` para a interface desejada
`obter_dados`.

Assim, independente de como os dados estiverem armazenados, existe uma forma de obtê-los como tuplas. Uma implementação mais fiel do padrão adaptador poderia
definir classes como `API` e `CSV` que fizessem dentro delas a coleta dos dados
do CSV e API, com seus próprios métodos e interfaces, e as classes adaptadoras
trabalhariam com elas para converter os dados ao formato desejado. No caso
da atividade, porém, isso introduziria uma complexidade desnecessária.

Os iteradores foram empregados junto com uma coleção de instrumentos. Essa
coleção/agregado de instrumentos oferece um método para obter um iterador (como
a atividade foi feita em python, o próprio método mágico `__iter__`). O iterador,
como discutido acima, abstrai qualquer preocupação sobre como percorrer essa
coleção.

A coleção em si recebe vários adaptadores. Apesar de não saber se essa é a melhor
abordagem para resolver o problema na prática, tentei me manter o mais fiel que
pude à ideia do livro, então fiz essa classe coleção. Uma implementação
alternativa poderia fazer a "coleta" dos itens dos adaptadores dentro da coleção,
e não no iterador. Uma implementação alternativa também poderia unificar a coleção
e o iterador em uma única classe.

Uma possível vantagem do iterador seria adicionar outras formas de iteração.
Uma delas seria não iterar em items que viessem de um adaptador X ou Y.

## O que não foi feito:
- Documentação em todos os métodos e funções
- Testes unitários
- Driver code em um arquivo `main.py`
