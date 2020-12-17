from math import log, ceil

def compress(filename):
    inputFile = open(filename, 'r')
    name = "comp_" + filename
    compressed = open(name, 'w')
    inputRead = inputFile.read()
    D = {}
    n = 1
    c = ''
    for i in repr(inputRead):
        if c + i not in D:
            if c == '':
                compressed.write('0/' + i + '\n')
                D[i] = n
            else:
                compressed.write(str(D[c]) + '/' + i + '\n')
                D[c + i] = n
            n += 1
            c = ''
        else:
            c = c + i
    inputFile.close()
    compressed.close()


def decompress(filename):
    compressedFile = open(filename, 'r')
    name = "decomp_" + filename
    decompressed = open(name, 'w')
    compressedRead = compressedFile.readlines()
    D = {}
    n = 1
    result = []
    for line in compressedRead:
        line = line[:-1]
        line = line.split('/')
        i=int(line[0])
        if i == 0:
            result.append(line[1])
            D[n] = line[1]
            n += 1
        else:
            result.append(D[i])
            result.append(line[1])
            D[n] = (D[i] + line[1])
            n += 1
    decompressed.write(str(''.join(result)))
    compressedFile.close()
    decompressed.close()



if __name__ == '__main__':
    filename = 'macbeth3.txt'
    compress(filename)
    name = "comp_" + filename
    decompress(name)
