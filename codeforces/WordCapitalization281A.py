w=input()
if w[0].islower():
    print(w[0].upper()+w[1::])
else:
    print(w)