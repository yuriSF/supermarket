with open('retail.dat', 'rb') as f:
    data = f.readlines()

def find_intersection(a, b):
    intersection = list(set(a) & set(b))
    intersection.sort()
    return intersection

def prepare_data(data):
    prepared_data = []
    for line in data:
        line = line.strip()
        integer_line = [int(char) for char in line.split(' ')]
        print integer_line
        prepared_data.append(integer_line)
    return prepared_data

data = prepare_data(data[0:1000])
print data

intersections_count = []
for ind, row in enumerate(data):
    current_row = data[ind]
    reduced_data = data[ind+1:-1]
    print len(reduced_data)
    for row in reduced_data:
        intersection = find_intersection(current_row, row)
        if len(intersection) > 2:
            intersections = [row[0] for row in intersections_count]
            if intersection not in intersections:
                entry = [intersection, 1]
                intersections_count.append(entry)
            else:
                for row in intersections_count:
                    if intersection == row[0]:
                        row[1] = row[1] + 1
                        print 'I am here'


intersections_count.sort(key = lambda x: x[1], reverse = True)
print intersections_count
for item in intersections_count:
    print item[0], item[1]
