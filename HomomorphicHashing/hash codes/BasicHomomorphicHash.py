# Reference used: 
## https://dzone.com/articles/algorithm-week-homomorphic
## Sub References: https://www.cs.cmu.edu/~rwh/theses/okasaki.pdf, https://pdos.csail.mit.edu/papers/otfvec/paper.pdf, 

# Constants used in the hash function
## Choose prime p
p = 257
## Choose q such that `p % q == 1` or `q | (p - 1)`
q = 257*6 + 1
## a random number g
g = 47

# hash message
m = [72, 101, 108, 108, 111]
h = []

# variables used in the hash function
sum = 0
product = 1

# compute the hash
## hash individual characters
## compute the hash of each individual character by raising g to the power of the character (mod q)
## compute the "sum" of the hashes of the individual characters by multiplying them (mod q)
for i in range(len(m)):
    h.append(pow(g, m[i], q))
    product *= h[i]
    product %= q
product_hash = product


## compute the sum of the characters
## hash that sum by raising g to the power of the sum (mod q)
for i in range(len(m)):
    sum += m[i]
    sum %= p
sum_hash = pow(g, sum, q)

print("message: ", m)
print("hashes: ", h)
print("sum_hash (hashing entire message): ", sum_hash)
print("product (hashing each block and then adding the hashes):", product_hash)

if(sum_hash == product_hash):
    print("Hashes are equal!")

