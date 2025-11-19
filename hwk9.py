# Name:       Tanya Chen, Emily Wang
# Peers:      N/A
# References: Greedy Algotithm Lecture Note 
#             https://docs.python.org/3/library/csv.html
#             https://www.geeksforgeeks.org/python/load-csv-data-into-list-and-dictionary-using-python/
#             https://www.geeksforgeeks.org/python/sets-in-python/
#             https://www.geeksforgeeks.org/python/python-set-methods/ (Eventually not used)
#             https://www.geeksforgeeks.org/python/how-to-save-a-python-dictionary-to-a-csv-file/
#             https://stackoverflow.com/questions/39176935/formatting-output-of-csv-file-in-python
import csv


### First CSV file: US state ###

states: dict[str, str] = {}

with open("color-US-states.csv", 'r') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        key = row["STATE"]
        value = row["NEIGHBORS"]
        states[key] = value


states_1: dict[str, list[str]] = {}
result_1: dict[str, int] = {} # Used to save states and their color

# Convert the value into a list of string
for key in states.keys():
    v_1 = states[key].split(", ") 
    states_1[key] = v_1
    

#### First Greedy Strategy ####
# Helper functions
def arr_append(arr: list[str], value: str) -> list[str]:
    """Add given value to the end of the array
    : param arr: (list[str]) The original array
    : param value: (str) The value we want to add the the tail of arr
    :return : (list[str]) A new array containing all the elements in arr and have value in its tail

    >>> arr = ["a", "b"]
    >>> print(arr_append(arr, "c"))
    ["a", "b", "c"]
    """
    new_arr = [""]*(len(arr)+1)

    i = 0

    while i < len(arr):
        new_arr[i] = arr[i]

        i += 1

    new_arr[i] = value

    return new_arr

def arr_slice(arr: list[str], start: int, end: int) -> list[str]:
    """ Return a slice the given array from start to end (not inclusive)
    : param arr: (list[str]) The original array
    : param start: (int) The start index
    : param end: (int) The end index (not included)
    :return : (list[str]) A new array containing elements from arr[start] to arr[end-1]

    >>> arr = ["a", "b", "c", "d", "e", "f", "g"]
    >>> print(arr_slice(arr, 2,5))
    ["c", "d", "e"]
    """
    new_arr = [""]*(end-start)

    i = start
    j = 0

    while j < len(new_arr):
        new_arr[j] = arr[i]
        i += 1
        j += 1

    return new_arr

def merge(states_1: dict[str, list[str]], left: list[str], right: list[str]) -> list[str]:
    """ It is not a generalized merge method
    Merge 2 sorted lists of states in decreasing order based on the number of their neighbors
    : param states_1: (dict[str, list[str]]) A dictionary used for referencing how many neighbors a state has
    : param left: (list[str]) A sorted list of states (in descending order)
    : param right: (list[str]) A sorted list of states (in descending order)
    :return : (list[int]) A list of integers that contains all elements in left and right and is sorted in ascending order

    >>> l1 = ["Utah","Nebraska","Massachusetts"]
    >>> l2 = ["Arizona", "Mississippi", "Maine"]
    >>> print(merge(states_1,l1,l2))
    ['Utah', 'Nebraska', 'Arizona', 'Massachusetts', 'Mississippi', 'Maine']
    """
    merged:list[str] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # If number of values in the left is greater than the number of values in the right
        if len(states_1[left[i]]) > len(states_1[right[j]]):
            merged = arr_append(merged, left[i])
            i+=1
        else:
            merged = arr_append(merged, right[j])
            j+=1

    while i < len(left):
        merged = arr_append(merged, left[i])
        i+=1

    while j < len(right):
        merged = arr_append(merged, right[j])
        j+=1

    return merged

def mergeSort(state_1: dict[str, list[str]], state_list:list[str]) -> list[str]:
    """Sort given list in an increasing order
    : param states_1: (dict[str, list[str]]) A dictionary used for referencing how many neighbors a state has
    : param state_list: (list[str]) An unsorted array of states
    :return : (list[str]) A sorted array of states in descending order based on how many neighbors they have

    >>> l3 = ["California", "Ohio", "Illinois", "Missouri", "Alaska", "Wyoming"]
    >>> print(mergeSort(l3))
    [ "Missouri", "Wyoming", "Illinois", "Ohio", "California", "Alaska"]
    """
    # Base Case: length of array is 1
    if len(state_list) == 1:
        return state_list
    
    mid = len(state_list)//2

    slice_left = arr_slice(state_list, 0, mid)
    slice_right = arr_slice(state_list, mid, len(state_list))

    left = mergeSort(state_1, slice_left)
    right = mergeSort(state_1, slice_right)

    return merge(state_1, left, right)

