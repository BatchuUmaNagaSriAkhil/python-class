#find the length of consecutive sequence
#input:[100,4,200,1,3,2]
#output:[4]   1,2,3,4

a = [100,4,200,1,3,2]
s = set(a)
count = 0

while s:
    x = s.pop()
    left = x - 1
    right = x + 1
    length = 1
    
    while left in s:
        s.remove(left)
        length += 1
        left -= 1

    while right in s:
        s.remove(right)
        length += 1
        right += 1
        count = max(count, length)

print(count)