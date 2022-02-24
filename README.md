<h3 align="center">Python e Orientação a Objetos</h3>

<p align="center">
    <a href="#conta">Conta</a> <br>
    <a href="#cliente">Cliente</a> <br>
    <a href="#desafio_data">Desafio: Data</a> <br>
    <a href="#desafio_retangulo">Desafio: Retângulo</a> <br>
    <a href="#solid">SOLID</a> <br>
    <a href="#data_model">Data Model</a> <br>
    <a href="#anotacoes">Anotações</a>
</p>

<hr>

<h3 id="conta" align="center">Conta</h3>

```python
from introducao_a_orientacao_a_objetos.conta import Conta
```

```python
conta = Conta(123, "Lucas", 55.5, 1000.0)
```

```python
conta.extrato()
```

```python
conta.deposita(60.0)
```

```python
conta.saca(20.0)
```

```python
conta2 = Conta(321, "Fulano", 50.0, 1000.0)
```

```python
conta.transfere(10.0, conta2)
```

```python
conta.get_saldo()
```

```python
conta.get_titular()
```

```python
conta.set_limite(2000.0)
```

```python
conta.get_limite()
```

```python
Conta.codigo_banco()
```

```python
codigos = Conta.codigos_bancos()
```

```python
codigos
```

```python
codigos['BB']
```

<hr>

<h3 id="cliente" align="center">Cliente</h3>

```python
from introducao_a_orientacao_a_objetos.cliente import Cliente
```

```python
cliente = Cliente("lucas")
```

```python
cliente.nome = "fulano"
```

```python
cliente.nome
```

<hr>

<h3 id="desafio_data" align="center">Desafio: Data</h3>

```python
from introducao_a_orientacao_a_objetos.datas import Data
```

```python
d = Data(19, 2, 2022)
```

```python
d.formatada()
```

<hr>

<h3 id="desafio_retangulo" align="center">Desafio: Retângulo</h3>

```python
from introducao_a_orientacao_a_objetos.retangulo import Retangulo
```

```python
r = Retangulo(7, 6)
```

```python
r.area = 7
```

```python
r.obter_area()
```

<hr>

<h3 id="solid" align="center">SOLID</h3>

<p align="left">
    S - Single responsibility principle <br>
    O - Open/closed principle <br>
    L - Liskov substitution principle <br>
    I - Interface segregation principle <br>
    D - Dependency inversion principle
</p>

<hr>

<h3 id="data_model" align="center">Data Model</h3>

<pre>
<strong>Inicialização</strong>   
__init__

<strong>Representação</strong> 
__str__   
__repr__

<strong>Container, sequência</strong>    
__contains__    
__iter__    
__len__     
__getitem__

<strong>Numéricos</strong>   
__add__     
__sub__     
__mul__     
__mod__
</pre>

<pre>
<strong>Inicialização</strong>   
obj = Novo()

<strong>Representação</strong> 
print(obj)
str(obj)
repr(obj)

<strong>Container, sequência</strong>    
len(obj)
item in obj
for i in obj
obj[2:3]

<strong>Numéricos</strong>   
obj + outro_obj
obj * obj
</pre>

<hr>

<h3 id="anotacoes" align="center">Anotações</h3>

<p align="justify">
    &emsp;Uma classe é uma especificação de um tipo, definindo valores e comportamentos. <br>
    &emsp;Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos. <br>
    &emsp;Uma boa analogia é considerar a classe como a receita para a criação de algum prato; por exemplo, um delicioso bolo de cenoura. <br>
    &emsp;Os atributos são as características que especificam uma classe. <br>
    &emsp;Os mixins são classes herdadas que não precisam ser instanciadas e contém preocupações comuns a diversas classes. <br>
    &emsp;Podemos usar composição para substituir herança como boa prática de orientação a objetos. <br>
    &emsp;title - Pega a primeira letra de cada palavra e coloca em maiúsculo. <br>
    &emsp;ABC - Abstract Base Classes <br>
    &emsp;MRO - Method Resolution Order
</p>
