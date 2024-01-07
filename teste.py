from cliente import Cliente
from conta import Conta

luis: Cliente = Cliente('Luis Villon', 'luis@gmail.com', '123.455.789-23', '11/08/1993')
angelica: Cliente = Cliente('Angelica Toledo', 'ang@gmail.com', '345.676.789-22', '24/03/1954')

print(luis)
print(angelica)

contaf: Conta = Conta(luis)
contaa: Conta = Conta(angelica)

print(contaf)
print(contaa)
