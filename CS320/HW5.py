import random  # optional and you can delete this line if not useful


# subroutines if any, go here


# fill in repeat
def placement(numobjects, map):
    if map is None or numobjects <= 0:
        return None

    # Find the dimensions of the map
    L = len(map)
    S = len(map[0])

    # Count the number of available spaces
    available_spaces = sum(row.count(True) for row in map)

    # Check if there are enough available spaces
    if available_spaces < numobjects:
        return None

    # Create a list of coordinates for all available spaces
    coordinates = [(i, j) for i in range(L) for j in range(S) if map[i][j]]

    # Shuffle the list of coordinates
    random.shuffle(coordinates)

    # Select the first num_objects coordinates
    selected_coordinates = coordinates[:numobjects]

    return selected_coordinates
