import copy
import random
from typing import Callable, List

from Assignment2.constants import Score, Weight
from Assignment2.pdp_utils.pdp_utils import feasibility_check, cost_function
from SearchClass import SearchClass
from solutiondict import SolutionDict


class LocalSearch(SearchClass):
    
    def __init__(self, vehicles:list, calls, probabilities, probaa):
        self.probabilities = [probabilities[0],
                              probabilities[0]+probabilities[0],
                              1-(probabilities[0]+probabilities[0])]
        # 1. Create dummy solution
        super().__init__(vehicles, calls)
        self.prob = probaa
        self.init_sol = self.init_sol_creator(self.prob)
        # 2. Add appendage of all calls to solution dict, random key.
        self.solman = SolutionDict(self.vehicles, self.prob)
        # THIS ADDS THE DUMMY VEHICLE JARLE YOU FUCK
        self.solman.add(0, [x for x in self.init_sol.vector if x != 0])

    def local_search(self, iterations, version):
        spag = list()
        spag.append(self.init_sol)
        for _ in range(10):
            spag.append(self._run_search(iterations, version))
        return spag


    def _run_search(self, iterations, version:int):
        """

        :param iterations:
        :param prob:
        :param version: Which group of operators to run - 1 or 2.
        :return:
        """
        # 3. Correctly format initial horrible solution.
        best_sol = self.init_sol
        weights = list()

        funcs = []
        if version == 2:
            funcs = [self.solman.swap_to_smaller, self.solman.hefty_scatter, self.solman.reinsert_better]

        weights = [Weight(funcman.__name__, 1) for funcman in funcs]

        def random_exchanging(solman:SolutionDict):
            ranman = random.random()

            # if version == 1:
            #     if ranman < self.probabilities[0]: # 2-exchange
            #         solman.swap_random(2)
            #         return solman.swap_random.__name__
            #
            #     elif ranman < self.probabilities[1]: #3-exchange
            #         solman.swap_random(3)
            #         return solman.swap_random.__name__
            #
            #     elif ranman < self.probabilities[2]: #1-reinsert
            #         solman.reinsert()
            #         return solman.reinsert.__name__
            #
            # elif version == 2:

            funcman = self.choose_func(funcs, ranman, weights, solman)
            funcman()
            return funcman.__name__



        # 3. Swap everything around.
        for iter_nr in range(iterations):
            op_name = random_exchanging(self.solman)
            best_sol = self.score_comparer(best_sol,
                                           self.solman.get_solution_vector(),
                                           op_name)
            
            if iter_nr % 100 == 0 and iter_nr != 0:
                weights = self.create_new_weights(weights)

        # print(weights)
        return best_sol

    def score_comparer(self, best_sol: Score, new_solvec:list, prob, op_name:str):
        feasibility, log = feasibility_check(new_solvec, prob)
        if feasibility:
            new_cost = cost_function(new_solvec, prob)
            if new_cost < best_sol.score:
                return Score(new_solvec, new_cost)
        return best_sol



    def choose_func(self, funcs:list, ranman, weights:list, solman:SolutionDict) -> Callable[[], None]:
        # IMPLEMENT WEIGHTS SOMEHOW
        if weights:
            random_func_name = random.choices(population=[w.op_name for w in weights],
                           weights=[w.weight for w in weights],
                           k=1)[0]
            actual_func = getattr(solman, random_func_name)
            return actual_func
            #
            # print("aaa")
            # weights_sum = sum([w.weight for w in weights])
            # sorted_weights = sorted(weights, key=lambda w: w.weight)
            # num_man = random.randint(0, weights_sum)
            # # print(sorted_weights)
            #
            #
            # for w in sorted_weights:
            #     if num_man < w.weight:
            #         return getattr(solman, w.op_name)


    def create_new_weights(self, old_weights:List[Weight]):
        new_op_scores = self.solman.operator_scores
        # self.solman.operator_scores = dict()
        r = 0.4

        new_weights = list()

        for w in old_weights:
            op_score = new_op_scores[w.op_name]['score']
            op_times_used = new_op_scores[w.op_name]['times_used']
            new_weight = w.weight*(1-r) + r*(op_score/op_times_used)

            new_weights.append(Weight(w.op_name, new_weight))

        return new_weights


    def dict_to_weights(self, weights_dict):
        return [Weight(*a) for a in weights_dict.items()]

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

