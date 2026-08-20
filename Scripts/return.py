def resta_livre(total, usado):
    sobra = total - usado
    return sobra

tot = int(input("Digite o espaço total: "))
use = int(input("Digite o que foi usado: "))

result = resta_livre(tot, use)
print( f"o valor livre é {result}")


if result <= 150:
    print("Atenção: Pouco espaço!")
else:
    print("Espaço OK!")
