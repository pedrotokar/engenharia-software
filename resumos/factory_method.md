# Factory Method

O factory method é um padrão pensado para delegar a criação de uma instância de
uma classe específica para um método, no lugar de diretamente construir essa
classe. Isso é útil para casos em que a interface do construtor é alterada mas
o cliente não precisa saber/se preocupar com isso. Também é útil para caso
existam várias subclasses que possam ser instânciadas, todas seguindo uma
inteface pré-estabelecida, e que a construção delas divirja. Nesse caso, não
é desejado que o cliente se preocupe com essa divergência.

Nesse padrão, existe um Creator, que tem a interface do método factory e 
um Produto, que tem uma interface desejada e posssivelmente várias subclasses
(Produtos Concretos) que implementem ela. 

Uma implementação padrão irá ter várias subclasses do Creator (Creators
Concretos), com cada uma implementando o método factory que cria uma instância
de um produto concreto diferente. O Creator original pode ou não pode implementar
uma factory padrão, tornando opcional ou não a existência de subclasses.

![Esquema UML das classes envolvidas na implementação do factory method](factory_method.png)

Uma variação do factory method é o factory method parametrizado. Nesse caso,
o método pode receber algum parâmetro e usar ele como base para saber qual
produto concreto ele irá instanciar e retornar. Nesse caso, subclasses do Creator
podem adicionar ou modificar o funcionamento de algumas opções de parâmetro
específicas, e delegar o processamento dos demais parâmetros para o método
da classe pai.
