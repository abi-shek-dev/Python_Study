x = input()

dic = {}

curr_ch = ''

for ch in x :

    curr_ch += ch

    count = x.count(curr_ch)
    dic[curr_ch] = count

ans = ""
max_count = 0
    

for key,value in dic.items():

    if value > max_count or (value == max_count and len(key) > len(ans)):

        ans, max_count = key, value

print(ans)
print(max_count)