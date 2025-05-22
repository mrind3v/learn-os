def main():
    arrival_times = list(map(int, input().split()))
    burst_times = list(map(int, input().split()))
    priorities = list(map(int, input().split()))
    
    n = len(arrival_times)
    process_list = [] 
    
    for i in range(n):
        # if priorities of two processes are same, .sort() method will sort 
        # according to arrival time
        process_list.append([priorities[i],arrival_times[i],burst_times[i],i])
    process_list.sort() 
    
    time = 0
    completed = {}
    
    while len(completed)<n: 
        available = []
        for p in process_list: 
            at = p[1]
            if at <= time:
                available.append(p)
        if available==[]:
            inc_time = int('inf') 
            for p in process_list:
                inc_time = min(inc_time, p[1])
            time = inc_time
        else:
            process = available.pop(0)
            at = process[1]
            bt = process[2]
            pid = process[3]
            time+=bt 
            ct = time 
            tat = ct - at 
            wait = tat - bt 
            completed[pid] = [ct,tat,wait]
            process_list.remove(process)
    
    tatSum = sum(value[1] for value in completed.values())    
    waitSum = sum(value[2] for value in completed.values())    
    print(waitSum//n) 
    print(tatSum//n)



if __name__=='__main__':
    main()