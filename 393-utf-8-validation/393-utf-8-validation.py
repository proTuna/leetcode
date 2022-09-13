class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        start,end = 0, len(data)
        while start<end:
            d, j = data[start],7
            while j>=0 and (d>>j)&1 == 1: j-=1
            cnt= 7-j # n-bytes
            if cnt == 1 or cnt >4: return False # 1이 한개로시작하거나 4개 보다 큰 것은 존재하지 않는다.
            if cnt == 0: # 1-byte이므로 다음으로 넘어간다
                start+=1
                continue
            cnt-=1 # n-byte의 경우에는 앞의 n-1개 만큼 체크해봐야하기 때문에 1을 빼준다.
            start+=1
            if end-start<cnt: # 앞에 남아있는 byte가 부족하면 False를 반환한다.
                return False
            while cnt>0:
                c = data[start] >> 6
                if c & 1 == 0 and (c>>1) & 1 == 1:
                    start+=1
                    cnt-=1
                else:
                    return False
        return True
                