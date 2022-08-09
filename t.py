input = "PAYPALISHIRING"
size_input = len(input)
n = 3 #how many elements in the leftmost side
gen_index = []
#print(size_input)

def check_more_append(max, index):
    run = True
    base = 2 # formultiplication with 2,4,6,8 ..
    while run:
        print("********************************************")
        print("index  = ", index)
        check  = (n-1)*base
        print("check = ",check)
        check_max = check + index # what maximum index it can append
        print("check_max = ",check_max)
        print("check - index is =",check - index)
        if check_max < max:
            if index == 0 or check == check - index:
                print("Going IF ")
                print("Appending = ", check)
                gen_index.append(check)
            else:
                print("Going ELSE")
                if (check - index) not in gen_index:
                    print("appending check - index = ", check - index)
                    gen_index.append(check - index)
                
                print("appending check + index = ", check + index)
                gen_index.append(check + index)
            
            base = base + 2
        else:
            if (check - index) < max:
                if (check - index) not in gen_index:
                    print("appending check - index = ", check - index)
                    gen_index.append(check - index) 
            run = False

for i in range (0,n):
    gen_index.append(i)
    print("******************")
    print("appending = ", i)
    print("******************")
    check_more_append(size_input, i)
    

print(gen_index)

for i in range(0,size_input):
    print(input[int(gen_index[i])], end =" ")
        