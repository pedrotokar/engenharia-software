# Chain of responsability

O padrão chain of responsability atua em casos onde um componente do programa faz
uma solicitação para tratamento de um recurso/interação, e diferentes objetos
podem realizar esse tratamento, a depender de qual é o recurso/interação. O chain
of responsability será adequado quando se há uma configuração dessa forma e há uma
"hierarquia" das objetos que podem tratar a requisição, com objetos que tratam
casos mais específicos e objetos que tratam casos mais gerais.

Participam desse padrão o client, que de alguma forma necessita que o recurso ou
interação sejam tratados, uma interface handler, que define o método
`handleRequest` padronizado para tratar o recurso, e os handlers concretos, que
efetivamente sobreescrevem o método com a forma de tratamento. Eles são reponsáveis
também por avaliar se podem tratar, e caso não possam, precisam passar para
frente a solicitação.

![Esquema UML das classes envolvidas no chain of responsability](chain.png)

Esse padrão reduz o acoplamento, já que o cliente não precisa saber tratar o
recurso, e adiciona flexibilidade no tratamento, já que é possível acrescentar
ou remover tratadores da cadeia dinamicamente. Mas o cliente precisa estar ciente
de que, a depender da estrutura da cadeia, uma requisição poderá ser não tratada.

Vale observar que é possível reutilizar relações entre classes já usadas para
outras partes do sistema para servirem como "propagadoras" das requisições, mas
esta prática pode ser confusa e não funcionar com as relações já estabelecidas
entre as classes. Quando se cria essas relações e interfaces do zero, é possível
fazer com que a implementação padrão do handler apenas passe a requisição para
frente, e então nas subclasses chamar a implementação da classe mãe para realizar
a passagem da requisição.

O padrão pode ficar complexo quando se é necessário fazer com que os handlers
ajam de forma diferente para diferentes tipos de requisição. É possível definir um
inteiro ou string que agem como flags para determinar o tipo de execução do
handler, o que torna necessário que os programadores estejam cientes dessa
convenção. Outra alternativa é definir uma classe (e classes herdadas dela) que
representa uma solicitação e que pode armazenar os parâmetros envolvidos nas
solicitações.
