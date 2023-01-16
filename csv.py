import csv


def resort(source_id, j=0):
    if j >= len(source_id) - 1:
        return source_id
    for i in range(j + 1, len(source_id)):
        if set(source_id[i]) & set(source_id[j]):
            source_id[j] = sorted(list(set(source_id.pop(i)) | set(source_id[j])))
            return resort(source_id, j)
    return resort(source_id, j + 1)


with open("in.csv", "r", newline="") as source_file:
    csv_reader = csv.reader(source_file, delimiter=";")
    source_data = list(csv_reader)

print('source_data:', source_data)
out_data = resort(source_data)
print('out_data:', out_data)

with open("out.csv", "w", newline="") as out_file:
    csv_writer = csv.writer(out_file, delimiter=";")
    csv_writer.writerows(out_data)
