input = "PAYPALISHIRING"
size_input = len(input)
n = 4 #how many elements in the leftmost side
gen_index = []

def check_more_append(max, index):
    run = True
    base = 2 # formultiplication with 2,4,6,8 ..
    while run:
        check  = (n-1)*base
        check_max = check + index # what maximum index it can append
        if check_max < max:
            if index == 0 or check == check - index:
                gen_index.append(check)
            else:
                if (check - index) not in gen_index:
                    gen_index.append(check - index)
                gen_index.append(check + index)
            
            base = base + 2
        else:
            if (check - index) < max:
                if (check - index) not in gen_index:
                    gen_index.append(check - index) 
            run = False

for i in range (0,n):
    gen_index.append(i)
    check_more_append(size_input, i)

for i in range(0,size_input):
    print(input[int(gen_index[i])], end =" ")
        