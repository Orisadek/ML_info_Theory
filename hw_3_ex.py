import numpy as np

seq = np.random.choice(7, 10000, p=[1 / 2, 1 / 8, 1 / 8, 1 / 16, 1 / 16, 1 / 16, 1 / 16])


print("Symbols - Start")
print("**************************************************")
print("Size:", len(seq))
for i in range(7):
    print("the percentage of", i, "is:")
    print(100 * (sum(seq == i) / 10000))

print("Before compression")
print("**************************************************")
seq2 = ['0'] * 10000
b0_before = 0
b1_before = 0
for i in range(7):
    bin_val = bin(i)[2:]
    for j in range(3 - len(bin_val)):
        bin_val = '0' + bin_val
    for z in range(10000):
        if seq[z] == i:
            seq2[z] = bin_val

seq2 = list(''.join(map(str, seq2)))

b0_before = seq2.count('0')
b1_before = seq2.count('1')

print("Size:", len(seq2))
print("Percentage of bit b ==0 :", 100 * (b0_before / len(seq2)))
print("Percentage of bit b ==1 :", 100 * (b1_before / len(seq2)))

print("After compression")
print("**************************************************")

dict_huffman = {0: '1', 1: "011", 2: "010", 3: "0011", 4: "0010", 5: "0001", 6: "0000"}
seq3 = ['0'] * 10000
b0_after = 0
b1_after = 0

for i in range(10000):
    seq3[i] = dict_huffman[seq[i]]

seq3 = list(''.join(map(str, seq3)))
b0_after = seq3.count('0')
b1_after = seq3.count('1')

print("Size:", len(seq3))
print("Percentage of bit b ==0 :", 100 * (b0_after / len(seq3)))
print("Percentage of bit b ==1 :", 100 * (b1_after / len(seq3)))
