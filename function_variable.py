

sam=150

def print_var():
    # global puja
    global sam
    sam=sam+50
    global puja
    puja='python'
    print('puja value inside the function,',sam)


# print('sam value out of the function :',puja)
print('sam value',sam)
print_var()
print('puja value',puja)