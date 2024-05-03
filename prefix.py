def FindString(a):
    string=[]
    pre="ca"
    for i in a:
        if pre in i:
          if i[0:2]==pre:
            string.append(i)
    print(string)
a=["cat","car","fear","center"]
FindString(a)