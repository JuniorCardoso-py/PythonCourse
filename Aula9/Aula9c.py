from calculo_imposto import calculo_inss, calculo_irrf

print('='*50)

salario = float( input("\n Digite seu salario: "))

inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)
    

salario_liquido = salario - inss - irrf


print(f'\n Seu salario liquido é {salario_liquido}')

print('\n', '='*50, sep='')