''' In this challenge, you will use logical bitwise operators. All data is stored in its binary representation. The logical operators, use 1 to represent true and 0 to represent false. The logical operators compare bits in two numbers and return true or false, 0 or 1, for each bit compared.

Bitwise AND operator & The output of bitwise AND is 1 if the corresponding bits of two operands is 1. If either bit of an operand is 0, the result of corresponding bit is evaluated to 0. It is denoted by &.

Bitwise OR operator | The output of bitwise OR is 1 if at least one corresponding bit of two operands is 1. It is denoted by |.

Bitwise XOR (exclusive OR) operator ^ The result of bitwise XOR operator is 1 if the corresponding bits of two operands are opposite. 
Code '''
n1, n2 = map(int, input().split())
k = int(input())

re_and = n1 & n2
re_or = n1 | n2
re_xor = n1 ^ n2

# apply filter 
re_and *= (k > re_and)
re_or *= k > re_or
re_xor *= k > re_xor

# display maximum
out = max(re_and, re_or, re_xor)

print(out)
     
