
import matplotlib.pyplot as plt
start  = 1
n = 5
end = 10


def hard_problem(i, n, end):
    n_output = list()
    while i < end:
        n_output.append(n**i)
        i = i+1
    return n_output


def easy_problem(i, end):
    n_output = list()
    while i < end:
        n_output.append(2**i)
        i = i+1
    return n_output

hard = (hard_problem(start,n, end))
easy = (easy_problem(start, end))

plt.plot(hard,'b', easy, 'ro')
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()

