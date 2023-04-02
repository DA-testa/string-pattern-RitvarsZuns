# python3

def read_input():
    input_type = input().strip().upper()
    if input_type == 'F':
        with open(f"tests/06") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()

    return pattern, text
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007 # A large prime number
    x = 1
    h_pattern = 0
    h_text = 0
    occurrences = []
    # Calculate the hash value of the pattern and the first window in the text
    for i in range(len(pattern)):
        h_pattern = (h_pattern + ord(pattern[i]) * x) % p
        h_text = (h_text + ord(text[i]) * x) % p
        x = (x * 263) % p

# Slide the window across the text and calculate the hash value of the new window at each step
    for i in range(len(text) - len(pattern) + 1):
        if h_pattern == h_text:
            if pattern == text[i:i+len(pattern)]:
                occurrences.append(i)

        if i < len(text) - len(pattern):
        # Calculate the hash value of the next window
            h_text = (h_text - ord(text[i]) + ord(text[i+len(pattern)]) * x) % p

    return occurrences

    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    #return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

