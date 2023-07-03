#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:59:54 2023

@author: gonzalo
"""
import matplotlib.pyplot as plt

def plot_fitness_progress(fitness_progress):
    generations = range(len(fitness_progress))
    plt.plot(generations, fitness_progress)
    plt.xlabel('Generaciones')
    plt.ylabel('Aptitud promedio')
    plt.title('Evolución de la aptitud promedio en el algoritmo genético')
    plt.show()

# Parámetros del algoritmo genético
population_size = 200
generations = 200
mutation_rate = 0.1

# Inicializar población y lista para almacenar la aptitud promedio de cada generación
population = init_population(population_size, parameter_ranges)
fitness_progress = []

# Ejecutar el algoritmo genético
for _ in range(generations):
    fitness_values = [fitness(individual) for individual in population]
    average_fitness = np.mean(fitness_values)
    fitness_progress.append(average_fitness)

    parents = select_parents(population, fitness_values)
    offspring = []

    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutate(child1, mutation_rate, parameter_ranges))
        offspring.append(mutate(child2, mutation_rate, parameter_ranges))

    population = offspring

# Graficar la evolución de la aptitud promedio
plot_fitness_progress(fitness_progress)

