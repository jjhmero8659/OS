
from dis import dis


Reference_string = []
frame = []
page_fault = 0;
page_count = []
count = 0;
distance = []

def init():
    global frame,Reference_string
    
    frame_length = int(input("frame의 길이를 입력해주세요: "))
    for i in range(0,frame_length):
        frame.append(-1)
        page_count.append(-1)
        distance.append(-1)
    
    while(1):   
        input_int = int(input("숫자를 입력해주세요(-1 입력시 종료) : "))
        if(input_int == -1):
            print("종료!")
            break
        Reference_string.append(input_int)
        
def exe():
    global frame,Reference_string,page_fault,page_count,count,distance
    
    max_page = 0
    max_page_index = 0
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
                print("")
            else:               #배열안에 null이 없다면
                print("-1이 아닌 miss")
                for h in range(0,len(page_count)): #count 배열 초기화
                    page_count[h] = 0;
                    distance[h] = -1;
                
                for q in range(0,len(frame)): #프레임 길이만큼 반복
                    for a in range(i-1,-1,-1): #현재위치 -1 부터 0까지 reverse 순환
                        if(frame[q] == Reference_string[a]):  #프레임[q] 번째 값이 reverse 순환하는 Reference_string[a] 값과 같다면?
                            page_count[q] += 1                   #해당 프레임 index에 해당하는page_count[q]의 count 증가
                            print(f"a : {a} Reference_string[a] : {Reference_string[a]}")
                            if(distance[q] == -1):            #distance 가 -1 이라면 쓰레기 값이니 값 대입
                                print(f"distance!!")
                                distance[q] = a              #해당하는 대기숫자 index값 대입
                            
                # print(f"distance : {distance}")               #distance 값 출력
                
                max_page = max(page_count) #count 가 가장많은 숫자
                max_page_index = page_count.index(max_page) # 해당하는 count의 index
                
                for b in range(0,len(page_count)):
                    if(page_count[b] != max_page):
                        distance[b] = 999
                
                
                min_distance = min(distance)
                min_distance_index = distance.index(min_distance)
                frame[min_distance_index] = Reference_string[i]
                
                
                print(f"miss 한 숫자는 Reference_string[{i}] : {Reference_string[i]}")
                
                
                print(f"frame : {frame}")
                print(f"page_count : {page_count}")
                print("")
                

def print_result():
    global page_fault,count,page_count
    print("MFU입니다.")
    print(f"Reference_string : {Reference_string}")
    print(f"frame : {frame}")
    print(f"distance : {page_count}")
    
    print(f"전체 count는 {count}번 발생")
    print(f"page fault는 {page_fault}번 발생")
    

def main():
    init()
    exe()
    print_result()
    

main()

# 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1       714 fault 14 