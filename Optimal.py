

Reference_string = []
frame = []
page_fault = 0;
distance = []
count = 0;

def init():
    global frame,Reference_string
    
    frame_length = int(input("frame의 길이를 입력해주세요: "))
    for i in range(0,frame_length):
        frame.append(-1)
        distance.append(-1)
    
    while(1):   
        input_int = int(input("숫자를 입력해주세요(-1 입력시 종료) : "))
        if(input_int == -1):
            print("종료!")
            break
        Reference_string.append(input_int)
        
def exe():
    global frame,Reference_string,page_fault,distance,count
    
    min_distance = 0
    min_distance_index = 0
    
    for i in range(0,len(Reference_string)):   #배열 숫자 대기열 길이만큼 반복
        count+=1
        
        if Reference_string[i] in frame: #해당 인덱스 대기열 숫자가 frame에 포함되어있다면? hit
            print(f"hit 한 숫자는 Reference_string[{i}] : {Reference_string[i]}")
            #total
            continue
        else:                            #해당 인덱스 대기열 숫자가 frame에 포함되어있지 않다면? miss
            page_fault+=1;               #pagefault++ 값증가
            if(-1 in frame): 
                frame[frame.index(-1,0,len(frame))] = Reference_string[i] 
                print(f"-1 miss 한 숫자는 Reference_string[{i}] : {Reference_string[i]}")
            else:               #배열안에 null이 없다면
                print("-1이 아닌 miss")
                for q in range(0,len(frame)): 
                    for a in range(i-1,0,-1): #현재위치 -1 부터 0까지 reverse 순환 
                        if(frame[q] == Reference_string[a]):  #프레임[q] 번째 값이 reverse 순환하는 Reference_string[a] 값과 같다면?
                            distance[q] = a                   #프레임[q]와 동일한 index의  distance[q] 에 a를 대입 (작을수록 least하다)
                            break                             #break
            
                    
                min_distance = min(distance)
                min_distance_index = distance.index(min_distance)
                
                print(f"miss 한 숫자는 Reference_string[{i}] : {Reference_string[i]}")
                frame[min_distance_index] = Reference_string[i]
                

def print_result():
    
    global page_fault,count
    
    print(f"Reference_string : {Reference_string}")
    print(f"frame : {frame}")
    print(f"distance : {distance}")
    
    print(f"전체 count는 {count}번 발생")
    print(f"page fault는 {page_fault}번 발생")
    

def main():
    init()
    exe()
    print_result()
    

main()