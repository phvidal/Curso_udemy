'''Crie um código onde seja solicitado dois valores e impresso qual valor é maior que o outro'''

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

vlr_01=int(primeiro_valor)
vlr_02=int(segundo_valor)

if vlr_01 > vlr_02:
    print(f'{vlr_01} é maior que {vlr_02}')
elif vlr_02 > vlr_01:
    print(f'{vlr_02} é maior que {vlr_01}')
else:
    print(f'O primeiro valor tem o mesmo valor que o segundo')