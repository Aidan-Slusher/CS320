import sys
import math
from util import cost, valid_path, best_path
from init_pop import init_pop
from load_dist import load_dist
from random import sample, randint, shuffle
from functools import partial

MIN_INIT_POPULATION = 20
MIN_POPULATION = 6


def _initial_size(population_size):
    population_size = population_size if population_size is not None else MIN_INIT_POPULATION

    psf = math.factorial(population_size)
    log_psf = int(math.log(psf, 2))
    if log_psf < MIN_INIT_POPULATION:
        return MIN_INIT_POPULATION
    return log_psf


def ga_tsp(initial_population, distances, generations):
    if initial_population is None or distances is None or generations is None or generations <= 0:
        return None

    population_size = len(initial_population)
    for _ in range(generations):
        children = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(initial_population, distances)
            child = crossover(parent1, parent2)
            children.append(child)
        initial_population = select_fittest(initial_population, children, distances)
    return best_path(initial_population, distances)


def select_parents(population, distances):
    parents = sample(population, 2)
    return parents


def crossover(parent1, parent2):
    crossover_point = randint(0, len(parent1) - 1)
    child = list(parent1[:crossover_point])
    for city in parent2:
        if city not in child:
            child.append(city)
    return tuple(child)


def select_fittest(population, children, distances):
    merged_population = population + children
    return sorted(merged_population, key=partial(cost, distances=distances))
