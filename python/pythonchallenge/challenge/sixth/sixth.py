import pickle
a = pickle.load(open("word.txt", "r"))
for item in a:
    # print item
    x_buffer = ""
    for x, y in item:
            # if x == ' ':
            #     x_buffer += ' '*y
        x_buffer += x*y
    print x_buffer

