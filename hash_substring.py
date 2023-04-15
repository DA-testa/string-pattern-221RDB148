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
        return False
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
    return ("as","sdasaP")

def get_hash(str):
    B = 256

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    ##sitie ir numbers, kur atkartojas fraze 
    print(next_prime(1000))
    print("asd")
    return [0, "asd", 2.8]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

