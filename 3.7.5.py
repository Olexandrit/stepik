def create_dict():

    dict = {i:[] for i in range(1,12)}

    return dict

def main_def():

    dict = create_dict()

    with open(r'/home/olexandrit/Downloads/dataset_3380_5.txt') as file:
        for line in file:

            words = line.split( )

            dict[int(words[0])].append(int(words[2]))

    ndict = {}
    for key in dict:
        if len(dict[key]) == 0:
            print(key,"","-")
        else:
            # ndict[key] = round(sum(dict[key]) / len(dict[key]),1)
            print(key,"",sum(dict[key]) / len(dict[key]))
    # print(ndict)

main_def()