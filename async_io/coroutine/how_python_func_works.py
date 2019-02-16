# The C function that executes a Python function
# PyEval_EvalFrameEx
# takes a Python STACK FRAME OBJECT
# evaluates Python bytecode IN THE CONTEXT OF THE FRAME

# PyEval_EvalFrameEx encounters CALL_FUNCTION bytecode 
# it creates a new Python stack frame and recurses

# IT IS CRUCIAL : Python stack frames are ALLOCATED IN HEAP MEMEORY!
# a Python stack frame can OUTLIVE ITS FUNCTION CALL

import inspect
frame=None

def foo():
    bar()

def bar():
    global frame
    frame=inspect.currentframe()

foo()
# The frame was executing the code for 'bar'
print(frame.f_code.co_name)

# Its back pointer refers to the frame for 'foo'
caller_frame=frame.f_back
print(caller_frame.f_code.co_name)


