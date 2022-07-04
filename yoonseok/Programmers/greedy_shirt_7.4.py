def solution(n, lost, reserve):
    answer = 0
    
    lost = list(set(lost))
    reserve = list(set(reserve))
    # 중복제거
    
    student =[]
    for i in range(1,n+1):
        student.append(i)
    
    have = list(set(student)-set(lost))
    cnt = 0
    
    for j in lost:
        if (j-1) in reserve:
            reserve.remove(j-1)
            cnt +=1
        elif (j+1) in reserve:
            reserve.remove(j+1)
            cnt +=1
                
    answer = int(len(have))+cnt
    
    
    
    
    return answer

#80퍼

------------------

def solution(n, lost, reserve):
    answer = 0
    
    lost = list(set(lost)-set(reserve))
    reserve = list(set(reserve)-set(lost))
    # 중복제거
    
    student =[]
    for i in range(1,n+1):
        student.append(i)
    
    have = list(set(student)-set(lost))
    cnt = 0
    
    for j in lost:
        if (j-1) in reserve:
            reserve.remove(j-1)
            cnt +=1
        elif (j+1) in reserve:
            reserve.remove(j+1)
            cnt +=1
                
    answer = len(have)+cnt
    
    
    
    
    return answer

#60퍼


---------- 
def solution(n, lost, reserve):
    answer = 0
    
    lost_n = list(set(lost)-set(reserve))
    reserve_n = list(set(reserve)-set(lost))
    # 중복제거
    
    student =[]
    for i in range(1,n+1):
        student.append(i)
    
    have = list(set(student)-set(lost_n))
    cnt = 0
    
    for j in lost_n:
        if (j-1) in reserve_n:
            reserve_n.remove(j-1)
            cnt +=1
        elif (j+1) in reserve_n:
            reserve_n.remove(j+1)
            cnt +=1
                
    answer = len(have)+cnt
    
    return answer


   # 100퍼