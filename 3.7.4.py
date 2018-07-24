def inputcoordintes():

    oper = {'север': 1, 'юг': -1, 'восток': 1, 'запад': -1}
    XY = {'север':'Y', 'юг':'Y', 'восток':'X', 'запад':'X'}

    list_X = []
    list_Y = []
    para_list_input = []

    count_coord = int(input("Enter count coordinates? "))
    i=1
    while i <= count_coord:
        para = str(input("Enter " + str(i) + " coordinates?")).strip()
        para_list_input.append(para)
        i += 1

    # para_list_input = ['север 10','запад 20','юг 30','восток 40']
    for para in para_list_input:

        para_list = para.split(" ")

        if XY[para_list[0]] == 'X':
            list_X.append(oper[para_list[0]] * int(para_list[1]))

        if XY[para_list[0]] == 'Y':
            list_Y.append(oper[para_list[0]] * int(para_list[1]))

    X = sum(list_X)
    Y = sum(list_Y)

    return str(X) + " " + str(Y)

#print(inputcoordintes())

print("Hello ")