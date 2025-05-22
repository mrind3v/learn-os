def main():
    arrival_times = list(map(int, input().split())) 
    burst_times = list(map(int, input().split())) 
    
    n = len(arrival_times) 
    process_list = [] 
    
    for i in range(n):
        process_list.append([ burst_times[i], arrival_times[i], i])
    process_list.sort()
    
    completed = {}
    time = 0
    
    while len(completed)<n:
        available = []
        for p in process_list: 
            at = p[1]
            if at <= time:
                available.append(p) 
        if available == []:
            # figure out the process with lowest arrival time in process_list, and increase
            # it to that amount 
            time += process_list[0][1]
        else:
            process = available.pop(0)
            at = process[1]
            bt = process[0]
            pid = process[2]
            time+=bt 
            ct = time 
            tat = ct-at 
            wait = tat-bt 
            completed[pid] = [ct,tat,wait]
            process_list.remove(process) 
    
    tatSum = sum(value[1] for value in completed.values())
    waitSum = sum(value[2] for value in completed.values()) 
    
    print(waitSum//n)
    print(tatSum//n)
    

if __name__="__main__":
    main()