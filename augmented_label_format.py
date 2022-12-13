import os

# file = 'data/augmented/labels/' + '1_aug.txt'
# with open(file, 'r') as f:
#     lines = f.read().rstrip()
# lines = lines.split('\n')
# for line in lines:
#     line = line[1:-1]
#     line = line.split(',')
#     line = [w.strip() for w in line]
#     text = line[0] + ' ' + line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + '\n'
#     print(line)
#     print(text)

files = os.listdir('data/augmented/labels')
for file in files:
    file = 'data/augmented/labels/' + file
    print(file)

    try:
        with open(file, 'r') as f:
            lines = f.read().rstrip()
        lines = lines.split('\n')
        print(lines)

        for line in lines:
            line = line[1:-1]
            line = line.split(',')
            line = [w.strip() for w in line]
            text = line[0] + ' ' + line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + '\n'
            # if os.path.exists(file):
            #     with open(file, 'a') as f:
            #         f.write(text)
            # else:
            with open(file, 'w') as f:
                f.write(text)
    except:
        pass

    # rename augmented files
    # source = 'data/augmented/labels/' + file
    # dest =  'data/augmented/labels/' + file[:-4]+ '_aug.txt'
    # os.rename(source, dest)

    