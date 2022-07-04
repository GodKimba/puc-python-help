"""
a) Escreva uma função chamada leDadosSorteio que leia o arquivo DADOS.TXT e retorne uma lista onde cada elemento é uma
sublista com o seguinte formato: [CPF, nome]. Importante: a lista só deve conter informações de pessoas que pagaram a inscrição
"""
dados = """
123.456.789-01:JOSE CARLOS SOUSA:S:JCS@MAIL.COM

542.124.566-19:ANA DE JESUS:S:ADJESUS@IGG.NET.PT

567.426.459-20:CARLOS ALBERTO DA SILVA:S:ALBERTO@GMAIL.COM

121.406.939-87:MARINA PLATA:N:MPLATA@MAIL.COM

521.124.533-94:ANNE MARIE DION:S:ACR@HOTMAIL.COM

030.278.796-11:ANA CLAUDIA MOREIRA:S:ACRR@RADV.BR

652.190.486-34:JAILSON DAS NEVES:N:JNVES@GGG.COM
"""

dadosEmLista = list(filter(None, dados.splitlines()))
novaLista = []

for i in dadosEmLista:
    # Iterando sob dados em lista, retirando pessoas que nao pagaram e inserindo pagantes em novalista
    if ":N:" in i:
        dadosEmLista.remove(i)
    else:
        novaLista += i.split(":")

for j in novaLista:
    # Retirando a informacao de se pagou ou nao
    if len(j) == 1:
        novaLista.remove(j)

for i in novaLista:
    # Retirando o email da lista
    if "@" in i:
        novaLista.remove(i)

# Usando compreensao de listas para iterar cada dois itens
# Adicionar cada item [i] mais seu proximo [i+1] em uma nova lista
listaFinal = [[novaLista[i], novaLista[i + 1]] for i in range(0, len(novaLista) - 1, 2)]

print(novaLista)
print(listaFinal)


"""
b) Escreva uma função chamada realizaSorteio que receba como parâmetro a lista criada pela função leDadosSorteio e um inteiro
representando a quantidade de pessoas que devem ser sorteadas. A função deve realizar o sorteio para essa quantidade de
pessoas da lista, imprimindo o resultado da seguinte forma:
• os 5 primeiros e os 3 últimos caracteres do CPF na sua posição original, assim como o caractere '.'; na posição dos demais
algarismos, deve ser impresso o caractere '*';
• os 4 primeiros caracteres do nome.
Exemplo para três sorteados considerando o arquivo exemplo disponibilizado:
===== Relação dos sorteados ====
CPF Nome
030.2**.***-11 ANAS
691.4**.***-31 CARO
123.4**.***-01 JOSE
Dicas (apenas sugestões; existem outras possibilidades):
• para não sortear duas vezes a mesma pessoa, exclua a pessoa sorteada da lista;
• utilize a função randint do módulo random.
"""


"""
c) Escreva um programa que leia do teclado um inteiro representando a quantidade de pessoas que devem ser sorteadas e exiba
na tela CPF e nome dessas pessoas, conforme descrito no item (b). Utilize, obrigatoriamente, as funções dos itens anteriores.
ATENÇÃO: se o valor lido for maior do que a quantidade de pessoas que pagaram a inscrição, o programa deve apenas exibir a
mensagem 'Impossível realizar o sorteio para essa quantidade'.
"""
