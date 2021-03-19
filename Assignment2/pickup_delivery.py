# import re
#
# class PickupDataParser:
#
#     def __init__(self, filename):
#
#         with open(filename, 'r') as f:
#
#             lines = f.read()
#             categs = re.split("%.*\n", lines)
#
#             nr_nodes = self.get_nr(categs[1])
#             nr_vehicles = self.get_nr(categs[2])
#             nr_calls = self.get_nr(categs[4])
#
#             vehicle_data = self.fetch_data(categs[3])
#             vehicle_trans_data = self.fetch_data(categs[5])
#             call_data = self.fetch_data(categs[6])
#             travel_data = self.fetch_data(categs[7])
#             node_time_data = self.fetch_data(categs[8])[:-1]
#
#             print(vehicle_data)
#             print(node_time_data)
#
#             data_dict = {}
#
#             # Vehicle data
#             for data in vehicle_data:
#                 data_dict[data[0]] = {}
#                 data_dict[data[0]]['vehicle_data'] = {
#                      'home_node':data[1],
#                      'starting_time':data[2],
#                      'capacity':data[3]}
#
#             # Vehicle transportation data
#             for data in vehicle_data:
#                 data_dict[data[0]]['available_transports'] = data[1:]
#
#
#
#             print(data_dict)
#
#     def get_nr(self, inp:str):
#         return int(inp.strip("\n"))
#
#     def fetch_data(self, inp:str):
#         templist = [x.split(",") for x in [a for a in inp.split("\n") if a != ""]]
#         return templist
#
#
# if __name__ == "__main__":
#     p = PickupDataParser("Call_7_Vehicle_3.txt")