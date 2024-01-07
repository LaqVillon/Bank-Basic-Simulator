from typing import List
from time import sleep
from conta import Conta
from cliente import Cliente


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print("================================================")
    print("==================== ATM =======================")
    print("================== Festa Bank ==================")
    print("================================================")
    print("Selecione uma opção abaixo: ")
    print("1 - Criar Conta")
    print("2 - Efetuar Saque")
    print("3 - Efetuar Depósito")
    print("4 - Efetuar Transferência")
    print("5 - Listar Contas")
    print("6 - Sair do Sistema")

    opcao: int = int(input())
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Volte sempre!!")
        sleep(2)
        exit()
    else:
        print("Opção inválida!")
        sleep(1)
        menu()


def criar_conta() -> None:
    nome: str = input("Informe o nome do cliente: ")
    email: str = input("Informe o email do cliente: ")
    cpf: str = input("Informe o cpf do cliente: ")
    data_nascimento: str = input("Informe a data de nascimento do cliente: ")
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)
    print("Conta criada com sucesso.")
    print("Dados da conta: ")
    print('------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor do saque: "))
            conta.sacar(valor)
        else:
            print(f"Não foi encontrada a conta com número {numero}")
    else:
        print("Ainda não existem contas cadastradas.")
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        else:
            print(f"Não foi encontrada uma conta com número {numero}")
    else:
        print("Ainda não existem contas cadastradas.")
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input("Informe o número da sua conta: "))
        conta_o: Conta = buscar_conta_por_numero(numero_o)
        if conta_o:
            numero_d: int = int(input("Informe o número da conta destino: "))
            conta_d: Conta = buscar_conta_por_numero(numero_d)
            if conta_d:
                valor: float = float(input("Informe o valor da transeferência: "))
                conta_o.transferir(conta_d, valor)
            else:
                print(f"A conta destino com número {numero_d} não foi encontrada")
        else:
            print(f"A sua conta com número {numero_o} não foi encontrada")
    else:
        print("Ainda não existem contas cadastradas.")
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print("Listagem de contas")
        for conta in contas:
            print(conta)
            print('-----------------------')
            sleep(1)
    else:
        print("Não existem contas cadastradas.")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
