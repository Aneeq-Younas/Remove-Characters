def lis (nmbr):
    s_from= 2 - 0
    srt= 0
    len_num = (len(nmbr))

    while len_num > 0:
        srt = (s_from + srt) % len_num
        print(nmbr.pop(srt))
        len_num -=1

elem = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lis(elem)
