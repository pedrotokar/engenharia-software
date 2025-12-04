# Atividade - adaptadores e iteradores

O diretório atual contém a resolução (parcial, pois não foram implementados
testes e o código não foi completamente documentado) da atividade guiada sobre
adaptadores e iteradores.

## Padrões utilizados na atividade

[Resumo sobre iteradores](./../resumos/iterator.md)

[Resumo sobre adaptadores](./../resumos/adapter.md)

## Decisões tomadas na atividade

Para o projeto, utilizei adaptadores para implementar uma interface `obter_dados`.
Cada subclasse da classe abstrata `AdaptadorInstrumento` implementa esse método, e
a subclasse `AdaptadorObjeto` é associada à uma instância de `Loja`, fazendo o
papel de adaptar as funcionalidades da classe `Loja` para a interface desejada
`obter_dados`.

Assim, independente de como os dados estiverem armazenados, existe uma forma de
obtê-los como tuplas. Uma implementação mais fiel do padrão adaptador poderia
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
