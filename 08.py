# Considere uma estrutura de dados que suporte as seguintes operações para um multiconjunto dinâmico S de números inteiros:
#     a) Insert(S, x) insere x em S;
#     b) Delete-Larger-Half(S) remove os  ⌈|S|/2⌉ maiores elementos de S.
# Projete e implemente em Python uma estrutura de dados de tal forma que qualquer sequência de m operações Insert e 
# Delete-Larger-Half execute em tempo total O(m). Analise e discuta seus resultados. 

# Sua implementação deve incluir também uma forma de imprimir os elementos de S em tempo O(|S|).

import random

class MultiSet:

    def __init__(self):
        self.S = []
        self.real_cost = 0 # Custo real das operações para análise amortizada
        self.op_count = 0  # Contador de operações para análise amortizada

    def insert(self, x):
        self.S.append(x)
        self.real_cost += 1
        self.op_count += 1

    # Encontra a mediana
    def quickselect(self, arr, k):
        if len(arr) == 1:
            return arr[0]

        pivot = random.choice(arr)

        lows = [x for x in arr if x < pivot]
        highs = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]

        if k < len(lows):
            return self.quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivot
        else:
            return self.quickselect(highs, k - len(lows) - len(pivots))

        self.real_cost += len(arr)

    def delete_larger_half(self):
        n = len(self.S)
        
        if n == 0: 
            self.op_count += 1
            return
        
        new_S = []
        
        keep = n // 2
        median = self.quickselect(self.S, keep)

        # Separa os elementos menores que a mediana e os iguais à mediana
        smaller = [x for x in self.S if x < median]
        equal = [x for x in self.S if x == median]
        self.real_cost += n

        new_S.extend(smaller)

        # Se ainda não tem o número suficiente de elementos, adiciona os iguais à mediana
        remaining = keep - len(smaller)
        new_S.extend(equal[:remaining])

        self.S = new_S
        self.op_count += 1

    def print_elements(self):
        for x in self.S:
            print(x, end=" ")

        print()
    
    def amortized_cost(self):

        if self.operations == 0:
            return 0

        return self.real_cost / self.operations

m = 1000
multiset = MultiSet()

for i in range(3):
    print(f"Teste {i+1} ---------------------------------")
    
    for _ in range(m):
        operation = random.choice(['insert', 'remove'])
            
        if operation == 'insert':
            multiset.insert(random.randint(1, 100))
        else:
            multiset.delete_larger_half()

    print("Elementos restantes no multiconjunto:")
    multiset.print_elements()

    print(f"Custo real total: {multiset.real_cost}")
    print(f"Número de operações: {multiset.op_count}")
    print(f"Custo amortizado por operação: {multiset.real_cost / multiset.op_count:.2f}")