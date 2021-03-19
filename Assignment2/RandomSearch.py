import copy
from random import choice, randint

from SearchClass import SearchClass
from constants import Score, N_ITERATIONS
from pdp_utils.pdp_utils import feasibility_check, cost_function


class RandomSearch(SearchClass):

    def run_search(self, prob, iterations:int):

        def iteration_run(vehicles, dummy_run: bool):
            solution_dict = {}
            nr_vecs = len(vehicles) # +1 ADDS THE DUMMY THICC VEHICLE

            if not dummy_run:
                for vehicle in vehicles:
                    solution_dict[vehicle] = []
            else:
                vehicles = [0]
                solution_dict[0] = []

            # Go through each call
            for call in self.calls:
                # Select vehicle
                vehicle = choice(vehicles)
                if solution_dict[vehicle]:
                    solution_dict[vehicle].insert(randint(0, len(solution_dict[vehicle]) - 1), call)
                    solution_dict[vehicle].insert(randint(0, len(solution_dict[vehicle]) - 1), call)
                else:
                    solution_dict[vehicle] = [call, call]

            # # Make dict into vector
            # solution_vector = []
            # for curr_v, curr_calls in solution_dict.items():
            #     solution_vector.extend(curr_calls)
            #     solution_vector.append(0)
            #
            # # Remove last 0
            # solution_vector = solution_vector[:-1]
            solution_vector = self.dict_to_sol(solution_dict)

            ## Final
            ## Only include feasible.

            if dummy_run: # Add zeroes to start of the only vector.
                new_sol_vector = [0 for _ in range(1, nr_vecs)]
                new_sol_vector.extend(solution_vector)
                solution_vector = new_sol_vector

            feasibility, log = feasibility_check(solution_vector, prob)
            if feasibility:
                cost = cost_function(solution_vector, prob)
                return Score(solution_vector, cost)

        #####

        solution_scores = []
        curr_vehicles_thing = copy.copy(self.vehicles)
        curr_vehicles_thing.append(0)
        # Initial run, all outsourced

        dummy_score = iteration_run(curr_vehicles_thing, True)
        solution_scores.append(dummy_score)
        # All subsequent runs.
        for iteration in range(iterations):
            # First run

            iter_score = iteration_run(curr_vehicles_thing, False)
            solution_scores.append(iter_score)

        solution_scores = list(filter(None, solution_scores))

        return solution_scores

    # # Printout
    # print(solution_scores)
    # first_sol_score = solution_scores[0].score
    # best_sol:Score = min(solution_scores, key=lambda x: x.score)
    # avg_sol_score = statistics.mean([a.score for a in solution_scores])
    # improv_score = 100 * (first_sol_score - best_sol.score) / first_sol_score
    # runtime = (time.time() - currtime)*1000
    #
    # print(f'RUNTIME FOR \'{path}\'\nAverage cost: {int(avg_sol_score)}\nBest cost: {best_sol.score}\n'
    #         f'Best vector: {best_sol.vector}\n'
    #       f'Improvement: {round(improv_score, 1)}%\nRuntime: {runtime} ms\n')