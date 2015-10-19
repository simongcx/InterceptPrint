import InterceptPrintM

for i in range(0,100):
    print i, 'hello'

InterceptPrintM.timestamp=True

for i in range(0,100):
    print i, 'bob'

InterceptPrintM.linenumber=True

for i in range(0,100):
    print i, 'joe'