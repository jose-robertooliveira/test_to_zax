
"""
Para executar o script digite no terminal python3 + o nome do arquivo(script.py).

"""

motoboys = ['Moto 1', 'Moto 2', 'Moto 3', 'Moto 4', 'Moto 5']
lojas = ['Loja 1', 'Loja 2', 'Loja 3']



for motoboy in motoboys:
    print(f"{motoboys[1]}, entrega para {lojas[0]}, 3 pedidos, o motoboy irá ganhar R$13,50. ")
print("----------------------------------------------------------------------------------")

escolha = int(input("Digite o número da lista de motoboys:\n "))
print("============================================================================|")

if escolha == 1:
    print(f"{motoboys[0]}, entrega para {lojas[0]}, 3 pedidos, o motoboy irá ganhar R$13,50. ")
    print(f"{motoboys[0]}, entrega para {lojas[1]}, 4 pedidos, o motoboy irá ganhar R$18,00. ")
    print(f"{motoboys[0]}, entrega para {lojas[2]}, 3 pedidos, o motoboy irá ganhar R$36,00. ")

elif escolha == 2:
    print(f"{motoboys[1]}, entrega para {lojas[0]}, 3 pedidos, o motoboy irá ganhar R$13,50. ")
    print(f"{motoboys[1]}, entrega para {lojas[1]}, 4 pedidos, o motoboy irá ganhar R$18,00. ")
    print(f"{motoboys[1]}, entrega para {lojas[2]}, 3 pedidos, o motoboy irá ganhar R$36,00. ")

elif escolha == 3:
    print(f"{motoboys[2]}, entrega para {lojas[0]}, 3 pedidos, o motoboy irá ganhar R$13,50. ")
    print(f"{motoboys[2]}, entrega para {lojas[1]}, 4 pedidos, o motoboy irá ganhar R$18,00. ")
    print(f"{motoboys[2]}, entrega para {lojas[2]}, 3 pedidos, o motoboy irá ganhar R$36,00. ") 

elif escolha == 4:
    print(f"{motoboys[3]}, entregador exclusivo da {lojas[0]} serão 3 pedidos, o motoboy irá ganhar R$13,50.  ")

elif escolha == 5:
    print(f"{motoboys[4]}, entrega para {lojas[0]}, 3 pedidos, o motoboy irá ganhar R$16,50. ")
    print(f"{motoboys[4]}, entrega para {lojas[1]}, 4 pedidos, o motoboy irá ganhar R$22,00. ")
    print(f"{motoboys[4]}, entrega para {lojas[2]}, 3 pedidos, o motoboy irá ganhar R$39,00. ")

try:
    print(escolha = int(input("Digite o número do motoboy:\n ")))
except ValueError as e:
    print("Digite apenas numeros de 1 a 5")
    