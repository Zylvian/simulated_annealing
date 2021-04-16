import statistics
import time

from Assignment2.SimulatedAnnealing import SimulatedAnnealing
from RandomSearch import RandomSearch
from LocalSearch import LocalSearch
from constants import paths, N_ITERATIONS, Score
from pdp_utils.pdp_utils.Utils import load_problem, feasibility_check, cost_function
import logging

class ProblemSolver:

    def __init__(self):
        logging.basicConfig(filename="HJELP.log", level=logging.DEBUG)

    def run_search(self):
        for path in paths: # Load each problem
            prob = load_problem(path)

            vehicles = [a for a in range(1, prob['n_vehicles']+1)] # Vehicles + dummy vehicle
            calls = [a for a in range(1, prob['n_calls']+1)]

            # Random Search
            # rs = RandomSearch(vehicles, calls)
            # rs_scores = rs.run_search(prob, N_ITERATIONS)
            #
            # self.score_printer(rs_scores, path)

            # Local Search
            currtime = time.time()
            probabilities = [0.2, 0.2]
            local_search = LocalSearch(vehicles, calls, probabilities, prob)
            # ls_scores = ls.local_search(N_ITERATIONS, prob)
            # self.score_printer(ls_scores, path + ' - Local Search', currtime)

            # Simulated Annealing
            currtime = time.time()
            temp = 10000
            cooling = 0.99999
            sa = SimulatedAnnealing(temp, cooling, local_search)
            print("Starting simulated annealing...")
            sa_scores = sa.local_search(N_ITERATIONS, 2)
            # print(sa_scores)
            self.score_printer(sa_scores, path + ' - Simulated Annealing', currtime)

    def score_printer(self, solution_scores, path, currtime):

        # Printout
        # print(solution_scores)
        first_sol_score = solution_scores[0].score
        print(solution_scores)
        best_sol:Score = min(solution_scores, key=lambda x: x.score)
        avg_sol_score = statistics.mean([a.score for a in solution_scores])
        improv_score = 100 * (first_sol_score - best_sol.score) / first_sol_score
        runtime = f'{int(time.time() - currtime)} s'
        runtime_ms = (time.time() - currtime)*1000

        print(f'RUNTIME FOR \'{path}\'\nAverage cost: {int(avg_sol_score)}\nBest cost: {best_sol.score}\n'
                f'Best vector: {best_sol.vector}\n'
              f'Improvement: {round(improv_score, 1)}%\n'
              f'Runtime: {runtime}\n'
              f'Average runtime: {runtime}\n')

import cProfile
cProfile.run('ProblemSolver().run_search()', sort='cumtime')

# import cProfile, pstats
# profiler = cProfile.Profile()
# profiler.enable()
# ProblemSolver().run_search()
# profiler.disable()
# stats = pstats.Stats(profiler)
# stats.strip_dirs()
# stats.sort_stats('cumtime')
# stats.print_stats()