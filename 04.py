# Considere um contador binário conforme visto em aula e suponha que desejamos não apenas incrementar 
# um contador, mas também reinicializá-lo com zeros. 
# Suponha que o tempo para examinar ou modificar um bit é Θ(1).

# Implemente em Python um contador representado por um vetor de bits tal que qualquer sequência 
# de n operações Increment e Reset tenha tempo total O(n), considerando um contador inicialmente igual a 0.

class BinaryCounter:
    def __init__(self, size):
        self.counter = [0] * size # Inicializa o contador com zeros
        self.size = size          # Tamanho do contador (número de bits)
        self.highbit = -1         # Índice do bit 1 mais significativo (lembrando que o counter está ao contrário)

    def increment(self):
        i = 0
        while i < self.size and self.counter[i] == 1:
            self.counter[i] = 0
            i += 1
        if i < self.size:
            self.counter[i] = 1
            self.highbit = max(self.highbit, i)
    
    def reset(self):
        for i in range(self.highbit+1):
            self.counter[i] = 0
        self.highbit = -1

    def counter_display(self):
        value = ''.join(str(bit) for bit in reversed(self.counter))
        return value

n = 32
size = 5
counter = BinaryCounter(size)

for i in range(n):
    counter.increment()
    # Verifica se o contador atingiu o valor máximo (2^size - 1) para resetar
    if i == 2**size - 1:
        counter.reset()
        print(f"Contador após reset: {counter.counter_display()}")
        break
    print(f"Contador após incremento {i+1}: {counter.counter_display()}")