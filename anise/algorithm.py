from dis import code_info


N = int(input("배달해야하는 설탕(Kg) : "))
count = 0

array = [5,3]


for sugar in array :
    if N//sugar < 1 :
        print(-1)
        break
    else :
        count += N // sugar
        N %= sugar

print(count)
