import math

cont = 'y'

func = dict()

while cont.lower() != 'n':
    x = float(input("Enter next x-axis: "))
    #y = float(input("Enter next y-axis: "))
    y = math.log(x)

    func[x] = y

    ind = ""

    for i in func:
        ind += "(x-" + str(i) + ")"

    sub = ""

    #Horribly inefficient but whatever, just experimenting rn
    for i in func:
        t = str(func[i])
        for j in func:
            if i != j:
                t += "\\frac{(x-" + str(j) + ")}{(" + str(i) + "-" + str(j) + ")}"
        
        sub += t + "+"

    print(ind + "+" + sub)
    
    cont = input("Continue? (y/n): ")
