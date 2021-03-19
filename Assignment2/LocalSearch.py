import copy
import random

from Assignment2.constants import Score
from Assignment2.pdp_utils.pdp_utils import feasibility_check, cost_function
from SearchClass import SearchClass
from SolutionDict import SolutionDict


class LocalSearch(SearchClass):
    
    def __init__(self, vehicles:list, calls, probabilities, probaa):
        self.probabilities = [probabilities[0],
                              probabilities[0]+probabilities[0],
                              1-(probabilities[0]+probabilities[0])]
        # 1. Create dummy solution
        super().__init__(vehicles, calls)
        self.probaaa = probaa
        self.init_sol = self.init_sol_creator(probaa)
        # 2. Add appendage of all calls to solution dict, random key.
        self.solman = SolutionDict(self.vehicles)
        # THIS ADDS THE DUMMY VEHICLE JARLE YOU FUCK
        self.solman.add(0, [x for x in self.init_sol.vector if x != 0])

    def local_search(self, iterations, prob, version):
        spag = list()
        spag.append(self.init_sol)
        for _ in range(10):
            spag.append(self._run_search(iterations, prob, version))
        return spag


    def _run_search(self, iterations, prob, version:int):
        """

        :param iterations:
        :param prob:
        :param version: Which group of operators to run - 1 or 2.
        :return:
        """
        # 3. Correctly format initial horrible solution.
        best_sol = self.init_sol

        def random_exchanging(solman:SolutionDict, version:int):
            ranman = random.random()

            if version == 1:
                if ranman < self.probabilities[0]: # 2-exchange
                    solman.swap_random(2)

                elif ranman < self.probabilities[1]: #3-exchange
                    solman.swap_random(3)

                elif ranman < self.probabilities[2]: #1-reinsert
                    solman.reinsert()

            elif version == 2:
                if ranman < self.probabilities[0]: # 2-exchange
                    solman.swap_to_smaller()

                elif ranman < self.probabilities[1]: #3-exchange
                    solman.hefty_scatter()

                else: #1-reinsert
                    solman.reinsert_better(prob)

        # 3. Swap everything around.
        for _ in range(iterations):
            random_exchanging(self.solman, version)
            best_sol = self.score_comparer(best_sol,
                                           self.solman.get_solution_vector(),
                                           prob)

        return best_sol

    def score_comparer(self, best_sol: Score, new_solvec:list, prob):
        feasibility, log = feasibility_check(new_solvec, prob)
        if feasibility:
            new_cost = cost_function(new_solvec, prob)
            if new_cost < best_sol.score:
                return Score(new_solvec, new_cost)
        return best_sol

    def init_sol_creator(self, probaaa) -> Score:
        init_sol = []
        for call in self.calls:
            # Select vehicle
            init_sol += 2*[call]
            # n_nodes = probaaa['n_nodes']
            # random_node = random.randint(1, n_nodes)
            # init_sol += 2*[random_node]

        init_solvec = [0 for _ in range(len(self.vehicles))]
        init_solvec.extend(init_sol)
        init_solscore = cost_function(init_solvec, probaaa)
        return Score(init_solvec, init_solscore)
