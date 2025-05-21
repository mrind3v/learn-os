# Processes and CPU Scheduling

## Table of Contents
- [Processes and CPU Scheduling](#processes-and-cpu-scheduling)
  - [Table of Contents](#table-of-contents)
  - [1. What is a Process?](#1-what-is-a-process)
    - [Process States](#process-states)
    - [Process Components](#process-components)
      - [Example: `open()` System Call (C)](#example-open-system-call-c)
    - [What are System Calls?](#what-are-system-calls)
    - [How System Calls Work](#how-system-calls-work)
    - [Most Common System Calls](#most-common-system-calls)
    - [Process Control Block (PCB)](#process-control-block-pcb)
    - [Process Lifecycle Flow](#process-lifecycle-flow)
  - [2. CPU Scheduling](#2-cpu-scheduling)
    - [CPU Scheduler](#cpu-scheduler)
    - [Preemptive vs Non-Preemptive Scheduling](#preemptive-vs-non-preemptive-scheduling)
    - [Scheduling Criteria and Terminology](#scheduling-criteria-and-terminology)
    - [Scheduling Algorithms](#scheduling-algorithms)
      - [First Come First Serve (FCFS)](#first-come-first-serve-fcfs)
      - [Shortest Job First (SJF)](#shortest-job-first-sjf)
      - [Priority Scheduling](#priority-scheduling)
      - [Round Robin (RR)](#round-robin-rr)
  - [3. Scheduling Queues](#3-scheduling-queues)
  - [4. Context Switching](#4-context-switching)
  - [5. CPU-bound vs I/O-bound Processes](#5-cpu-bound-vs-io-bound-processes)

---

## 1. What is a Process?

A **process** is a program in execution. It is an active entity, as opposed to a program, which is a passive set of instructions.

### Process States

A process moves through various states during its lifetime:
- **New:** Process is being created.
- **Ready:** Process is in RAM, waiting for CPU time.
- **Running:** Process is currently being executed by the CPU.
- **Waiting:** Process is waiting for some I/O operation or event.
- **Terminated:** Process has finished execution and is being removed from the system.

**Note:** Only one process can be running on any processor core at any instant.

### Process Components

A process consists of:
- **Program code:** The actual instructions.
- **Program counter:** Current position in program code.
- **Data:** Global/static variables.
- **Stack:** Function calls and local variables.
- **Heap:** Dynamically allocated memory.
- **Process Control Block (PCB):** Metadata about the process.

#### Example: `open()` System Call (C)
```c
#include 
#include 
#include 
int open(const char *pathname, int flags, mode_t mode) {
    return syscall(SYS_open, pathname, flags, mode);
}
```
**Kernel Implementation (Simplified):**
```c
asmlinkage long sys_open(const char __user *filename, int flags, umode_t mode) {
    return do_sys_open(AT_FDCWD, filename, flags, mode);
}

int do_sys_open(int dfd, const char __user *filename, int flags, umode_t mode) {
    struct open_flags op;
    struct filename *tmp;
    tmp = getname(filename); // Resolves user-space string
    if (IS_ERR(tmp))
        return PTR_ERR(tmp);
    // Parse flags like O_CREAT, O_TRUNC etc.
    int fd = do_filp_open(dfd, tmp, &op); // Opens file and returns file descriptor
    putname(tmp);
    return fd;
}
```

### What are System Calls?

A **system call** is the main way a user program interacts with the operating system. User programs (like your code or apps) run in **user mode**, which is restricted for safety and security. When a program needs to perform a privileged operation—such as accessing hardware, reading/writing files, creating processes, or communicating over the network—it must ask the OS to do it on its behalf. This request is made via a system call.

**Intuitive Analogy:**  
Think of the OS as a hotel manager and your program as a guest. If you want extra towels (access hardware), you can't just walk into the supply room (hardware). Instead, you call the front desk (system call), and the manager (OS) handles it for you.

### How System Calls Work

1. **User Program Requests Service:**  
   The program calls a library function (like `open()`, `read()`, `write()`, etc.), which prepares the system call.

2. **Mode Switch:**  
   The CPU switches from user mode to kernel mode (privileged mode) to safely execute the requested operation.

3. **OS Handles the Request:**  
   The OS checks permissions, performs the requested action (e.g., opens a file, allocates memory), and prepares a result.

4. **Return to User Mode:**  
   The OS switches back to user mode and returns the result to the program.

**Why not access hardware directly?**  
Direct access would be unsafe—bugs or malicious code could crash the system or steal data. System calls provide a controlled, secure interface.

### Most Common System Calls

- **Process Control:**  
  - `fork()`, `exec()`, `exit()`, `wait()`
  - Create, run, terminate, or wait for processes.

- **File Management:**  
  - `open()`, `close()`, `read()`, `write()`, `lseek()`
  - Open, close, read from, write to, or move within files.

- **Device Management:**  
  - `ioctl()`, `read()`, `write()`
  - Interact with hardware devices.

- **Information Maintenance:**  
  - `getpid()`, `alarm()`, `sleep()`
  - Get process ID, set timers, pause execution.

- **Communication:**  
  - `pipe()`, `shmget()`, `mmap()`, `msgget()`, `socket()`
  - Inter-process communication (IPC), shared memory, sockets for networking.

**Summary:**  
System calls are the "gateways" between user programs and the OS, ensuring safe and controlled access to system resources.

### Process Control Block (PCB)

The **PCB** is a data structure maintained by the OS that contains all the information needed to manage a process. It is like the ID card of a process.

**Purpose of PCB:**
- Context switching
- Scheduling the process

### Process Lifecycle Flow

1. **New Process → Ready Queue:** Process is created and enters the ready queue.
2. **Dispatched → CPU:** Scheduler selects the process and assigns it to a CPU core.
3. **While Running, three things can happen:**
   - I/O Request → moved to I/O wait queue
   - Child Process Created → moved to wait queue
   - Interrupted/Time Slice Over → returned to ready queue
4. **Event Completes:** Process moves from wait queue to ready queue.
5. **Termination:** Process is removed from all queues and resources are deallocated.

---

## 2. CPU Scheduling

### CPU Scheduler

Schedulers ensure process execution alternates between CPU bursts and I/O bursts.

### Preemptive vs Non-Preemptive Scheduling

- **Preemptive:** Context switching can happen at any time (e.g., time slice expires, higher priority process arrives).
- **Non-Preemptive:** Once a process starts, it runs to completion or until it waits for I/O.

### Scheduling Criteria and Terminology

- **Response time:** Time from submission of request until first response is produced.
- **Waiting time:** Time spent waiting in the ready queue.
- **CPU utilization:** Keeping the CPU as busy as possible.
- **Turnaround time:** Time from submission to completion.

**Key Terms:**
- **Arrival time:** When process enters the ready queue.
- **Burst time:** Time required by a process for execution on CPU.
- **Completion time:** When process finishes execution.
- **Turnaround time (TAT):** Completion time - Arrival time (total time the CPU took from arrival of the process to completing execution)
- **Waiting time:** Turnaround time - Burst time (Burst time is the actual time needed for the process to be executed by the CPU, but it took the CPU, Turnaround amount of time to actually finally complete the process. So wait time is the extra amount of time for complete process execution)

---

### Scheduling Algorithms

#### First Come First Serve (FCFS)

- Non-preemptive (no context-switching), queue-based (FIFO).
- First process arrived will be executed first (so sort processes based on arrival time)

| Process | Arrival | Burst | Start | Completion | Wait | TAT |
|---------|---------|-------|-------|------------|------|-----|
| P0      | 0       | 4     | 0     | 4          | 0    | 4   |
| P1      | 1       | 3     | 4     | 7          | 3    | 6   |
| P2      | 2       | 1     | 7     | 8          | 5    | 6   |
| P3      | 3       | 2     | 8     | 10         | 5    | 7   |

**Average waiting time:** $$(0+3+5+5)/4 = 3.25$$

#### Shortest Job First (SJF)

- Non-preemptive.
- Process with the shortest burst time is executed next.

| Process | Arrival | Burst | Start | Completion | TAT | WT  |
|---------|---------|-------|-------|------------|-----|-----|
| P1      | 1       | 3     | 3     | 6          | 5   | 2   |
| P2      | 2       | 4     | 6     | 10         | 8   | 4   |
| P3      | 1       | 2     | 1     | 3          | 2   | 0   |
| P4      | 4       | 4     | 10    | 14         | 10  | 6   |

#### Priority Scheduling

- Each process is assigned a priority.
- CPU is allocated to the process with the highest priority (lower value = higher priority, by convention).

| Process | Arrival | Burst | Priority | Start | Completion | TAT | WT  |
|---------|---------|-------|----------|-------|------------|-----|-----|
| P1      | 0       | 10    | 2        | 0     | 10         | 10  | 0   |
| P2      | 1       | 4     | 1        | 10    | 14         | 13  | 9   |
| P4      | 3       | 3     | 2        | 14    | 17         | 14  | 11  |
| P3      | 2       | 5     | 3        | 17    | 22         | 20  | 15  |

- If preemptive, check priorities at every time quantum.

#### Round Robin (RR)

- Preemptive scheduling algorithm.
- Each process gets a fixed time slice (quantum).
- If not finished, process is moved to the back of the queue.

**How it works:**
1. All processes are added to a ready (FIFO) queue.
2. CPU scheduler picks the first process.
3. Process is given CPU for a fixed time quantum.
4. If finished, it is removed. If not, it's preempted and placed at the back.
5. Repeat until all processes are complete.

| Process | Arrival | Burst | Start | Completion | TAT | WT  |
|---------|---------|-------|-------|------------|-----|-----|
| P1      | 0       | 8     | 0     | 21         | 21  | 13  |
| P2      | 1       | 5     | 4     | 20         | 19  | 14  |
| P3      | 2       | 10    | 8     | 27         | 25  | 15  |
| P4      | 3       | 6     | 12    | 24         | 21  | 15  |

---

## 3. Scheduling Queues

- **Job Queue:** Contains newly created processes.
- **Ready Queue:** Contains processes ready to run.
- **Waiting Queue:** Contains processes waiting for an event (e.g., I/O).

---

## 4. Context Switching

A **context switch** is the act of:
1. Saving the context of the currently running process in its PCB.
2. Loading the context of the next process.

**Context switches occur:**
- On interrupts
- When time slice expires
- When a higher priority process arrives

---

## 5. CPU-bound vs I/O-bound Processes

- **I/O-bound process:** Spends more time waiting for I/O operations (e.g., reading files, printing).
  - CPU burst time is low.
- **CPU-bound process:** Spends most of the time doing computations (e.g., mathematical processing, encryption).
  - CPU burst time is high.

