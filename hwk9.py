# Name:       Tanya Chen, Emily Wang
# Peers:      Maggie Hollis (CSC TA)
# References: Greedy Algotithm Lecture Note 
#             https://docs.python.org/3/library/csv.html
#             https://www.geeksforgeeks.org/python/load-csv-data-into-list-and-dictionary-using-python/
import csv

# with open('color-US-states.csv') as US_map:
#     map_reader = csv.reader(US_map, delimiter=' ', quotechar='|')
#     for row in map_reader:
#         pass

states: dict[str, str] = {}

with open("color-US-states.csv", 'r') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        key = row["STATE"]
        value = row["NEIGHBORS"]
        states[key] = value
    
print(states)


#### First Greedy Strategy ####


#### Second Greedy Strategy ####
# Emily: start w/ fewer neighbors
states_sets = set(states)
colored_states = {state: "" for state in states.keys()}
colors = ["red", "orange", "yellow", "green", "blue", "inidigo", "violet"] #change it to simple array


# some thoughts

# find the states with fewest neighbor

# process it
# check if neighbor is colored in colored_states:
#   yes: color w/ different color; 
#   how to find this different color? current thought: we have to go in order: double for loop?
#   no/else: color it with the first color in list colors, update colored_states

# remove from states_sets