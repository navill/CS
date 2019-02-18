#the concept of a coroutine 
# a subroutine that can be paused and resumed

#coroutines multitask cooperatively,
#they choose WHEN TO PAUSE, and WHICH COROUTINE TO RUN NEXT

def gen_fn():
    result=yield 1
    print('result of yield : {}'.format(result))
    result2=yield 2
    print('result of 2nd yield : {}'.format(result2))
    #return in StopIteration
    return 'done'

#yield statement sets a flag 
generator_bit = 1<<5
print(bool(gen_fn.__code__.co_flags & generator_bit))

# NOT RUN the function
# creates a generator
gen=gen_fn()
print(type(gen))

# Python generators encapsulates a stack fame plus a reference to some code
# HEAP
# PyGenObject
# gi_frame--------------> PyFrameObject
#                         - f_lasti : instruction pointer
#                         - f_locals
# gi_code---------------> PyCodeObject
#                         - gen_fn's bytecode


