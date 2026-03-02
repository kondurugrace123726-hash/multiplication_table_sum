#input

n = int(input().strip())
total = 0

# calculate sum of first 10 multiples

for i in range(1, 11):
    total += i * n

#print the output

print(total)