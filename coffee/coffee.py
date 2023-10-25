print('======================================')
print('=============== COFFEE ===============')
print('======================================')
print('Desenvolvido por WellersonDev \nImagem do icone de srip do site flaticon: https://www.flaticon.com/br/autores/srip')
print('')
print('ITEMS')
#print('(01)Café \n(02)Café Capuccino \n(03)Café Lungo \n(04)Café Gelado \n(05)Pão Francês \n(06)Pão Integral \n(07)Waffle \n(08)Pão de Aveia \n(09)Rosquinha \n(10)Sanduiche \n(11)Fatia de Bolo')

from time import sleep
comida = ['Pão Francês', 'Pão Integral', 'Waffle', 'Pão de Aveia', 'Rosquinha', 'Sanduiche', 'Fatia de Bolo']
bebidas = ['Café', 'Café Capuccino', 'Café Lungo', 'Café Gelado']
print(f'(01){comida[0]:<15} (02){bebidas[0]} \n(03){comida[1]:<15} (04){bebidas[1]} \n(05){comida[2]:<15} (06){bebidas[2]} \n(07){comida[3]:<15} (08){bebidas[3]} \n(09){comida[4]} \n(10){comida[5]} \n(11){comida[6]}')
print('')

lista = list()
items = dict()
qtd = 0
items["item"] = input('O que vai pedir?(ID): ')

while True:

    if items['item'] == '02':
        items["item"] = 'Café'
        items["valor"] = 4.00
        lista.append(items.copy())
        qtd = qtd + 1

    elif items['item'] == '04':
        items['item'] = 'Café Capuccino'
        items['valor'] = 5.00
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '06':
        items['item'] = 'Café Lungo'
        items['valor'] = 5.00
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '08':
        items['item'] = 'Café Gelado'
        items['valor'] = 4.50
        lista.append(items.copy())
        qtd = qtd + 1
        
    elif items['item'] == '01':
        items['item'] = 'Pão Francês'
        items['valor'] = 2.50
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '03':
        items['item'] = 'Pão Integral'
        items['valor'] = 3.00
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '05':
        items['item'] = 'Waffle'
        items['valor'] = 4.00
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '07':
        items['item'] = 'Pão de Aveia'
        items['valor'] = 3.00
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '09':
        items['item'] = 'Rosquinha'
        items['valor'] = 3.00
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '10':
        items['item'] = 'Sanduiche'
        items['valor'] = 4.00
        lista.append(items.copy())
        qtd = qtd + 1
    
    elif items['item'] == '11':
        items['item'] = 'Fatia de Bolo'
        items['valor'] = 3.55
        lista.append(items.copy())
        qtd = qtd + 1
    
    if items['item'] == 'Café' or items['item'] == 'Café Capuccino' or items['item'] == 'Café Lungo' or items['item'] == 'Café Gelado' or items['item'] == 'Pão Francês' or items['item'] == 'Pão Integral' or items['item'] == 'Waffle' or items['item'] == 'Pão de Aveia' or items['item'] == 'Rosquinha' or items['item'] == 'Sanduiche' or items['item'] == 'Fatia de Bolo':
        pergunta = input('Deseja pedir algo mais?[SIM/NÃO]: ').strip().upper()[0]
        if pergunta == 'S':
            items['item'] = input('O que vai pedir?(ID): ').strip()
        else:
            break

#print(lista)
#print(qtd)
print('')

conte = 0
total = 0
for produto in lista:
    for v in produto.values():
        if conte%2 == 0:
            print(f'{v:<35}', end='')
        elif conte%2 == 1:
            print(f'{v:.2f}')
            print('------------------------------------------')
            total = total + v
        conte = conte + 1

sleep(1)
print(f'Total: {total:.2f}')
fim = input('Enter para fechar')