def strategy_1(states_1: dict[str, list[str]]) -> None:
    """ Use a greedy algorithm to color the map. 
        The local optimal solution in this strategy is to color the state which has the most neighbors first
    :param states_1: (dict[str, list[str]])
    """
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
    colored:list[str] = [""]

    # Use for loop to loop through every state
    for state in state_list:
        # Use a set to store colors for neighbors
        neighbor_colors: set[int] = set()

        # Check whether current state is colored or not -> We only color states that do not have any color
        # If the current state is not colored, check whether its neighbors are colored
        if state not in colored:
            # Check whether the current state has neighbor or not before adding neighbor colors
            if states_1[state] == [""]:
                result_1[state] = 1
            else:
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

                # Add state, color pair to result
                result_1[state] = color

            # Record that current state is colored
            colored = arr_append(colored, state)

    print("Map is colored. The result is stored as a csv file called map_coloring_strategy_1.csv")

    # Store the result as a csv file
    filename = "map_coloring_strategy_1.csv"
    
    category = ["states", "color"]

    # Writing dictionary to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(category)
        for k, v in result_1.items():
            row = [k,v]
            writer.writerow(row)

    file = open("map_coloring_strategy_1.csv")
    read_file = csv.reader(file)
    for row in read_file:
        print('{:<15}  {:<15}'.format(*row))


#### Second Greedy Strategy ####
def color_fewest_neighbor(states: dict[str, list[str]]):
    """This function colors the map with different color for adjacent areas by coloring the area with fewest neighbor first. 
        BUT specifically the US states, because it has limited colors.
        
    :param map (dict[str, list[str]]): A dictionary that contais all the areas
    >>> map = {'Hawaii': ''}
    >>> color_fewest_neighbor(map)
    State: Hawaii, color: red
    """
    states_sets = set(states.keys())
    colored_states = {state: "" for state in states.keys()}
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
    # it is actually terrible just having 7 colors of the rainbow defined
    # because this code cannot generalize to other complicated maps 
    # but I am only coloring the 50 states, so I want to use it :)

    while states_sets:

        fewest_key: str|None = None
        smallest_len = float('inf')

        for key in states_sets:
            num_neighbors = len(states[key])
            if num_neighbors < smallest_len:
                smallest_len = num_neighbors
                fewest_key = key
    
        if fewest_key is not None:
            if states[fewest_key] == ['']: 
                colored_states[fewest_key] = colors[0]
            else:
                for color in colors:
                    conflict = False
                    for neighbor in states[fewest_key]:
                        if colored_states.get(neighbor) == color:
                            conflict = True
                            break
                    if not conflict:
                        colored_states[fewest_key] = color
                        break

            states_sets.remove(fewest_key)

    print("Map is colored. The result is stored as a csv file called map_coloring_strategy_2.csv")

    # Store the result as a csv file
    filename = "map_coloring_strategy_2.csv"
    
    category = ["states", "color"]

    # Writing dictionary to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(category)
        for k, v in colored_states.items():
            row = [k,v]
            writer.writerow(row)

    file = open("map_coloring_strategy_2.csv")
    read_file = csv.reader(file)
    for row in read_file:
        print('{:<15}  {:<15}'.format(*row))

def main():
    #### -------Tests for Strategy 1 -> Ensure all helper functions work -----####
    # print("---Test: arr_append---")
    # arr = ["a", "b"]
    # print(arr_append(arr, "c")) # Desired output ["a", "b", "c"]

    # print("---Test: arr_slice---")
    # arr = ["a", "b", "c", "d", "e", "f", "g"]
    # print(arr_slice(arr, 2,5)) # Desired output ["c", "d", "e"]

    # print("---Test: merge---")
    # l1 = ["Utah","Nebraska","Massachusetts"]
    # l2 = ["Arizona", "Mississippi", "Maine"]
    # print(merge(states_1,l1,l2)) 
    # Desired output: ['Utah', 'Nebraska', 'Arizona', 'Massachusetts', 'Mississippi', 'Maine']
    #                   6       6           5           5               4               1

    # l3 = ["California", "Ohio", "Illinois", "Missouri", "Alaska", "Wyoming"]
    # print(mergeSort(states_1, l3))
    # Desired output: [ "Missouri", "Wyoming", "Illinois", "Ohio", "California", "Alaska"]
    #                   8           6           6           5       3               0
    #### ------End of Tests for Strategy 1 ------------------------------------####
    #print(states)

    print("Hello! Do you want to see a colored US map?")
    choice = input("Which methods would you like to choose? type in 1/2\n")
    if choice == "1":
        strategy_1(states_1)
    elif choice == "2":
        color_fewest_neighbor(states_1)
    else:
        print("Thank you!")

if __name__ == "__main__":
    main()
