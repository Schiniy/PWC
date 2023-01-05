result = input("Digite seu endereço: ")

parte1 = []
parte2 = []
trava = False
template1 = False

# D
if " No " in result:
    result = result.split(" No ")
    parte1 = [result[0]]
    parte2 = ["No", result[1]]

# A e C
elif "," in result:
    result = result.split(",")
    result = list(map(lambda x: x.strip(), result))
    if any(letra.isdigit() for letra in result[0]):
        parte2 = [result[0]]
        parte1 = [result[1]]
    else:
        parte2 = [result[1]]
        parte1 = [result[0]]

# Padrão
else:
    result = result.split(" ")
    if any(letra.isdigit() for letra in result[0]):
        parte1 = result[1:]
        parte2 = [result[0]]

    else:
        for palavra in result:
            if any(letra.isdigit() for letra in palavra) and not trava:
                trava = True
            if trava:
                parte2.append(palavra)
            else:
                parte1.append(palavra)

parte1 = ' '.join(parte1)
parte2 = ' '.join(parte2)

print('{"', parte1, '",', '"', parte2, '"}', sep="")