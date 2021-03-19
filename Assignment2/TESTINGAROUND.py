# vec1 = [1]
# vec2 = [3,3]
# vec3 = [1,1,1,1]
# smallest_list = max([vec1, vec2, vec3], key=len)
# print(smallest_list)
#
# dictman = {1: ["asd"], 2: ["asdasd"], 3: [1,2]}
# # get_list = lambda keyman: dictman.get(keyman)
# #
# # a, b, c = tuple(map(get_list, [1,2,3]))
# # print(a)
# largest_key = max(dictman, key=dictman.get)
# print(largest_key)

# import numpy as np
# # print(np.arrange(3).reshape(3,3))
# vehicles = [0, 1, 2, 4, 5]
# calls = [1,2,3,4,5,6]
# a = np.array(vehicles, np.int32).reshape(len(vehicles), 1)
# a = np.empty([len(vehicles), len(calls)])
# print(a)
# print(a[0,0] >= 1)
# print(a[0,0])

import ujson
a = {1:[1,2,3,4,5], 2:[1,2,3,4,5]}
ujson.dumps(a)
