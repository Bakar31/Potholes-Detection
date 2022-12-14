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
    file_path = 'data/augmented/labels/' + file
    # print(file)

    try:
        with open(file_path, 'r') as f:
            lines = f.read().rstrip()
        lines = lines.split('\n')
        # print(lines)

        for line in lines:
            line = line[1:-1]
            line = line.split(',')
            line = [w.strip() for w in line]
            text = line[0] + ' ' + line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + '\n'
            print(text)
            
            dest_file = 'data/augmented/aug_labels/' + file
            print(dest_file)
            if os.path.exists(dest_file):
                with open(dest_file, 'a') as f:
                    f.write(text)
            else:
                with open(dest_file, 'w') as f:
                    f.write(text)
    except:
        print('Executing pass')
        pass

    # rename augmented files
    # source = 'data/augmented/labels/' + file
    # dest =  'data/augmented/labels/' + file[:-4]+ '_aug.txt'
    # os.rename(source, dest)

    