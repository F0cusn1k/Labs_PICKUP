import json
import io
import codecs


from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique

'''
with open("data_light.json") as f:
    data = json.load(f)
'''

file = codecs.open( "data_light.json", "r", "utf-8" )
data = json.load(file)
file.close()

@print_result
def f1(arg):
    return sorted(list(Unique([item['job-name'] for item in arg], ignore_case = True)))
    


@print_result
def f2(arg):
    return list(filter(lambda text: (text.split())[0] == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda text: text + ' с опытом Python', arg))


@print_result
def f4(arg):
    tmp = list(zip(arg, [', зарплата ' + str(salary) + ' руб.' for salary in gen_random(len(arg), 100000, 200000)]))
    return [item[0] + item[1] for item in tmp]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
