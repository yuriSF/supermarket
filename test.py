import time
from run import prepare_data, find_overlap, count_overlaps, sort_by_frequency

test_data = [
    [1, 2, 3, 8],
    [1, 2, 3, 4],
    [1, 2, 3, 5],
    [1, 2, 3, 5],
    [1, 2, 6, 6, 3, 6],
    [1, 2, 6, 6, 3, 6],
    [1, 2, 3, 7],
    [1, 2, 3, 7],
    [1, 1, 2, 3, 7],
    [110, 111, 120],
    [110, 111, 120],
    [110, 120, 111],
    [200, 201, 202]
]

expected_output = [
    [3, 9, [1, 2, 3]],
    [3, 3, [120, 110, 111]],
    [4, 3, [1, 2, 3, 7]],
    [4, 2, [1, 2, 3, 6]],
    [4, 2, [1, 2, 3, 5]]
    ]

def output_results(sorted_frequency):
    output = []
    for row in sorted_frequency:
        set_size = len(row[0])
        co_occur = row[1]
        ids = [item for item in row[0]]
        line = [set_size, co_occur, ids]
        output.append(line)
    return output

if __name__ == '__main__':
    start_time = time.time()
    with open('retail.dat', 'rb') as f2:
        data = f2.readlines()
    data = prepare_data(data)
    all_overlaps = count_overlaps(test_data, 2)
    sorted_frequency = sort_by_frequency(all_overlaps)
    output = output_results(sorted_frequency)
    print("--- {} seconds ---".format(time.time() - start_time))
    if output == expected_output:
        print('Test passed')
    else:
        print('Test failed')
