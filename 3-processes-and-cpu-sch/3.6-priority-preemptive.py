def main():
    arrival_times = list(map(int, input().split()))
    burst_times = list(map(int, input().split()))
    priorities = list(map(int, input().split()))
    
    n = len(arrival_times)
    process_list = [] 
    
    for i in range(n):
        process_list.append([priorities[i], arrival_times[i],burst_times[i], i]) 
    # don't sort now! 
    
    time = 0
    completed = {}
    
    org_burst_times = {}
    for p in process_list:
        pid = p[3]
        org_burst_times[pid]=p[2]
    
    while len(completed)<n: 
        available = [] 
        for p in process_list:
            at = p[1]
            if at <= time: 
                available.append(p) 
        
        if available == []:
            time+=1
        else:
            # available is not empty, sort and execute the first process for 1 unit of time 
            available.sort() 
            process = available.pop(0)
            process[2]-=1 # burst_time - 1
            time+=1
            if process[2]==0: # if burst time becomes zero  
                ct = time 
                pid = process[3]
                at = process[1]
                bt = org_burst_times[pid]
                tat = ct - at 
                wait = tat - bt 
                completed[pid]=[ct,tat,wait] 
                process_list.remove(process)
    
    tatSum = sum(value[1] for value in completed.values())
    waitSum = sum(value[2] for value in completed.values())
    
    print(waitSum//n)
    print(tatSum//n)

if __name__=="__main__":
    main()