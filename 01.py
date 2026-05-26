# Suponha que executamos uma sequência de operações sobre uma pilha cujo tamanho nunca
# ultrapassa k. Considere uma pilha com operações Push e Pop. Após cada bloco de k operações,
# executamos uma operação Copy, que faz uma cópia completa da pilha para fins de backup.

# Implemente essa estrutura de dados em Python, contabilizando apropriadamente as operações
# que forem relevantes para uma análise amortizada, e gere um arquivo com 1000 operações e
# execute-as usando o seu programa.

import random

class Stack:
    def __init__(self, k):
        self.stack = []
        self.backup = []
        self.k = k

        # Contadores
        self.push_count = 0
        self.pop_count = 0
        self.copy_count = 0
        self.real_cost = 0 # Custo real das operações para análise amortizada
        self.op_count = 0  # Contador de operações para determinar quando fazer a cópia

    def push(self, value):
        if len(self.stack) < self.k:
            self.stack.append(value)
            self.push_count += 1
            self.real_cost += 1

            self.call_copy()
    
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
            self.pop_count += 1
            self.real_cost += 1

            self.call_copy()
    
    # Verifica se precisa fazer a cópia após cada operação
    def call_copy(self):
        self.op_count += 1
        
        if self.op_count % self.k == 0:
            self.copy()

    def copy(self):
        self.backup = self.stack.copy()
        self.copy_count += 1
        self.real_cost += len(self.stack)

    # Calcula o custo amortizado por operação
    def amortized_cost(self):
        if self.op_count == 0: return 0
        
        return self.real_cost / self.op_count
    

k = 20
ops = 1000

for i in range(3):
    print(f"Teste {i+1} ---------------------------------")
    stack = Stack(k)
    
    for _ in range(ops):
        operation = random.choice(['push', 'pop'])
        
        if operation == 'push':
            stack.push(random.randint(1, 100))
        else:
            stack.pop()

    print(f"Total Push: {stack.push_count}")
    print(f"Total Pop: {stack.pop_count}")
    print(f"Total Copy: {stack.copy_count}")
    print(f"Custo Real Total: {stack.real_cost}")
    print(f"Custo Amortizado por Operação: {stack.amortized_cost():.2f}")

