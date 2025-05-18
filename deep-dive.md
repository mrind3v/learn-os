# OS: Deep Dive

## Table of Contents
- [Buses](#buses)
  - [Types of Buses](#types-of-buses)
  - [Expansion Buses](#expansion-buses)
  - [Case Study](#case-study)
- [Computer System Architecture](#computer-system-architecture)
- [Operating Systems Operations](#operating-systems-operations)
  - [Kernel](#kernel)
  - [Operations of OS](#operations-of-os)
  - [Case Studies](#case-studies)
- [Services provided by Operating System](#services-provided-by-operating-system)

## Today's Content

- Buses
- Computer architecture
  - Single processor
  - Multi processor
- Operating System Operations
  - Kernels
- Operating system services
  - Interfaces
  - Sys calls
  - Bottle Necks

## Buses

Buses are wires that carry information, serving as a bridge between RAM & CPU. They help in transmitting data, address, or control signals from CPU to RAM or RAM to CPU.

### Types of Buses

**1. Data bus**
- Transfers actual data between processor & memory
- Wider data bus means more bits transferred per cycle
- 64 bits → 64 bits transferred in one CPU cycle

**2. Address bus**
- Carries address in memory where we need to write or read data
- Size determines addressable memory:
  - 16 bit → 2^16 = 64 KB
  - 32 bit → 2^32 = 4 GB
- A 32-bit address bus can only store addresses up to 4 GB, so with 8 GB RAM, we need a proper address bus

**3. Control Bus**
- Carries signals which control activities (read, write, interrupts)
- Responsible for coordinating between buses

### Expansion Buses

**1. PCIe (Peripheral Component Interconnect Express)**
- High speed bus for CPU & SSD
- Used for graphical cards/WiFi cards

**2. Other expansion buses**
- USB / HDMI / Thunderbolt / SATA

### Case Study

M3 Pro (192-bit) vs M1 Pro & M2 Pro (256-bit) memory bus:
- M3 Pro is better at power usage and cache management
- For transferring large data (video editing, ML model training), the narrower bus can become a bottleneck

## Computer System Architecture

**1. Single processor system**
- One CPU with one processing core executes instructions
- Can run only one query at a time
- Example: Nokia phones where you could run only one app at a time

**2. Multiprocessor system**
- Two or more processors, each with a single core CPU
- All processors share computer bus, memory and devices
- More work completed in less time

**3. Multicore system**
- One CPU/processor containing multiple cores

**Benefits of Multicore systems:**
- Less power consumption
- In-chip communication is faster compared to multiprocessor systems

## Operating Systems Operations

Operating systems provide an environment where programs can be executed. A program in execution is called a process.

**Bootstrap Process:**
1. Turn on computer → Bootstrap Program loads
2. Loads kernel into memory
3. Kernel provides services to users and applications

**Kernel**
- Brain of the operating system
- Core component responsible for executing all low-level instructions
- Handles memory management, CPU scheduling, I/O devices

### Operations of OS

**1. Multiprogramming & Multitasking**
- Multiprogramming: OS has multiple programs to execute; next process gets a chance when first process is waiting for I/O or has terminated
- Multitasking: Switches between processes based on a timer (context switching)

**2. Resource Management**
- Process management:
  - Creating and deleting user and system processes
  - Scheduling processes and threads on CPUs
  - Suspending and resuming processes
  - Providing mechanisms for process synchronization and communication
- Memory Management
- File storage management
- Cache management

**3. Security & Protection**

**4. Virtualization**
- Allows one physical computer to behave like many separate computers

### Case Studies

**Case: Chrome + Docker + VS Code on 8GB RAM Systems**
- Source: Stack Overflow Developer Survey, Microsoft Dev Blogs
- Issue: Laptops becoming unusable when running development tools and browser simultaneously
- Docker consumes significant memory
- When RAM is full, OS uses hard disk/SSD as "virtual memory"
- Accessing data from RAM is ~100x faster than from disk

**Case: Microsoft Teams on Intel i5 Laptops During Screen Recording**
- Source: Reddit (r/sysadmin, r/Surface), Microsoft Support Forums
- Issue: Heavy lag and app crashes during video conferencing with screen sharing on dual-core CPUs

**Common Bottlenecks:**
- Memory bus
- CPU usage
- Cache size

## Services provided by Operating System

**User Interface**
- GUI (Graphical User Interface)
- CLI (Command Line Interface)
  - `mkdir` → make directory/folder
  - `pwd` → print path of current directory
  - `ls` → list all items
  - `rm file.txt` → remove file

**API**

---
Answer from Perplexity: pplx.ai/share