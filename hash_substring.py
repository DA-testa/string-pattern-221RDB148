# python3

def next_prime(n):
    def is_prime(n):
        if n<= 1:
            return False
        elif n <= 3:
            return True
        elif n%2 == 0 or n%3==0:
            return False
        i=5
        while i*i <= n:
            if n% i == 0 or n% (i+2) == 0:
                return False
            i+=6
        return True
    i= n + 1
    while not is_prime(i):
        i+=1
    return i

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())
    pattern = ""
    text = ""
    
    inp = input()
    if inp.upper == "I":
        pattern = input()
        text = input()
    if inp.upper == "F":
        file = open(inp.split(" ",1))
        str = file.readlines()
        pattern = str(str[0])
        text = str(str[1])
    # textos = "ZtonpqnFzlpvUKZrBbRlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXxtHmTxoLuMbRYsvSpxhtrlvABBlFYmndFzHypOmJyFxjHEPlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXbDiEAvtPlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXRRNoBCUMQVOlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXRLKlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXAYPDKWtVpShhclNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXOJlUlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXglmlNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUXuaOibGlVrwghvNTgLfltIbEdBlgjelFjQkBeFrdEV"
    # patternos = "lNoYhXmlwOscxnkTWjsyNJNhgvzMFbxFnbiWuBAGjZQlCRQHjTUX"
    return (pattern,text)

Q = 0
# def get_hash(str:str):
#     m = len(str)
#     result = 0
#     for i in range(m):
#         result = (B + result + )
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    results = []
    B = 256
    Q = next_prime(len(pattern))
    
    tl = len(text)
    pl = len(pattern)

    h = 1
    for i in range(1,pl):
        h = (h * B) % Q

    #initial hash values:
    p_hash = 0
    t_hash = 0
    for i in range(0,pl):
        p_hash = (B * p_hash + ord(pattern[i])) % Q
        t_hash = (B * t_hash + ord(text[i])) % Q

    #remaining charecters
    for i in range(0,tl-(pl-1)):
        # print(text[i:i+pl],end=" ")
        # print(t_hash, p_hash)
        if p_hash == t_hash:
            if pattern == text[i:i+pl]:
                # print("URAAAAAA=",i)
                results.append(i)
        #do i need this?
        if i < tl-pl:
            t_hash = (B * (t_hash-ord(text[i])*h) + ord(text[i+pl]))%Q

            if t_hash < 0:
                print("t is negative")
                t = t + Q 
    # print("pattern not found")
    return results
                


    # return [0, "asd", 2.8]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

