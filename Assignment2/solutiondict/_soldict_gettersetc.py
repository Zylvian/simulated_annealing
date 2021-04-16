import random
from typing import Tuple, Any


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

def _get_random_nr(self, vec):
    """Returns random vehicle number from list of calls."""
    # if self.soldict[vec]:
    return random.choice(self.getman(vec))
    # else:
    #     return -1
