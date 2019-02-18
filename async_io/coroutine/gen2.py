def gen_fn():
    result=yield 1
    print('result of yield : {}'.format(result))
    result2=yield 2
    print('result of 2nd yield : {}'.format(result2))
    return 'done'

def caller_fn():
    gen=gen_fn()
    rv=yield from gen
    print('return value of yield-from : {}'.format(rv))

caller=caller_fn()
#start the generator
print(caller.send(None))
#instruction pointer : 10
print(caller.gi_frame.f_lasti)

#resume the generator
#and tossthe data of 'yang' to gen_fn
print(caller.send('Go'))
#instruction pointer remains at 10
print(caller.gi_frame.f_lasti)

#resume the generator
try:
    print(caller.send('Y'))
except StopIteration:
    pass
