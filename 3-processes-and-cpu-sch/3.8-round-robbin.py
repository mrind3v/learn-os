from collections import deque

def main():
    arrival_times = list(map(int, input().split()))
    burst_times = list(map(int, input().split()))
    tq = int(input())
    
    n = len(arrival_times)
    process_list = []
    
    for i in range(n):
        process_list.append([arrival_times[i],burst_times[i],i]) 
    process_list.sort() # sort even tho it is preemptive 
    
    time = 0
    completed = {} 
    
    org_burst_times = {}
    for p in process_list:
        pid = p[2]
        org_burst_times[pid]=p[1]
    
    ready_queue = deque()
    added_to_ready_queue = set()
    curr_process_ref = None
    current_quantum_used = 0
    
    while len(completed)<n: 
        for p in process_list:
            at = p[0]
            pid = p[2]
            if at <= time and pid not in added_to_ready_queue:
                ready_queue.append(p)
                added_to_ready_queue.add(pid) 
            
        # if no processes are running currently in CPU
        if curr_process_ref is None:
            # if there are processes in ready queue, get the next process acc to arrival time
            # and let it be executed
            if ready_queue:
                curr_process_ref = ready_queue.popleft() 
                current_quantum_used = 0 # new process is being executed, so reset counter
            else:
                time+=1
                continue
        # if there is actually a process running in CPU - simulate process executed by CPU
        
        curr_process_ref[1]-=1
        current_quantum_used+=1
        time+=1
        
        # after executing process in CPU, if current process burst time becomes zero
        # meaning, completed execution - add it to the completed dic
        if curr_process_ref[1]==0:
            pid = curr_process_ref[2]
            at = curr_process_ref[0]
            bt = org_burst_times[pid] 
            ct = time 
            tat = ct - at 
            wait = tat - bt 
            completed[pid] = [ct,tat,wait]
            process_list.remove(curr_process_ref)    
            curr_process_ref=None # cpu is now free  
        # if process couldn't be completed due to time quanta expiry
        elif current_quantum_used==tq:     
            ready_queue.append(curr_process_ref)
            curr_process_ref = None # cpu is now free 
    
    tatSum = sum(value[1] for value in completed.values())
    waitSum = sum(value[2] for value in completed.values())
    
    print(waitSum//n)
    print(tatSum//n)



if __name__=="__main__":
    main()