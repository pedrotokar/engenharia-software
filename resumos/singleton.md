# Singleton

O singleton é um padrão pensado para casos em que apenas uma instância de uma
classe deve/pode existir na execução da aplicação. Esses casos ocorrem quando
uma classe é uma coleção de várias outras, e apenas uma coleção dessas deve
existir, ou quando a classe tem a responsabilidade de se comunicar com o sistema
e apenas uma instância deve estar fazendo essa comunicação.

O padrão previne que o cliente se preocupe em adminstrar o acesso à instância
durante a execução, já que a própria classe se responsabiliza por sempre retornar
a mesma instância e não permitir a criação de outra, nem que seja por acidente.
Essa característica também permite que o acesso à instância seja alterado na
classe, para por exemplo permitir mais de uma instância, sem precisar de muita
refatoração no código do cliente.

![Esquema UML das classes envolvidas em um singleton](singleton.png)

A implementação pode ser feita de várias maneiras. Na mais simples, existirá um
método de classe que vai fazer o gerenciamento da instância. Quando esse método é
chamado pela primeira vez, ele irá criar a instância (lazy loading) e nas
próximas vezes irá retornar a instância já criada (e nesse caso o construtor)
da classe será privado/protegido. Em Python é possível sobreescrever o método
`__new__` ou usar um decorador. 

O singleton fica mais complexo quando envolve subclasses. Caso seja possível
haver uma instância pra cada subclasse, o problema pode ser resolvido com um
mapeamento de classe -> instância da classe que pode ser usado para encontrar
a instância certa. Esse também é conhecido como multiton. Em C++ é possível
implementar o método instance em cada subclasse, mas isso irá forçar o cliente
a saber de quais subclasses ele irá querer fazer a instância de antemão.
