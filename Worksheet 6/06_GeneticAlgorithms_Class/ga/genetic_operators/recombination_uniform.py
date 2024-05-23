
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm


class RecombinationUniform(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    # TODO
    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        for i in range(ind1.num_genes):
            if GeneticAlgorithm.rand.random() < self.probability:
                ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

    def __str__(self):
        return "Uniform recombination (" + f'{self.probability}' + ")"
