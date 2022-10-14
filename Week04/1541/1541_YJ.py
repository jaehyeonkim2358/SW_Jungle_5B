exp  = input()
nums = []
operators= ['+']
brake = 0

for i in range(len(exp)+1):
    if i == len(exp) :
        nums.append(int(exp[brake:i]))
    elif exp[i] =='+' or exp[i] == '-' :
        nums.append(int(exp[brake:i]))
        operators.append(exp[i])
        brake = i+1 

operator = '+'
total = 0

for i in range(len(nums)) :
    if operators[i] == '-' :
        operator = '-'
    if operator == '+' :
        total += nums[i]
    else: 
        total -= nums[i]

print(total)