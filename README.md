<h3 align="center">Python e Orientação a Objetos</h3>

<p align="justify">
    &emsp;Uma classe é uma especificação de um tipo, definindo valores e comportamentos. <br>
    &emsp;Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos. <br>
    &emsp;Uma boa analogia é considerar a classe como a receita para a criação de algum prato; por exemplo, um delicioso bolo de cenoura. <br>
    &emsp;Os atributos são as características que especificam uma classe.
</p>

<h4 align="center">&emsp;Conta</h4>

```python
from conta import Conta
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

<h4 align="center">&emsp;Desafio: Data</h4>

```python
from datas import Data
```

```python
d = Data(19, 2, 2022)
```

```python
d.formatada()
```

<h4 align="center">&emsp;Desafio: Retangulo</h4>

```python
from retangulo import Retangulo
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

#### SOLID
- S - Single responsibility principle
- O - Open/closed principle
- L - Liskov substitution principle
- I - Interface segregation principle
- D - Dependency inversion principle