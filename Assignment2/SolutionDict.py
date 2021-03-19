import copy
import random
from typing import Tuple, Any


class SolutionDict:

    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.soldict = {}
        for vehicle in self.vehicles:
            self.soldict[vehicle] = []

    def overwrite_sol(self, new_sol: dict):
        self.soldict = copy.deepcopy(new_sol)


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

