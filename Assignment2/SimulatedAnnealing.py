import copy
import math
from random import random

import ujson

from Assignment2.LocalSearch import LocalSearch
from Assignment2.solutiondict import SolutionDict
from Assignment2.constants import Score
from Assignment2.helperfuncs import log_time
from Assignment2.pdp_utils.pdp_utils import feasibility_check, cost_function





class SimulatedAnnealing(LocalSearch):


    def __init__(self, temperature, cooling, ls:LocalSearch):

            self.temperature = temperature
            self.cooling = cooling
            #super().__init__(**vars(ls))
            super().__init__(ls.vehicles, ls.calls, ls.probabilities, ls.prob)

            # This line copies the initial solution on init, and continually updates to be
            # the "previous state" of the soldict.
            # self.incumb: solutiondict = copy.deepcopy(self.solman)
            self.incumbman = ujson.dumps(self.solman.soldict)
            self.old_sols = list()

    # Jarle notes
    # Incumb here is an earlier state of the solution object, solutiondict
    # Compare new_solvec against self.incumb, and if it is not better, reset self.solman to self.incumb.

    # There are 3 things in play:
    # The incumb: not necessarily the best, but it's what we compare against.
    # The best: the one we know is best for a fact.
    # The new: new solution vector post-operating.

    # @log_time
    def score_comparer(self, best_sol:Score, new_solvec:list, op_name:str):
        """Overrides superclass' score_comparer."""
        # NOTE: WE CAN LOWEST POSSIBLE SCORE LOL


        #load solution
        incumbcurr:dict = ujson.loads(self.incumbman)
        incumbcurr = {int(k):v for (k, v) in incumbcurr.items()}
        incumb_vec = self.solman.get_solution_vector(incumbcurr)

        incumb_cost = cost_function(incumb_vec, self.prob)
        new_cost = cost_function(new_solvec, self.prob)
        # Check if the new solution is better.
        feasibility, log = feasibility_check(new_solvec, self.prob)
        diff = new_cost - incumb_cost

        # Checks for old solutions.
        is_completely_new = self.is_new_solution(new_solvec)
        if is_completely_new:
            self.old_sols.append(str(new_solvec))

        if op_name not in self.solman.operator_scores:
            self.solman.operator_scores[op_name] = {'score': 0, 'times_used': 0}

        self.solman.operator_scores[op_name]['times_used'] += 1

        if feasibility and diff < 0:
            # If the new solution is feasible and better than the incumb, update incumb.
            self.incumbman = ujson.dumps(self.solman.soldict)

            # If the cost of previous solution(incumb) is lower, return that as best solution,
            # EVEN after updating the incumb.

            # NEW_COST is basically incumb_cost at this point.
            # Task says f(incumb) at this point, which would be new_cost.
            if new_cost < best_sol.score:
                if is_completely_new:
                    self.update_op_score(op_name, 4)

                else:
                    self.update_op_score(op_name, 2)

                #return Score(incumb_vec, incumb_cost)
                return Score(new_solvec, new_cost)

        # Whether we should update the solution, even though it's not better.
        elif feasibility and random() < math.e**((-diff)/self.temperature):#and the formula
            self.incumbman = ujson.dumps(self.solman.soldict)

        # Else, update the current solution to be the previous solution.
        else:
            self.solman.soldict = incumbcurr

        #endif

        # If solution is new but sucks ass.
        if is_completely_new:
            self.update_op_score(op_name, 1)

        self.temperature = self.cooling * self.temperature
        return best_sol

    def is_new_solution(self, new_sol_vec:list):
        if str(new_sol_vec) not in self.old_sols:
            return False
        else:
            return True

    def update_op_score(self, op_name, val):
        self.solman.operator_scores[op_name]['score'] += val

    # If the current solution is feasible and better, update incumb.
    # def better_and_feasible(self, incumb_score, best_sol, incumb_vec):
    #         self.incumbman = ujson.dumps(self.solman.soldict)
    #
    #         if incumb_score < best_sol.score:
    #             return Score(incumb_vec, incumb_score)

    # def score_comparer_old(self, best_sol:Score, new_solvec:list, prob):
    #     """Overrides superclass' score_comparer."""
    #     #
    #     #load solution
    #     incumbcurr:dict = ujson.loads(self.incumbman)
    #     incumbcurr = {int(k):v for (k, v) in incumbcurr.items()}
    #     incumb_vec = self.solman.get_solution_vector(incumbcurr)
    #
    #     incumb_score = cost_function(incumb_vec, prob)
    #     # Check if the new solution is better.
    #     feasibility, log = feasibility_check(new_solvec, prob)
    #     new_cost = cost_function(new_solvec, prob)
    #     diff = new_cost - incumb_score
    #
    #     if feasibility and diff < 0:
    #         # If the current solution is feasible and better, update previous solution.
    #         self.incumbman = ujson.dumps(self.solman.soldict)
    #         if incumb_score < best_sol.score:
    #             return Score(incumb_vec, incumb_score)
    #
    #     # Whether we should update the solution, even though it's not better.
    #     elif feasibility and random() < math.e**((-diff)/self.temperature):#and the formula
    #         self.incumbman = ujson.dumps(self.solman.soldict)
    #
    #     # Else, update the current solution to be the previous solution.
    #     else:
    #         self.solman.soldict = incumbcurr
    #
    #     #endif
    #     self.temperature = self.cooling * self.temperature
    #     return best_sol


