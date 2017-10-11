import operator
import sys

# orig_stdout = sys.stdout
# f = open('out2.txt', 'w')
# sys.stdout = f

def find_overlap(a, b):
    set_a, set_b = set(a), set(b)
    return frozenset(set_a.intersection(set_b))

def prepare_data(data):
    prepared_data = []
    for line in data:
        line = line.strip()
        integer_line = [int(char) for char in line.split(' ')]
        # print integer_line
        prepared_data.append(integer_line)
    return prepared_data

def count_overlaps(data):
    count_overlaps = {}
    for ind, j in enumerate(data):
        current_row = j
        reduced_data = data[ind+1:]
        local_dict = {}
        for row in reduced_data:
            overlap = find_overlap(current_row, row)
            print 'current', current_row
            print 'row', row
            print overlap
            if overlap and overlap not in count_overlaps.keys():
                print True
                if len(overlap) > 2:
                    if overlap not in count_overlaps:
                        local_dict[overlap] = 2
                    else:
                        local_dict[overlap] += 1
        print 'local', local_dict
        print 'global', count_overlaps
        count_overlaps.update(local_dict)
        print 'global', count_overlaps
        print '___________________'
    return count_overlaps

def print_overlaps(all_overlaps):
    frequency_distribution = []
    for key in all_overlaps:
        row = (key, all_overlaps[key])
        frequency_distribution.append(row)
    frequency_distribution.sort(key = lambda x: x[1], reverse=False)
    for row in frequency_distribution:
        print row

with open('retail.dat', 'rb') as f:
    data = f.readlines()

data = prepare_data(data)

test_data = [
    [1,2,3, 8],
    [1,2,3, 4],
    [1,2,3, 5],
    [1,2,3, 5],
    [1,2,6, 6, 3, 6],
    [1,2,6, 6, 3, 6],
    [1,2,3, 7],
    [1,2,3, 7],
    [1,1,2,3, 7]
]

all_overlaps = count_overlaps(test_data)
print_overlaps(all_overlaps)
#
# for overlap in all_overlaps:
#     for key in all_overlaps.keys():
#         if len(key) > len(overlap):
#             if len(overlap) == len(key.intersection(overlap)):
#                 all_overlaps[key] += 1
#
# sys.stdout = orig_stdout
# f.close()
