class SolutionDict:

    def __init__(self, vehicles, prob:dict={}):
        self.vehicles = vehicles
        self.soldict = {}
        self.operator_scores = dict()
        for vehicle in self.vehicles:
            self.soldict[vehicle] = []
        self.prob = prob



    from ._soldict_helpers import exchange_2, exchange_3, move_elem, testaaaa
    from ._soldict_gettersetc import getman, add, _get_random_nr, get_random_keys, get_solution_vector, _get_keys
    from ._operators import swap_to_smaller, swap_random, hefty_scatter, reinsert_better, reinsert
