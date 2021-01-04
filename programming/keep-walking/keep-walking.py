#!/usr/bin/env python3
#Pseudo code: Set X = 1, Y = 1, previous answer = 1, answer = X * Y + previous answer + 3
#After that => X + 1 and Y + 1 ('answer' becomes 'previous answer') and repeat this till you have X = 525.
#The flag is the value of 'answer' when X = 525. {FLAG: 48373851}
#Example: 5 = 1 * 1 + 1 + 3, 12 = 2 * 2 + 5 + 3, 24 = 3 * 3 + 12 + 3

X = 1
Y = 1
prev_ans = 1

while X != 526:
    answer = X * Y + prev_ans + 3
    print(str(answer) + " = " + str(X) + " * " + str(Y) + " + " + str(prev_ans) + " + 3")
    X += 1
    Y += 1
    prev_ans = answer
