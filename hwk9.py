# Name:       Tanya Chen, Emily Wang
# Peers:      Maggie Hollis (CSC TA)
# References: Greedy Algotithm Lecture Note 
#             https://docs.python.org/3/library/csv.html
import csv
with open('color-US-states.csv') as US_map:
    map_reader = csv.reader(US_map, delimiter=' ', quotechar='|')
    for row in map_reader:
        pass


#### First Greedy Strategy ####


#### Second Greedy Strategy ####