import math

nome = str(input('Qual o seu nome: '))
p = float(input('{} qual o seu peso: '.format(nome)))
a = float(input('{} qual a sua altura: '.format(nome)))

cal = p/(a)**2
print('{} O seu imc é de  {:.2f}'.format(nome, cal))

if cal < 18.5:
    print('PESO BAIXO ')
elif cal >= 18.5 and cal <= 24.9:
    print('PESO NORMAL ')
elif cal >= 25.0 and cal <= 29.9:
    print('SOBREPESO ')
elif cal >= 30.0 and cal <= 34.9:
    print('OBESIDADE (GRAU 1) ')
elif cal >= 35.0 and cal <= 39.9:
    print('OBESIDADE SEVERA (GRAU 2) ')
elif cal >= 40.0:
    print('OBESIDADE MÓRBIDA (GRAU 3)')
else:
    print('Opção invalida !!')
