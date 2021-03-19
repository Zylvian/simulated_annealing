class SearchClass:

    def __init__(self, vehicles: list, calls: list):
        self.vehicles = vehicles
        self.calls = calls

    def dict_to_sol(self, soldict):
        # Make dict into vector
        solution_vector = []
        for curr_v, curr_calls in soldict.items():
            solution_vector.extend(curr_calls)
            solution_vector.append(0)

        # Remove last 0
        solution_vector = solution_vector[:-1]

        return solution_vector