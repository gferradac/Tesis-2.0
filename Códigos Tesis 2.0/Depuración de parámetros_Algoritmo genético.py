#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:58:20 2023

@author: gonzalo
"""

import random
import numpy as np
from scipy.integrate import odeint

# Definir la función de aptitud (fitness) para evaluar la probabilidad de oscilación en O
def fitness(params):
    d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a = params

    def m(G, O):
        return mmax * (G / (G + KGm)) * (O / (O + KOm))

    def n(G, O):
        return nmax * (G / (G + KGn)) * (O / (O + KOn))

    def ode_model(X, t):
        C, D, G, O = X

        dC = n(G, O) * C * D - d * C
        dD = m(G, O) * D - a * C * D - d * D
        dG = (Gin - G) * d - (m(G, O) / YGD) * D - (n(G, O) / YGC) * C
        dO = (Osat - O) * k - (m(G, O) / YOD) * D - (n(G, O) / YOC) * C

        return [dC, dD, dG, dO]

    # Condiciones iniciales
    IC = [1, 1, 1, 1]

    # Tiempo de integración
    t = np.linspace(0, 1000, 1000)

    # Resolver el sistema de ecuaciones diferenciales
    sol = odeint(ode_model, IC, t)

    # Calcular la probabilidad de oscilación en O
    oscillations = np.sum(np.diff(np.signbit(np.diff(sol[:, 3])))) > 0
    probability = np.mean(oscillations)

    return probability

# Función de inicialización de la población
def init_population(population_size, parameter_ranges):
    population = []
    for _ in range(population_size):
        individual = [random.uniform(low, high) for low, high in parameter_ranges]
        population.append(individual)
    return population

# Función de selección de padres mediante torneo binario
def select_parents(population, fitness_values):
    parents = []
    for _ in range(len(population)):
        tournament_indices = random.sample(range(len(population)), 2)
        fitness1 = fitness_values[tournament_indices[0]]
        fitness2 = fitness_values[tournament_indices[1]]
        if fitness1 > fitness2:
            parent = population[tournament_indices[0]]
        else:
            parent = population[tournament_indices[1]]
        parents.append(parent)
    return parents

# Función de cruce de dos padres para generar dos descendientes
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Función de mutación de un individuo
def mutate(individual, mutation_rate, parameter_ranges):
    mutated_individual = individual.copy()
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            low, high = parameter_ranges[i]
            mutated_individual[i] = random.uniform(low, high)
    return mutated_individual

# Función para encontrar el conjunto de parámetros óptimo utilizando el algoritmo genético
def optimize_parameters(population_size, parameter_ranges, generations, mutation_rate):
    population = init_population(population_size, parameter_ranges)
    best_fitness = -1
    best_individual = None

    for _ in range(generations):
        fitness_values = [fitness(individual) for individual in population]

        if max(fitness_values) > best_fitness:
            best_fitness = max(fitness_values)
            best_individual = population[np.argmax(fitness_values)]

        parents = select_parents(population, fitness_values)
        offspring = []

        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            offspring.append(mutate(child1, mutation_rate, parameter_ranges))
            offspring.append(mutate(child2, mutation_rate, parameter_ranges))

        population = offspring

    return best_individual

# Rango de los parámetros [d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a]
parameter_ranges = [(0.1, 0.2), (0, 0.5), (0.5, 1), (0, 0.2), (0, 0.2), (0, 0.01), (0, 0.01), (8, 10), (0.5, 1), (0, 0.2), (0, 0.2), (0.5, 1), (1, 1.5), (7, 10), (0, 0.1)]

# Parámetros del algoritmo genético
population_size = 100
generations = 100
mutation_rate = 0.1

# Ejecutar el algoritmo genético para encontrar los parámetros óptimos
best_parameters = optimize_parameters(population_size, parameter_ranges, generations, mutation_rate)

print("Los parámetros óptimos son:")
print("d =", best_parameters[0])
print("mmax =", best_parameters[1])
print("nmax =", best_parameters[2])
print("KGm =", best_parameters[3])
print("KOm =", best_parameters[4])
print("KGn =", best_parameters[5])
print("KOn =", best_parameters[6])
print("Gin =", best_parameters[7])
print("YGC =", best_parameters[8])
print("YGD =", best_parameters[9])
print("YOC =", best_parameters[10])
print("YOD =", best_parameters[11])
print("k =", best_parameters[12])
print("Osat =", best_parameters[13])
print("a =", best_parameters[14])