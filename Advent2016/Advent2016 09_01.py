#lines = ["ADVENT","A(1x5)BC","(3x3)XYZ","A(2x2)BCD(2x2)EFG","(6x1)(1x3)A","X(8x2)(3x3)ABCY"]
#lines = ["A(2x2)BCD(2x2#)EFG"]
with open("input09.txt") as f:
   lines = [x.strip() for x in f.readlines()]

sum = 0
for i in lines:
    idx = 0
    i = i.replace(" ","")
    print(i)
    while idx < len(i):
        if i[idx] == "(":
            start = idx
            while i[idx] != ")":
                if i[idx] == "x": x_pos = idx
                idx += 1
            marker_len = int(i[start+1:x_pos])
            marker_repeat = int(i[x_pos+1:idx])
            marker_cont = i[idx+1:idx+1+marker_len]
            i = i[:start] + marker_cont*marker_repeat + i[idx+marker_len+1:]
            idx = idx + marker_len * (marker_repeat-1) - 2
        idx += 1
    sum += len(i.strip())
    print(i)
    print(len(i))
print(sum)
