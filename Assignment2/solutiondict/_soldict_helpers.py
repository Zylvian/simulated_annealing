import random

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

def testaaaa(self, spamann):
    print(self.vehicles)
    print(spamann)