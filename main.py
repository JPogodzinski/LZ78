def compress(data):
    D = {}
    result = []
    n = 1
    c = ''
    for i in data:
        if c + i not in D:
            if c == '':
                result.append((0, i))
                D[i] = n
            else:
                result.append((D[c], i))
                D[c + i] = n
            n += 1
            c = ''
        else:
            c = c + i
    return result

def decompress(data):
    D={}
    n=1
    result=[]
    for i,s in data:
        if i==0:
            result.append(s)
            D[n]=s
            n+=1
        else:
            result.append(D[i])
            result.append(s)
            D[n] = (D[i]+s)
            n += 1
    return ''.join(result)

def openFile(name):
    D=''
    f=open(name,"r")
    for x in f:
        D+=x
    f.close()
    return D

def writeFile(name, compressed):
    name="comp_"+name
    print(name)
    f = open(name, "w")
    f.write(str(compressed))
    f.close()

if __name__ == '__main__':
    filename="small.txt"
    data=openFile(filename)
    print(data)
    compressed=compress(data)
    print(compressed)
    writeFile(filename,compressed)
    decompressed=decompress(compressed)
    print(decompressed)


