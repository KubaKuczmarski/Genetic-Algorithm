**[PL]**

# Algorytm Genetyczny

Algorytmy genetyczne to popularna rodzina algorytmów heurystycznych, inspirowanych procesem ewolucji w przyrodzie, które stosuje się do rozwiązywania problemów optymalizacyjnych. Algorytmy genetyczne operują na populacji rozwiązań, reprezentowanych przez chromosomy, które są następnie
ewoluowane w kolejnych generacjach.

Podstawowy algorytm genetyczny składa się z następujących kroków:
  1. Inicjalizacja populacji początkowej - losowe utworzenie populacji początkowej rozwiązań, reprezentowanych przez chromosomy.
  2. Selekcja - wybór najlepszych rozwiązań z populacji, które będą przekazywane do kolejnej generacji. Najczęściej stosuje się tu selekcję metodą turniejową, ruletki      lub rankingową.
  3. Krzyżowanie - losowe łączenie chromosomów najlepszych osobników, aby utworzyć nowe rozwiązania w kolejnej populacji. Najczęściej stosuje się tu krzyżowanie jedno-      lub wielopunktowe.
  4. Mutacja - losowa zmiana wartości jednego lub kilku genów w chromosomie, co zwiększa szansę na znalezienie nowych, lepszych rozwiązań.
  5. Ocena - obliczenie wartości funkcji celu dla nowych osobników.
  6. Sukcesja -zastępowanie populacji nowymi osobnikami. Najczęściej stosowane rodzaje sukcesji to generacyjna lub elitarna.

Algorytm polega na powtórzeniu kroków 2-6 dla każdej kolejnej generacji, aż do spełnienia kryterium zakończenia (np. osiągnięcia zadanego poziomu jakości rozwiązania lub przekroczenia maksymalnej liczby generacji).

Algorytmy genetyczne znajdują zastosowanie w wielu dziedzinach, takich jak optymalizacja procesów przemysłowych, planowanie tras w logistyce, projektowanie sieci neuronowych czy optymalizacja parametrów modeli w uczeniu maszynowym.

# Zadanie

Tematem projektu jest implementacja oraz zbadanie wpływu hiperparametrów na algorytmu genetycznego z mutacją, selekcją ruletkową, krzyżowaniem jednopunktowym oraz sukcesją generacyjną w odniesieniu do optymalizacji zysku w problemie sterowania dronem. Zysk definiowany jest jako maksymalna wysokości jaką osiągnie dron.

**Selekcją ruletkową** polega na wyborze osobników do krzyżowania i mutacji na podstawie wartości ich funkcji celu. Im wyższa wartość funkcji celu, tym większe prawdopodobieństwo wyboru danego osobnika.

**Krzyżowanie jednopunktowe** polega na losowym wyborze punktu przecięcia chromosomu, z dwóch osobników rodzicielskich powstają dwa osobniki potomne przez prostą wymianę części chromosomów rodziców

**Sukcesja generacyjna** polega na całkowitej wymianie populacji w każdej kolejnej generacji. W tym przypadku najlepsi osobnicy nie są automatycznie zachowywani w kolejnej populacji, co oznacza, że ich geny mogą zostać utracone w procesie selekcji i krzyżowania. Sukcesja generacyjna pozwala na większą różnorodność w populacji, co może prowadzić do znalezienia lepszych rozwiązań.


# Opis problemu

Zadaniem jest optymalizacja zysku w następującym problemie sterowania dronem: Kwant czasu trwa 0.1s. Dron może mieć silnik włączony albo wyłączony przez pierwsze 10 sekund, następnie ma silnik cały czas wyłączony. Jeżeli dron ma silnik włączony, to nadaje mu przyspieszenie 30 𝑚/𝑠^2. Ponadto działa na niego grawitacja (10 𝑚/𝑠^2) oraz spowolnienie wynikające z tarcie wynoszące −0.1 𝑚/𝑠^2 · 𝑠/𝑚 𝑣, gdzie 𝑣 to aktualna prędkość. Zysk jest równy maksymalnej wysokości jaką osiągnie dron (licząc w metrach) minus 1500 jeżeli w chwili uderzenia w ziemię prędkość drona przekroczy 20 𝑚/𝑠. Pojedyncza próba trwa do momentu aż dron spadnie na ziemię.

Pseudokod problemu

![image](https://user-images.githubusercontent.com/113121214/232013177-cd852bf7-4924-4861-b429-96d36c421f9d.png)



=========================================================================================

**[ENG]**

# Genetic Algorithm

Genetic algorithms are a popular family of heuristic algorithms inspired by the process of evolution in nature, which are used to solve optimization problems. Genetic algorithms operate on a population of solutions, represented by chromosomes, which are then evolved in successive generations.

The basic genetic algorithm consists of the following steps:
  1. Initialization of the initial population - randomly creating an initial population of solutions, represented by chromosomes.
  2. Selection - choosing the best solutions from the population, which will be passed on to the next generation. Tournament, roulette, or rank-based selection is usually applied here.
  3. Crossover - randomly combining the chromosomes of the best individuals to create new solutions in the next population. One-point or multi-point crossover is usually used here.
  4. Mutation - randomly changing the value of one or several genes in the chromosome, increasing the chance of finding new and better solutions.
  5.Evaluation - calculating the value of the objective function for the new individuals.
  6. Succession - replacing the population with new individuals. The most commonly used types of succession are generational or elitist.

The algorithm consists of repeating steps 2-6 for each successive generation until the termination criterion is met (e.g., achieving a desired level of solution quality or exceeding the maximum number of generations).

Genetic algorithms find application in many fields, such as optimizing industrial processes, planning routes in logistics, designing neural networks, or optimizing model parameters in machine learning.

# Task
The project topic is the implementation and investigation of the impact of hyperparameters on a genetic algorithm with mutation, roulette selection, one-point crossover, and generational succession in relation to profit optimization in a drone control problem. Profit is defined as the maximum height that the drone will reach.

**Roulette selection** involves selecting individuals for crossover and mutation based on the value of their objective function. The higher the value of the objective function, the greater the probability of selecting a particular individual.

**One-point crossover** involves randomly choosing a crossover point in the chromosome, from which two offspring individuals are generated by a simple exchange of parts of the parents' chromosomes.

**Generational succession** involves a complete exchange of the population in each successive generation. In this case, the best individuals are not automatically preserved in the next population, which means that their genes may be lost in the selection and crossover process. Generational succession allows for greater diversity in the population, which can lead to finding better solutions.

# Problem Description

The task is to optimize profit in the following drone control problem: The time quantum is 0.1s. The drone can have its engine on or off for the first 10 seconds, then it has the engine off all the time. If the drone has the engine on, it has an acceleration of 30 𝑚/𝑠^2. Additionally, gravity (10 𝑚/𝑠^2) and deceleration due to friction of −0.1 𝑚/𝑠^2 · 𝑠/𝑚 𝑣, where 𝑣 is the current velocity, act on it. Profit is equal to the maximum height that the drone will reach (measured in meters) minus 1500 if the drone is on during the first 10 seconds, or minus 2000 if the drone is off.

# Pseudocode of the problem

![image](https://user-images.githubusercontent.com/113121214/232013177-cd852bf7-4924-4861-b429-96d36c421f9d.png)

