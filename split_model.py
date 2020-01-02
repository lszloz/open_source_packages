
with open("inception_v3.caffemodel", 'rb') as f:
    byte_list = []
    while True:
        single_r = f.read(25165824)
        if single_r:
            byte_list.append(single_r)
        else:
            break

for i in range(len(byte_list)):
    with open(str(i), 'wb+') as f:
        f.write(byte_list[i])
