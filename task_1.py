def fib_num(i, calculated = {1:0, 2:1}):
    if i not in calculated:
        calculated[i] = fib_num(i-1, calculated) + fib_num(i-2, calculated)
    return calculated[i]

#fib_num(10)

#get_ipython().run_line_magic('timeit', 'fib_num(10)')

