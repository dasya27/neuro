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

    def change_weights(self, n):
        # меняем веса по правилу Хебба
        for neuron in self.neurons:
            for i in range(2):
                # для каждого веса своя дельта
                delta = n * neuron.signals[i] * self.outputs[i]
                neuron.weights[i] += delta




x = [[0.97, 0.20], [1.00, 0.00], [-0.72, 0.70], [-0.67, 0.74], [-0.80, 0.60], [0.00, -1.00], [0.20, -0.97], [-0.30, -0.95]]
# коэффициент обучения нейрона
n = uniform(0.01, 0.99)

for vector in x:
    # создаем нейросеть из 2 нейронов
    neurons = [Neuron(x[i]) for i in range(2)]
    network = Network(neurons)

    print()
    print("Входной вектор:" + str(vector))
    print("Начальные веса нейронов:")
    for neuron in neurons:
        print(neuron.weights)

    for i in range(10):
        # запускаем круг обучения
        network.loop()
        output = network.outputs

        print()
        print(str(i+1) + " Круг обучения")
        print("Выходные сигналы: " + str(output))

        # меняем веса нейронов:
        network.change_weights(n)

        # измененные веса нейронов:
        print("Измененные веса:")
        for k in range(2):
            print("Нейрон " + str(k+1) + ": " + str(neurons[k].weights))


    print(">" * 100)
