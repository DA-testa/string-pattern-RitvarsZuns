#python3

def read_input():
    input_type = input().rstrip()

    if input_type == 'F':
        with open(f"tests/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()

    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    P = len(pattern)
    T = len(text)
    prime = 1000000007  # A big prime number to avoid collisions

# Calculate powers of prime
    p_pow = [1]
    for i in range(1, P):
        p_pow.append((p_pow[i-1] * 31) % prime)

# Calculate hash values for pattern and the first window of text
    pattern_hash = 0
    for i in range(P):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * p_pow[P-i-1]) % prime

    text_hash = 0
    for i in range(P):
        text_hash = (text_hash + (ord(text[i]) - ord('a') + 1) * p_pow[P-i-1]) % prime

    occurrences = []

# Compare hash values and if they match, check if pattern and window are the same
    for i in range(T - P + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+P]:
                occurrences.append(i)
        if i < T - P:
        # Recalculate hash value for the next window
            text_hash = ((text_hash - (ord(text[i]) - ord('a') + 1) * p_pow[P-1]) * 31 + (ord(text[i+P]) - ord('a') + 1)) % prime
        # If the hash value becomes negative, make it positive again
            if text_hash < 0:
                text_hash += prime

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

