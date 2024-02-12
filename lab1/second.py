from random import *

class Neuron:
    weights = []
    signals = []
    wins = 0
    out = 0

    def __init__(self, signals):
        # инициализируем нейрон
        self.signals = signals
        self.weights = [uniform(-1.0, 1.0) for i in range(2)]

    def summ(self):
        return self.weights[0] * self.signals[0] + self.weights[1] * self.signals[1]

    def change_weights(self, n, limit):
        # меняем веса по правилу Гроссберга (по формуле) + штраф победителя
        if self.wins >= limit:
            pass
        else:
            for i in range(len(self.weights)):
                self.weights[i] = self.weights[i] + n * (self.signals[i] - self.weights[i])
            # меняем выходной сигнал и количество побед
            self.out = 1
            self.wins += 1

class Network:
    neurons = []
    outputs = []

    def __init__(self, neurons):
        # создаем нейроны
        self.neurons = neurons

    def loop(self):
        # круг обучения нейронов
        self.outputs = []
        for neuron in self.neurons:
            self.outputs.append(neuron.summ())

    def get_outputs(self):
        return self.outputs

    def get_winner(self):
        return self.outputs.index(max(self.outputs))

x = [[0.97, 0.20], [1.00, 0.00], [-0.72, 0.70], [-0.67, 0.74], [-0.80, 0.60], [0.00, -1.00], [0.20, -0.97], [-0.30, -0.95]]
n = 0.5
limit = 5

for vector in x:
    # создаем нейросеть
    neurons = [Neuron(x[i]) for i in range(4)]
    network = Network(neurons)

    print()
    print("Входной вектор:" + str(vector))
    print("Начальные веса нейронов:")
    for neuron in neurons:
        print(neuron.weights)

    for i in range(10):
        # запускаем круг обучения
        network.loop()
        # определяем нейрона-победителя
        winner_index = network.get_winner()
        # меняем веса победителю
        neurons[winner_index].change_weights(n, limit)
        # получаем выходные сигналы нейронов
        output = network.get_outputs()

        print()
        print(str(i + 1) + " Круг обучения")
        print("Выходные сигналы: " + str(output))
        print("Победитель: " + str(winner_index))
        print("Измененные веса победителя: " + str(neurons[winner_index].weights))
        print("Количество побед:")
        for k in range(len(neurons)):
            print("Нейрон " + str(k) + ": " + str(neurons[k].wins))

    print(">" * 100)
