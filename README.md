### Python: Orientação a Objetos

Uma classe é uma especificação de um tipo, definindo valores e comportamentos. <br>
Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos. <br>
Uma boa analogia é considerar a classe como a receita para a criação de algum prato; por exemplo, um delicioso bolo de cenoura. <br>
Os atributos são as características que especificam uma classe.

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