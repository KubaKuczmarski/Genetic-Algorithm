import random
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import time
import gc

class Solver(ABC):

    """A solver. It may be initialized with some hyperparameters."""

    @abstractmethod
    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        pass

    @abstractmethod
    def solve(self, problem, zero_population):
        """
         A method that solves the given problem for given initial solution.
         It may accept or require additional parameters.
         Returns the solution and may return additional info.
         """
        pass

# Funkcja do symulacji lotu drona
def flight_simulate(x):
    # Stałe
    T = 100
    g = -10  # grawitacja
    dt = 0.1  # kwant czasu
    P = 30  # przyspieszenie drona
    r = 0.1  # tarcie = -0.1 m/s^2 * s/m * v, gdzie v - aktualna prędkość
    v_crash = 20
    crash_penalty = 1500

    # Symulacja
    h = 0
    v = 0
    t = 0

    max_h = 0
    while h >= 0:
        a = g + (P * x[t] if t < T else 0) - v * r
        v += a * dt
        h += v * dt
        t += 1
        max_h = max(h, max_h)
    reward = max_h
    if v < -v_crash:
        reward -= crash_penalty
    return reward

class GeneticSolver(Solver):

    def __init__(self, population_size, genome_size, mutation_rate, num_generations, crossing_probability):
        self.population_size = population_size
        self.genome_size = genome_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations
        self.crossing_probability = crossing_probability

    def get_parameters(self):
        return {
            "population_size": self.population_size,
            "genome size": self.genome_size,
            "mutation_rate": self.mutation_rate,
            "num_generations": self.num_generations,
            "crossing_probability": self.crossing_probability,
        }
    # Algorytm genetyczny
    def solve(self, population=None):

        #Inicjalizacja populacji
        if population is None:
            population = self.init_population(self.population_size, self.genome_size)

        best_fitness_values = []
        mean_fitness_values = []
        best_chromosome = None
        best_fitness = float("-inf")

        for generation in range(self.num_generations):
            # Ocena populacji
            fitness_values = [flight_simulate(individual) for individual in population]
            mean_fitness_values.append(sum(fitness_values) / len(fitness_values))

            # Wybór najlepszego osobnika
            current_best_fitness_index = fitness_values.index(max(fitness_values))
            current_best_chromosome = population[current_best_fitness_index]
            current_best_fitness = fitness_values[current_best_fitness_index]

            # Zapisanie najlepszego osobnika
            if current_best_fitness > best_fitness:
                best_chromosome = current_best_chromosome
                best_fitness = current_best_fitness

            # Zapisanie wartości najlepszego osobnika w każdej iteracji
            best_fitness_values.append(best_fitness)

            # Selekcja
            selected_population = self.roulette_selection(population, fitness_values)

            # Krzyżowanie
            offspring = []
            while len(offspring) < self.population_size - 1:
                parent1 = random.choice(selected_population)
                parent2 = random.choice(selected_population)
                child1, child2 = self.one_point_crossover(parent1, parent2, self.crossing_probability)
                offspring.append(child1)
                offspring.append(child2)

            # Dodanie najlepszego osobnika do nowej populacji potomnej (badanie - sukcesja elitarna)
            #offspring.append(best_chromosome)

            # Mutacja
            mutated_offspring = [self.mutation(chromosome, self.mutation_rate) for chromosome in offspring]

            # Zastąpienie populacji rodzicielskiej populacją potomną
            population = mutated_offspring

        return best_chromosome, best_fitness, best_fitness_values, mean_fitness_values

    # Inicjalizacja populacji
    def init_population(self, pop_size, genome_size):
        population = []
        for i in range(pop_size):
            chromosome = [random.randint(0, 1) for _ in range(genome_size)]
            population.append(chromosome)
        return population

    # Selekcja metodą ruletki
    def roulette_selection(self, population, fitness_scores):
        max_score = sum(fitness_scores)
        selection_probs = [score / max_score for score in fitness_scores]
        selected_indices = []
        for i in range(len(population)):
            r = random.uniform(0, 1)
            current_prob = 0
            for j in range(len(population)):
                current_prob += selection_probs[j]
                if current_prob > r:
                    selected_indices.append(j)
                    break
        selected_population = [population[i] for i in selected_indices]
        return selected_population

    # Krzyżowanie jednopunktowe
    def one_point_crossover(self, parent1, parent2, crossing_probability):
        crossover_point = random.randint(1, len(parent1) - 1)
        if random.uniform(0, 1) > crossing_probability:
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
        else:
            child1 = parent1
            child2 = parent2
        return child1, child2

    # Mutacja
    def mutation(self, chromosome, mutation_rate):
        mutated_chromosome = []
        for gene in chromosome:
            if random.uniform(0, 1) < mutation_rate:
                mutated_chromosome.append(int(not gene))
            else:
                mutated_chromosome.append(gene)
        return mutated_chromosome

    # Wizualizacja
    def visualization(self, best_fitness_values, mean_fitness_values, num_generations):
        fig, axs = plt.subplots(ncols=3, figsize=(15, 10))
        fig.suptitle("Przebieg algorytmu genetycznego", fontsize=16)

        axs[0].plot(best_fitness_values, "y")
        axs[1].plot(mean_fitness_values, "b")
        axs[2].plot(best_fitness_values, "y")
        axs[2].plot(mean_fitness_values, "b")

        axs[2].legend(["Najlepsze wyniki", "Średnie wyniki"], loc=0)

        axs[0].set_xlabel("Generacja")
        axs[1].set_xlabel("Generacja")
        axs[2].set_xlabel("Generacja")

        axs[0].set_ylabel("Wartość najlepszego osobnika")
        axs[1].set_ylabel("Średnia wartość osobników")
        axs[2].set_ylabel("Wartości osobników")

        for sub in axs:
            sub.grid(True)

        plt.show()
        fig.savefig('Result.png')
        plt.close(fig)

def main():
    genetic_solver = GeneticSolver(population_size=100, genome_size=100, mutation_rate=0.01, num_generations=200, crossing_probability=0.3)
    param = genetic_solver.get_parameters()
    print(f"Parametry algorytmu genetycznego: {param}")

    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    best_chromosome, best_fitness, best_fitness_values, mean_fitness_values = genetic_solver.solve()
    stop = time.time()
    if gc_old:
        gc.enable()
    function_time = stop - start

    print(f'Najlepszy osobnik: {best_chromosome}')
    print(f'Maksymalna osiągnięta wysokość: {best_fitness}')
    print(f"Czas działania algorytmu: {function_time}")

    genetic_solver.visualization(best_fitness_values, mean_fitness_values, param['num_generations'])

if __name__ == "__main__":
    main()
