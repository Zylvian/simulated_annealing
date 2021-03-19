import copy
import math
from random import random

import ujson

from Assignment2.LocalSearch import LocalSearch
from Assignment2.SolutionDict import SolutionDict
from Assignment2.constants import Score
from Assignment2.helperfuncs import log_time
from Assignment2.pdp_utils.pdp_utils import feasibility_check, cost_function


class SimulatedAnnealing(LocalSearch):


    def __init__(self, temperature, cooling, ls:LocalSearch):

            self.temperature = temperature
            self.cooling = cooling
            #super().__init__(**vars(ls))
            super().__init__(ls.vehicles, ls.calls, ls.probabilities, ls.probaaa)

            # This line copies the initial solution on init, and continually updates to be
            # the "previous state" of the soldict.
            # self.incumb: SolutionDict = copy.deepcopy(self.solman)
            self.incumbman = ujson.dumps(self.solman.soldict)

    # Jarle notes
    # Incumb here is an earlier state of the solution object, SolutionDict
    # Compare new_solvec against self.incumb, and if it is not better, reset self.solman to self.incumb.

    # @log_time
    def score_comparer(self, best_sol:Score, new_solvec:list, prob):
        """Overrides superclass' score_comparer."""
        #
        #load solution
        incumbcurr:dict = ujson.loads(self.incumbman)
        incumbcurr = {int(k):v for (k, v) in incumbcurr.items()}
        incumb_vec = self.solman.get_solution_vector(incumbcurr)

        incumb_score = cost_function(incumb_vec, prob)

        # Check if the new solution is better.
        feasibility, log = feasibility_check(new_solvec, prob)
        new_cost = cost_function(new_solvec, prob)
        diff = new_cost - incumb_score

        if feasibility and diff < 0:
            # If the current solution is feasible and better, update previous solution.
            self.incumbman = ujson.dumps(self.solman.soldict)


            if incumb_score < best_sol.score:
                return Score(incumb_vec, incumb_score)

        # Whether we should update the solution, even though it's not better.
        elif feasibility and random() < math.e**((-diff)/self.temperature):#and the formula
            self.incumbman = ujson.dumps(self.solman.soldict)

        # Else, update the current solution to be the previous solution.
        else:
            self.solman.soldict = incumbcurr

        #endif
        self.temperature = self.cooling * self.temperature
        return best_sol
