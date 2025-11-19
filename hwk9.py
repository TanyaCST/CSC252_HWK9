# Name:       Tanya Chen, Emily Wang
# Peers:      Maggie Hollis (CSC TA)
# References: Greedy Algotithm Lecture Note 
#             https://docs.python.org/3/library/csv.html
#             https://www.geeksforgeeks.org/python/load-csv-data-into-list-and-dictionary-using-python/
#             https://www.geeksforgeeks.org/python/sets-in-python/
#             https://www.geeksforgeeks.org/python/python-set-methods/
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
# Helper functions
def arr_append():
    pass

def arr_slice():
    pass

def merge(states_1: dict[str, list[str]], left: list[str], right: list[str]) -> list[str]:
    """ Merge 2 sorted lists in increasing order
    : param left: (list[int]) A sorted list of integers (in ascending order)
    : param right: (list[int]) A sorted list of integers (in ascending order)
    :return : (list[int]) A list of integers that contains all elements in left and right and is sorted in ascending order

    >>> l1 = [1,5,6]
    >>> l2 = [2,3,4]
    >>> print(merge(l1,l2))
    [1,2,3,4,5,6]
    """
    merged:list[str] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # If number of values in the left is greater than the number of values in the right
        if len(states_1[left[i]]) > len(states_1[right[j]]):
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    while i < len(left):
        merged.append(left[i])
        i+=1

    while j < len(right):
        merged.append(right[j])
        j+=1

    return merged

def mergeSort(state_1: dict[str, list[str]], btList:list[str]) -> list[str]:
    """Sort given list in an increasing order
    : param btList: (list[int]) 
    :return : (list[int])

    >>> l1 = [5,1,6,4,2,3]
    >>> print(mergeSort(l1))
    [1,2,3,4,5,6]
    """
    # Base Case: length of array is 1
    if len(btList) == 1:
        return btList
    
    mid = len(btList)//2

    left = mergeSort(state_1, btList[0:mid])
    right = mergeSort(state_1, btList[mid:])

    return merge(state_1, left, right)

def strategy_1(states: dict[str, str]):
    states_1: dict[str, list[str]] = {}
    result_1: dict[str, int] = {} # Used to save states and their color

    # Convert the value into a list of string
    for key in states.keys():
        v_1 = states[key].split(", ") # Can we use split there for string? I assume not?
        states_1[key] = v_1

    # Check the state with most neighbors first (highest length in value)
    # Sort the dictionary based on the number of neighbors (Use quick sort or merge sort)

    # Add all keys into a list
    len_key: int = len(states_1)
    state_list: list[str] = [""]*len_key
    i = 0

    for key in states_1.keys():
        state_list[i] = key
        i += 1

    # Sort the state list
    state_list: list[str] = mergeSort(states_1, state_list)

    # Start Coloring based on the state with highest
    # Define a set for colored states
    colored:list[str] = []

    # Use for loop to loop through every state
    for state in states_1.keys():
        # Use a set to store colors for neighbors
        neighbor_colors: set[int] = set()

        # Check whether current state is colored or not -> We only color states that do not have any color
        # If the current state is not colored, check whether its neighbors are colored
        if state not in colored:
            # Find the color of neighbors
            for neighbor in states_1[state]:
                # pass through the neighbors not being colored
                if neighbor in colored:
                    neighbor_colors.add(result_1[neighbor])

            # Assign current state first available color 
            # if the neighbors did not used up add colors in the set
            color: int = 1

            # Find first available color
            while color in neighbor_colors:
                color += 1

            # Assignment
            result_1[state] = color

    # Print the result in a clear way.


#### Second Greedy Strategy ####
