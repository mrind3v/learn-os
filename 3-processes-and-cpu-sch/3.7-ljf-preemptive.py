def main():
    arrival_times = list(map(int, input().split())) 
    burst_times = list(map(int, input().split()))
    
    n = len(arrival_times)
    process_list = []
    
    for i in range(n): 
        process_list.append([burst_times[i], arrival_times[i],i]) 
    # don't sort, it's PREEMPTIVE! 
    
    time = 0
    completed = {}
    
    org_burst_times = {}
    for p in process_list: 
        pid = p[2]
        org_burst_times[pid]=p[0]
    
    while len(completed)<n: 
        available = [] 
        for p in process_list:
            at = p[1]
            if at <= time: 
                available.append(p) 
        if available == []:
            time+=1
        else:
            available.sort(reverse=True) 
            process = available.pop(0) 
            process[0]-=1
            time+=1 
            if process[0]==0:
                pid = process[2]
                at = process[1]
                bt = org_burst_times[pid]
                ct = time 
                tat = ct - at 
                wait = tat - bt 
                completed[pid]=[ct,tat,wait]
                process_list.remove(process)
    
    tatSum = sum(value[1] for value in completed.values())
    waitSum = sum(value[2] for value in completed.values())
    
    print(waitSum//n)
    print(tatSum//n)

if __name__ == "__main__":
    main()