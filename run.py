import time
import sys

def prepare_data(data):
    prepared_data = []
    for line in data:
        line = line.strip()
        integer_line = [int(char) for char in line.split(' ')]
        prepared_data.append(integer_line)
    return prepared_data

def find_overlap(a, b):
    set_a, set_b = set(a), set(b)
    return frozenset(set_a.intersection(set_b))

def count_overlaps(data, sigma):
    """Iterate over transactions. After each iteration, exclude the transaction
    from further comparison. Find intersections between each transaction
    pair. Create an outer loop dictionary with frozen sets as keys and
    incrementing frequencies as values. Set up a nested loop with an inner
    dictionary, so that on the inner loop the outer dictionary can be used to
    filter out duplicate comparisons and the inner one to keep track of
    incrementation. Update the outer dictionary with the inner one on each
    iteration of the outer loop. Return the outer dictionary."""
    outer_dict = {}
    for i, j in enumerate(data):
        outer_row = j
        inner_data = data[i+1:]
        inner_dict = {} # Allow incrementing sets within a nested loop
        for inner_row in inner_data:
            overlap = find_overlap(outer_row, inner_row)
            if overlap and overlap not in outer_dict: # Exclude sets found
            # in previous outer loops
                if len(overlap) > sigma:
                    if overlap not in inner_dict:
                        inner_dict[overlap] = 2
                    else:
                        inner_dict[overlap] += 1
        outer_dict.update(inner_dict)
    return outer_dict

def sort_by_frequency(all_overlaps):
    """Represent the dictionary of frozen sets and their frequencies as a
    nested list. Sort the list by frequency."""
    sorted_frequency = []
    for key in all_overlaps:
        row = (key, all_overlaps[key])
        sorted_frequency.append(row)
    sorted_frequency.sort(key = lambda x: x[1], reverse=True)
    return sorted_frequency

def output_results(sorted_frequency, file_name):
    for row in sorted_frequency:
        set_size = len(row[0])
        co_occur = row[1]
        ids = [str(item) for item in row[0]]
        ids = ', '.join(ids)
        with open(file_name, 'a') as f:
            line = "{}, {}, {}\n".format(set_size, co_occur, ids)
            f.write(line)
    return

if __name__ == '__main__':
    start_time = time.time()
    with open('retail.dat', 'rb') as f2:
        data = f2.readlines()
    data = prepare_data(data)
    all_overlaps = count_overlaps(data, 2)
    sorted_frequency = sort_by_frequency(all_overlaps)
    output_results(sorted_frequency, sys.argv[1])
    print("--- {} seconds ---".format(time.time() - start_time))
