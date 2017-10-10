import operator
import sys
import time

def find_overlap(a, b):
    set_a, set_b = set(a), set(b)
    return frozenset(set_a.intersection(set_b))

def prepare_data(data):
    prepared_data = []
    for line in data:
        line = line.strip()
        integer_line = [int(char) for char in line.split(' ')]
        prepared_data.append(integer_line)
    return prepared_data

def count_overlaps(data):
    count_overlaps = {}
    checked = []
    for i, j in enumerate(data):
        outer_row = j
        reduced_data = data[i+1:]
        for inner_row in reduced_data:
            overlap = find_overlap(outer_row, inner_row)
            if overlap and overlap not in checked:
                if len(overlap) > 2:
                    if overlap not in count_overlaps:
                        count_overlaps[overlap] = 2
                    else:
                        count_overlaps[overlap] += 1
        checked.append(overlap)
    return count_overlaps

def sort_by_frequency(all_overlaps):
    sorted_frequency = []
    for key in all_overlaps:
        row = (key, all_overlaps[key])
        sorted_frequency.append(row)
    sorted_frequency.sort(key = lambda x: x[1], reverse=True)
    return sorted_frequency

def output_results(sorted_frequency):
    for row in sorted_frequency:
        set_size = len(row[0])
        co_occur = row[1]
        ids = [str(item) for item in row[0]]
        ids = ', '.join(ids)
        print row
        with open('output.txt', 'a') as f:
            line = "{}, {}, {}\n".format(set_size, co_occur, ids)
            f.write(line)
    return

if __name__ == '__main__':
    start_time = time.time()
    with open('retail.dat', 'rb') as f2:
        data = f2.readlines()
    data = prepare_data(data)
    all_overlaps = count_overlaps(data)
    sorted_frequency = sort_by_frequency(all_overlaps)
    output_results(sorted_frequency)
    print("--- %s seconds ---" % (time.time() - start_time))
