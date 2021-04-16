import random
from typing import Tuple, Any
import numpy as np

class SolutionDictNumpy:

    def __init__(self, vehicles: list, calls:list):
        self.vehicles = vehicles
        # self.solarr = np.array(vehicles, np.int32).reshape(len(vehicles), 1)
        self.solarr = np.empty([len(vehicles), len(calls)])


    def move_elem(self, key_from:int, key_to:int, elem:int):
        try:
            self.soldict[key_from].remove(elem)
        except Exception as e:
            # If list is already empty
            pass

        if not elem == -1:
            #Inserts element at random position.
            index = random.randrange(len(self.soldict[key_to]) + 1)
            self.soldict[key_to].insert(
                index,
                elem)
            # self.soldict[key2].append(elem)

    def exchange_2(self, key1:int, key2:int, elem1:int, elem2:int):
            self.move_elem(key1, key2, elem1)
            self.move_elem(key2, key1, elem2)

    def exchange_3(self, key1:int, key2:int, key3:int,
                   elem1:int, elem2:int, elem3:int
                   ):
            self.move_elem(key1, key2, elem1)
            self.move_elem(key2, key3, elem2)
            self.move_elem(key3, key1, elem3)

    def add(self, key, elem):
        self.soldict[key] = elem

    def get_random_keys(self, amount:int) -> Tuple[Any, ...]:
        # Note: list(dict) gets a list of all the keys. Idk why
        return tuple(random.sample(list(self.soldict), amount))

    ###
    ### OPERATORS
    ###


    def swap_to_smaller(self):
        """Swap an order from big to small list"""

        smallest_key = min(self.soldict, key=lambda x: len(set(self.soldict[x])))
        largest_key = max(self.soldict, key=lambda x: len(set(self.soldict[x])))


        if smallest_key != largest_key:
            # Get random order number from largest list.
            order_nr = self._get_random_nr(largest_key)
            for _ in range(2):
                # We have to move 2, as all orders are in numbers of 2.
                self.move_elem(largest_key, smallest_key, order_nr)

    ###

    def _get_random_nr(self, vec):
        """Returns random vehicle number from list of calls."""
        if self.soldict[vec]:
            return random.choice(self.soldict[vec])
        else:
            return -1

    def get_solution_vector(self):
        # Make dict into vector
        solution_vector = []
        for curr_v, curr_calls in self.soldict.items():
            solution_vector.extend(curr_calls)
            solution_vector.append(0)

        # Remove last 0
        solution_vector = solution_vector[:-1]

        return solution_vector

    def incumb_to_dict(self, incumb):
        # Rewrite the soldict based on the incumb aka new solution
        pass

