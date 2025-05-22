def main():    
    arrival_times = list(map(int, input().split()))
    burst_times = list(map(int, input().split()))

    n = len(arrival_times) 
    process_list = []

    for i in range(n):
        process_list.append([arrival_times[i], burst_times[i],i]) 
    process_list.sort()

    time = 0
    completed = {} 

    while len(completed)<n:
        available  = [] 
        for p in process_list:
            at = p[0]
            if at <= time:
                available.append(p)
        if available == []:
            time += 1 
        else:
            # meaning, available has processes in it. So process the first process in it 
            process = available.pop(0)
            at = process[0]
            bt = process[1]
            pid = process[2]
            time+=bt 
            ct = time 
            tat = ct - at
            wait = tat - bt
            completed[pid]=[ct,tat,wait]
            # since our process has gone into the completed map, remove it from the processes list 
            process_list.remove(process) 

    tatSum = sum(value[1] for value in completed.values())
    waitSum = sum(value[2] for value in completed.values())

    print(tatSum//n)
    print(waitSum//n)
    
    
    if __name__=="__main__":
        main()