def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}

    return conta

print(cria_conta(123, "Lucas", 55.0, 1000.0))