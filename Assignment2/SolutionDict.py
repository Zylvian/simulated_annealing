import copy
import random
from typing import Tuple, Any


class SolutionDict:

    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.soldict = {}
        for vehicle in self.vehicles:
            self.soldict[vehicle] = []


    def move_elem(self, key_from:int, key_to:int, elem:int, pos_to:int=None, pos_from:int=None):
        try:
            self.soldict[key_from].remove(elem)
        except Exception as e:
            # If list is already empty
            pass

        if not elem == -1:
            # If positions are not defined, insert randomly.
            if not pos_from and not pos_to:
                #Inserts element at random position.
                index = random.randrange(len(self.soldict[key_to]) + 1)
                self.soldict[key_to].insert(
                    index,
                    elem)
                # self.soldict[key2].append(elem)
            else:
                self.soldict[key_to].insert(
                    pos_to,
                    elem)

    def exchange_2(self, key1:int, key2:int, elem1:int, elem2:int):
            self.move_elem(key1, key2, elem1)
            self.move_elem(key2, key1, elem2)

    def exchange_3(self, key1:int, key2:int, key3:int,
                   elem1:int, elem2:int, elem3:int
                   ):
            self.move_elem(key1, key2, elem1)
            self.move_elem(key2, key3, elem2)
            self.move_elem(key3, key1, elem3)

    def getman(self, key):
        return self.soldict[key]

    def add(self, key, elem):
        self.soldict[key] = elem

    def _get_keys(self) -> list:
        return list(self.soldict)

    def get_random_keys(self, amount:int, not_zero:bool=True) -> Tuple[Any, ...]:
        # Note: list(dict) gets a list of all the keys. Idk why
        if not not_zero:
            return tuple(random.sample(list(self.soldict), amount))
        else:
            dictkeys = list(self.soldict)
            dictkeys.remove(0)
            return tuple(random.sample(dictkeys, amount))

    ###
    ### OPERATORS
    ###

    def swap_random(self, times):
        """
        Random swapping operator.
        :param times: number of elements to swap
        :return:  none
        """
        vec1, vec2, vec3 = self.get_random_keys(3)
        nr_1 = self._get_random_nr(vec1)
        nr_2 = self._get_random_nr(vec2)
        nr_3 = self._get_random_nr(vec3)

        if times == 2:
            self.exchange_2(vec1, vec2, nr_1, nr_2)
            self.exchange_2(vec1, vec2, nr_1, nr_2)
        elif times == 3:
            self.exchange_3(vec1, vec2, vec3, nr_1, nr_2, nr_3)
            self.exchange_3(vec1, vec2, vec3, nr_1, nr_2, nr_3)
        else:
            print("idk what happened")

    def reinsert(self):
        """
        Reinsert element back in solution at random place.
        :return: none
        """
        vec1 = self.get_random_keys(1)
        nr_1 = self._get_random_nr(vec1[0])
        self.move_elem(vec1[0], vec1[0], nr_1)


    def swap_to_smaller(self):
        """Swap an order from vehicle with many calls to vehicle with few calls.
        Diversifying. """

        smallest_key = min(self.soldict, key=lambda x: len(set(self.soldict[x])))
        largest_key = max(self.soldict, key=lambda x: len(set(self.soldict[x])))

        if smallest_key != largest_key:
            # Get random order number from largest list.
            order_nr = self._get_random_nr(largest_key)
            for _ in range(2):
                # We have to move 2, as all orders are in numbers of 2.
                self.move_elem(largest_key, smallest_key, order_nr)

    def reinsert_better(self, prob):
        """Checks if traveling from start node is more expensive than other uh node.
        Intensifying."""
        vecs = self.get_random_keys(1, not_zero=True)
        vec1 = vecs[0]
        vec_orderlist = self.getman(vec1)
        if not vec_orderlist:
            return

        first_travel_costs = prob['FirstTravelCost']
        first_call = vec_orderlist[0]

        cargo_inf = prob['Cargo']
        cargo_call_origin_node = int(cargo_inf[first_call-1][1])

        vehicle_travel_costs = first_travel_costs[vec1-1]
        first_order_init_cost = vehicle_travel_costs[cargo_call_origin_node-1]

        # To check vehicle 1, we have to look in index 0.
        # This creates a problem, as one of the keys are 0.
        # try:
        #     first_order_init_cost = first_travel_costs[vec1-1][first_order]
        # except:
        #     pass

        for i, call in enumerate(vec_orderlist):
            if call != first_call:
                # To check order 3, we have to look in the 2nd
                call_start_node = int(cargo_inf[call-1][1])
                curr_init_cost = first_travel_costs[vec1-1][call_start_node-1]
                if curr_init_cost < first_order_init_cost:
                    self.move_elem(vec1, vec1, call, pos_to=0)

    def hefty_scatter(self):
        """Take all calls from a vehicle, and randomly distribute.
        Diversifying."""
        vec_from = self.get_random_keys(1)[0]

        while self.getman(vec_from): # dict lookup takes O(1) time
            vec_to = self.get_random_keys(1)[0]
            if vec_to != vec_from:
                order_nr = self._get_random_nr(vec_from)
                # Move twice as orders are in order of 2.
                self.move_elem(vec_from, vec_to, order_nr)
                self.move_elem(vec_from, vec_to, order_nr)



    ###

    def _get_random_nr(self, vec):
        """Returns random vehicle number from list of calls."""
        # if self.soldict[vec]:
        return random.choice(self.getman(vec))
        # else:
        #     return -1

    def get_solution_vector(self, external_sol=None):
        # Make dict into vector
        if external_sol:
            the_items = external_sol.items()
        else:
            the_items = self.soldict.items()
        solution_vector = []
        for curr_v, curr_calls in the_items:
            solution_vector.extend(curr_calls)
            solution_vector.append(0)

        # Remove last 0
        solution_vector = solution_vector[:-1]

        return solution_vector

    def incumb_to_dict(self, incumb):
        # Rewrite the soldict based on the incumb aka new solution
        pass

