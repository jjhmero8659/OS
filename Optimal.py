

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
                for j in range(0,len(frame)):
                    try:
                        if(Reference_string.index(frame[j],i+1,len(Reference_string))):
                            distance[j] = Reference_string.index(frame[j],i+1,len(Reference_string))
                    except:
                        distance[j] = 999
                print(f"distance : {distance}")
                    
                max_distance = max(distance)
                max_distance_index = distance.index(max_distance)
                
                print(f"miss 한 숫자는 Reference_string[{i}] : {Reference_string[i]}")
                frame[max_distance_index] = Reference_string[i]
                

def print_result():
    
    global page_fault,count
    print("Optimal 입니다.")
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