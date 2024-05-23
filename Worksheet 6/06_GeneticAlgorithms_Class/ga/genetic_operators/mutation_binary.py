
from ga.individual_bit_vector import BitVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm


class MutationBinary(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    # TODO
    def mutate(self, individual: BitVectorIndividual) -> None:
        num_genes = len(individual.genome)
        for i in range(num_genes):
            if GeneticAlgorithm.rand.random() < self.probability:
                individual.genome[i] = not individual.genome[i]

    def __str__(self):
        return "Binary mutation (" + f'{self.probability}' + ")"
