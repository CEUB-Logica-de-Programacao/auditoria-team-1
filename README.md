# Auditoria

Dado a grande repercussão sobre uma possível fraude das urnas, você foi selecionado para desenvolver um sistema de
auditoria para o TSE. Para isso, você deve implementar um programa que, dado um arquivo de entrada, verifique se
há alguma inconsistência nos dados. A verificação se dará através de um algoritmo de 3 etapas.

## 1ª Etapa

A primeira etapa consiste em verificar se o ID do arquivo é um número válido. Esse ID deve ser um número inteiro entre
1000 e 9999. É válido ressaltar que zeros a esquerda são considerados válidos. Por exemplo, 0001 é um ID. Para descobrir
se o ID é válido, você deve dividi-lo em dois novos números inteiros `new1` e `new2`.

* Por exemplo, dado ID = 2932, você tem os seguintes dígitos: dois 2's, um 9 e um 3. Alguns dos possíveis
  pares [`new1`, `new2`] são [22, 93], [23, 92], [223, 9] e [2, 329].

Agora, você deve verificar qual é a menor soma possível de `new1` e `new2`. Por exemplo, se `new1 = 22` e `new2 = 93`,
a soma é 115. Caso a soma seja menor ou igual a 100, o ID é válido. Caso contrário, o ID é inválido.

## 2ª Etapa

A segunda etapa consiste em verificar se existe algum voto que não foi computado. Para isso, você receberá uma
lista `votos`
de `n` números inteiros, aonde todo `votos[i]` está entre `[1, n]`. Você deve verificar se existe algum número `i` tal
que
`votos[i]` não está presente em `votos`. Caso exista, o voto não foi computado. Caso contrário, todos os votos foram
computados.

### Exemplo

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

```
Input: nums = [1,1]
Output: [2]
```

def ValidaSenha():
    
    senha = input('Digite a senha: ')

    
    aux, quantidade = [], []

    for i in range(0, len(senha)):
      
        if len(aux) == 0:
            aux.append(senha[i])
            
            quantidade.append(senha.count(senha[i]))
        else:
            for j in range(0, len(aux)):
                if senha[i] == aux[j]:
                    teste = 1
                    break
                else:
                    teste = 0

           
            if teste == 0:
                aux.append(senha[i])
                quantidade.append(senha.count(senha[i]))

    if quantidade.count(quantidade[0]) == len(quantidade):
        print('A senha é válida')
    else:
        print('A senha é inválida. É fraude!')

ValidaSenha()
