def main():
    arrival_times = list(map(int, input().split())) 
    burst_times = list(map(int, input().split())) 
    
    n = len(arrival_times)
    process_list = [] 
    
    for i in range(n):
        process_list.append([burst_times[i],arrival_times[i],i]) 
    # process_list.sort() Here we'll sort available array itself 
    
    time = 0
    completed = {}
    
    org_burst_times = {}
    for p in process_list:
        pid = p[2]
        org_burst_times[pid] = p[0]
    
    while len(completed)<n:
        available = []
        for p in process_list:
            at = p[1]
            if at <= time:
                available.append(p) 
        if available == []:
            time+=1 
        else:
            available.sort() # so at this time instant, some processes are available 
            # pick the first process
            process = available.pop(0)
            # execute it for one sec 
            process[0]-=1 # modifying process[0] modifies the org list, as it refers to org list only
            time+=1
            # check if it is completed or not. If completed, add it to completed list.
            if process[0]==0: # meaning, burst time became 0 or process is completed
                pid = process[2]
                bt = org_burst_times[pid]
                at = process[1]
                ct = time 
                tat = ct - at 
                wait = tat - bt 
                completed[pid]=[ct,tat,wait]
                process_list.remove(process) # finally remove the process from process_list
            # otherwise, add the process back to process_list with updated burst time
            # no need of else part, because if the process was not completed, it is already in 
            # the list with updated burst time
    
    tatSum = sum(value[1] for value in completed.values())
    waitSum = sum(value[2] for value in completed.values())
    
    print(waitSum//n)
    print(tatSum//n)
                
        

if __name__=="__main__":
    main()