from collections import Counter
import gzip

def answer(a):
    print("Reads in the file = {}".format(a[5]))
    print("Reads sequence average length =", round(a[6] / a[5]))
    print()
    print("Repeats = {}".format(a[3]))
    print("Reads with Ns = {}".format(a[7]))
    print('')
    print("GC content average = {}%".format(round(a[2] / a[5], 2)))
    print("Ns per read sequence = {}%".format(round(a[1] / a[5], 2)))


dict_best = {}

for b in range(3):
    file_name = input()
    list_ = []
    with gzip.open('{}'.format(file_name), 'rt') as fin:
        for line in fin:
            list_.append(line)
    file = open("{}".format(file_name), 'rt', encoding='latin1')
    list_b = []
    list_gc = []
    list_n = []
    for i in list(list_)[1::4]:
        list_gc.append(i.replace('\n', ''))
        list_b.append(len(i.replace('\n', '')))
    file.close()
    gc_content = 0
    n_name = 0
    for i in list_gc:
        array = str(i)
        c = Counter(array)
        for i in list(c):
            if i not in "GCAT":
                if i in "[]'  ,":
                    c.pop('{}'.format(i))
                elif i == "N":
                    list_n.append(i)
        i = ((c['G'] + c['C']) / len(array)) * 100
        n_name += c['N'] / len(array) * 100
        gc_content += i
    repeats = len(list_gc) - len(set(list_gc))
    dict_best["{}".format(b)] = [round((sum(list_b) / len(list_b))), n_name, gc_content, repeats, len(list_n), len(list_b), sum(list_b), len(list_n)]

first_list = dict_best['0']
second_list = dict_best['1']
third_list = dict_best['2']


best_repeats = (first_list[1], second_list[1], third_list[1])
best_n = (first_list[3], second_list[3], third_list[3])

if sum(best_repeats) == 0:
    index = best_n.index(min(best_n))
    answer(dict_best["{}".format(index)])
else:
    index = best_repeats.index(min(best_repeats))
    answer(dict_best["{}".format(index)])


