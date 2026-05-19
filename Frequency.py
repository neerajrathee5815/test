

def frequency(x):

    words = x.lower().split()
    freq = {}
    for i in words:
        freq[i] = freq.get(i,0) + 1
    return freq

if __name__ == "__main__":
    a = str(input("Please enter a sentence : "))
    frq = frequency(a)
    print(frq)  

