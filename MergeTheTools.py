def replace(Str):
    temp=[];
    for i in Str:
        if i in temp:
            continue;
        else:
            temp.append(i);
    return temp;

def merge_the_tools(Str,k):
    Len=len(Str);
    #print("Len=",Len);
    t=int(Len/k);
    #print("t=",t);
    string=[];
    for i in Str:
        string.append(i);
    #print(string);
    for i in range(t):
        # print("i=",i);
        val = ''.join(replace(string[i*k:i*k+k]));
        print(val);




if __name__ == '__main__':
