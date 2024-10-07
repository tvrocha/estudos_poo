from datetime import datetime
import pytz
from time import sleep
from random import randint


class ContaCorrente:

    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome: Nome do Cliente
        cpf: CPF do cliente
        ...
    """


    @staticmethod
    def _data_hora() -> str:
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime(r'%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta) -> None:
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo:,.2f}')

    def depositar(self, valor):
        self.saldo += valor
        self._transacoes.append(('Depósito', valor, ContaCorrente._data_hora()))

    def _limite(self):
        self.limite = -1000
        return self.limite

    def sacar(self, valor):
        if self.saldo - valor < self._limite():
            print('Saldo indisponível.')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.consultar_saldo()
            self._transacoes.append(('Saque', valor, ContaCorrente._data_hora()))

    def exibir_historico(self):
        if self._transacoes:
            print('Histórico:')
            for tipo, valor, hora in self._transacoes:
                print(f'Tipo: {tipo}, Valor: R${valor:,.2f}, Hora: {hora}')
        else:
            print('Sem transações na conta.')
    
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self._transacoes.append(('Transferência', valor, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino._transacoes.append(('Transferência', valor, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora() -> str:
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente) -> None:
        self.numero = randint(1000_0000_0000_0000, 9999_9999_9999_9999)
        self.titular = titular
        self.validade = f'{self._data_hora().month}/{self._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


tuba_conta = ContaCorrente('Tulio Vinicius', '136.349.446-50', '0001', '01')
tuba_cartao = CartaoCredito('Tulio Vinicius', tuba_conta)
print(tuba_cartao.conta_corrente.num_conta)
print(tuba_cartao.numero, tuba_cartao.cod_seguranca)
