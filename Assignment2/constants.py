from collections import namedtuple

Score = namedtuple("Score", ['vector', 'score'])
Weight = namedtuple("Weight", ['op_name', 'weight'])
Operator_Score = ("Operator_Score", ['op_name', 'score', 'times_used'])

N_ITERATIONS = 100
x = "datama/"
paths = [x+a for a in
         [
             "Call_7_Vehicle_3.txt",
         "Call_18_Vehicle_5.txt",
         "Call_035_Vehicle_07.txt",
         "Call_080_Vehicle_20.txt",
         "Call_130_Vehicle_40.txt"]]

