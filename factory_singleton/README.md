# Atividade - factorys e singleton

O diretório atual contém a resolução da atividade sobre abstract factories,
factory methods e singletons.

## Padrões utilizados na atividade

[Resumo sobre singleton](./../resumos/singleton.md)

[Resumo sobre factory method](./../resumos/factory_method.md)

[Resumo sobre abstract factory](./../resumos/abstract_factory.md)

## Decisões tomadas na atividade

Para fazer a atividade, tomei a liberdade de mudar a ideia dos elementos de UI
para serem independentes do sistema Mac ou Windows. No lugar, usei a ideia de
diferentes bibliotecas gráficas com diferentes componentes.

Nesse caso, a janela e o cursor são produtos, e suas versões específicas para GTK
ou Qt são produtos concretos. Uma abstract factory define dois métodos, um para
retornar um cursor e um para retornar uma janela, e duas subclasses implementam
eles para o Qt e para o GTK, de forma que um usuário não se preocupa em ele mesmo
garantir que todos os componentes sejam da interface correta.

Essas factorys são criadas por um factory method que está presente na classe da
aplicação, e esse método não faz distinção caso a aplicação seja de Mac ou 
Windows. Esse método é um factory method parametrizado, já que recebe uma string
indicando se a factory retornada deve ser de Qt ou GTK. Seria possível usar
singleton nessas factorys, mas como usei em outra parte da atividade, não usei
aqui pela simplicidade.

Os documentos foram feitos com uma classe abstrata de documento, que define
a interface que eles devem ter, e duas subclasses representando documentos
de cada um dos SO (Mac e Windows). Eles são criados usando um factory method
presente na aplicação. Esse factory method não é parametrizado: existem
subclasses da aplicação para Windows e Mac, e cada uma delas implementa
o facotry method usando a subclasse correta do documento.

A aplicação foi protegida por um singleton, de forma que apenas uma aplicação
pode existir. A forma como implementei isso fugiu um pouco das implementações
vistas normalmente, já que nesse caso só pode exisitr uma aplicação, mas ela
pode ser ou de Mac ou de Windows. Da forma que fiz, o que ocorre é:

1. Quando a classe `Aplicacao` vai ser instanciada, ela verifica uma variável
de ambiente para saber o sistema em uso. Essa ideia foi tirada do GoF.
2. Ela então cria uma instância apropriada de uma aplicação de Windows ou Mac
baseada nessa flag, mesmo que o inicializador seja genérico (`Aplicacao`) ou
de uma subclasse específica (`_AplicacaoWindows` ou `_AplicacaoMac`).
3. Futuras tentativas de instânciar tanto a classe genérica quanto as subclasses
específicas por sistema retornarão a instância existente, mesmo que seja de
outra subclasse.

Esse útlimo comportamento pode ser inconsistente, e as subclasses foram feitas
pensando em *não* serem utilizadas pelo usuário da aplicação, que deve sempre
usar o construtor da classe `Aplicacao` para recuperar a instância desejada.
O cliente então também não se preocupa com instanciar corretamente uma subclasse
de `Aplicacao`, já que essa verificação é feita internamente levando em conta
uma flag. Assim é possível definir operações de Mac e Windows em subclasses
diferentes, sem atrapalhar a interface.

Isso poderia ser feito simplesmente com uma flag armazenada na classe 
`Aplicacao`, que auxiliaria os métodos a saberem qual ação tomar. Mas isso traria
mais responsabilidades para a classe aplicação, que precisaria saber operações
específicas de cada sistema. 
