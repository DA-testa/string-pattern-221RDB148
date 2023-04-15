T = "mmmasdmmm"
P = "asdm"


B = 12
Q = 256
def get_hash(pattern:str) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result

for i in range(0,len(T)-(len(P)-1)):
    str = T[i:i+len(P)]
    print(str, P, end=" ")
    print(get_hash(str), get_hash(P))
    
