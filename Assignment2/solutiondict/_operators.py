###
### OPERATORS
###

## OPERATORS V1

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


## OPEARTORS V2

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


def reinsert_better(self):
    """Checks if traveling from start node is more expensive than other uh node.
    Intensifying."""
    prob = self.prob
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