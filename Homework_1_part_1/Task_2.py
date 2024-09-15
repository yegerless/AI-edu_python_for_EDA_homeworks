students_data = {}
while True:
    data = input()
    if data == 'END':
        break
    name, subj, mark   = data.split()
    if students_data.get(name, 0):
        students_data[name][subj] = mark
    else:
        students_data[name] = {subj: mark}

student = input()
[print(subj, mark) for subj, mark in sorted(students_data[student].items(), key= lambda x: x[0])]