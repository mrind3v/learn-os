# OS: Deep Dive

## Table of Contents
- [Buses](#buses)
  - [Types of Buses](#types-of-buses)
    - [Data Bus](#1-data-bus)
    - [Address Bus](#2-address-bus)
    - [Control Bus](#3-control-bus)
  - [Interplay Between the Buses](#interplay-between-the-buses-an-example)
  - [Expansion Buses](#expansion-buses)
  - [Case Study](#case-study)
- [Computer System Architecture](#computer-system-architecture)
  - [Single Processor System](#1-single-processor-system)
  - [Multiprocessor System](#2-multiprocessor-system)
  - [Multicore System](#3-multicore-system)
- [Operations of OS](#operations-of-os)
  - [Multiprogramming & Multitasking](#1-multiprogramming--multitasking)
  - [Resource Management](#2-resource-management)
  - [Security & Protection](#3-security--protection)
  - [Virtualization](#4-virtualization)
- [Case Studies](#case-studies)
  - [Development Environment](#case-1-development-environment-on-8gb-ram)
  - [Video Conferencing](#case-2-video-conferencing-with-screen-share)
  - [Common Bottlenecks](#common-bottlenecks-explained)


## Buses

Buses are physical communication pathways on the motherboard that connect various computer components. They act as a universal communication system for:

**Components Connected by Buses:**
- CPU to RAM
- CPU to Cache
- CPU to Input/Output devices
- CPU to Storage devices (HDD/SSD)
- RAM to Graphics Card
- Motherboard to Expansion Cards

### Types of Buses

**1. Data bus**
- Transfers actual data between processor & memory
- Wider data bus means more bits transferred per cycle
- 64 bits → 64 bits transferred in one CPU cycle
- Bidirectional (data can flow both ways)


**2. Address bus**
- Carries memory addresses from CPU to memory components
- Unidirectional (CPU → memory only)
- Works together with data and control buses
- Size determines addressable memory:
  - 16-bit address bus example:
    * Has 16 wires/lines carrying binary signals
    * Each combination represents a unique memory address
    * Total possible combinations = 2^16 = 65,536
    * Each address points to ONE byte of memory
    * Therefore: 65,536 unique addresses × 1 byte = 65,536 bytes = 64 KB
    * Note: The 16-bit width of address bus only determines number of unique locations,
           not the size of data at each location
  - 32-bit address bus:
    * Total possible addresses = 2^32
    * Each address points to 1 byte
    * Total addressable memory = 2^32 bytes = 4 GB
- A 32-bit address bus can only store addresses up to 4 GB, so with 8 GB RAM, we need a proper address bus

**3. Control Bus**
- Coordinates operations between components
- Carries signals like:
  * Read/Write commands
  * Memory ready signals
  * Interrupt signals
  * Clock signals
  * Error signals

### Interplay Between the Buses (an Example)

**Reading from Memory:**
1. CPU needs data (triggered by instruction like `MOV AX, [1000H]`)
2. Control Unit in CPU:
   - Activates memory read signal on control bus (goes to memory)
   - Places address 1000H on address bus (connects to memory)
3. Memory responds to read signal:
   - Recognizes address on address bus
   - Places data from that location onto _data bus_
4. CPU:
   - Reads data from data bus
   - Stores it in specified register (AX)
5. Control Unit deactivates read signal

**Writing to Memory:**
1. CPU needs to write data (triggered by instruction like `MOV [2000H], BX`)
2. Control Unit in CPU:
   - Activates memory write signal on control bus (goes to memory)
   - Places address 2000H on address bus (connects to memory)
   - Places data from BX register on data bus (goes to memory)
3. Memory responds to write signal:
   - Recognizes address on address bus
   - Takes data from data bus
   - Stores it at specified address
4. Control Unit deactivates write signal


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
- System with multiple processors (CPUs)
- Each processor can execute instructions independently

**Real-world Example:**
- While one processor is:
  * Handling your video call
  * Another processor can simultaneously:
    - Process your spreadsheet calculations
    - Handle background music playing
    - Run your antivirus scan

**Advantages:**
- True parallel execution (multiple things happening at exact same time)
- Better performance for multiple tasks
- System keeps running even if one processor fails

**3. Multicore system**
- One CPU/processor containing multiple cores

**Benefits of Multicore systems:**
- Less power consumption
- In-chip communication is faster compared to multiprocessor systems


### Operations of OS

**1. Multiprogramming & Multitasking**

**Multiprogramming:**
- A technique that allows multiple programs to reside in main memory and be executed by a single processor concurrently
- The primary goal of multiprogramming is to maximize CPU utilization by keeping the CPU busy as much as possible.
- When one program waits for I/O, CPU switches to another program
- Like a chef working on multiple dishes:
  * While waiting for water to boil (I/O wait)
  * Chef starts chopping vegetables for another dish (CPU utilization)
  * No time is wasted waiting


**Multitasking:**
- Extension of multiprogramming
- Switches between programs based on timer (time slicing)
- Like a teacher in a classroom:
  * Gives attention to each student for fixed time
  * Then moves to next student
  * Comes back to first student after helping others
  * Everyone gets CPU time, creating illusion of parallelism


**Differences:**
- Multiprogramming: Focus on keeping CPU busy
- Multitasking: Focus on frequent switching for interactive use
- Example:
  * Multiprogramming: Batch processing of multiple programs
  * Multitasking: Running Chrome, VS Code, and Spotify simultaneously

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

**Case 1: Development Environment on 8GB RAM**
- Scenario: Running Chrome + Docker + VS Code
- Problem breakdown:
  * Chrome with multiple tabs: ~2-4 GB RAM
  * Docker container: ~2-3 GB RAM
  * VS Code with extensions: ~1-2 GB RAM
  * Total needed: ~8 GB (entire RAM)
- What happens:
  * Like trying to fit items in a full backpack
  * When RAM fills up:
    - OS starts using hard disk as extra memory
    - Similar to storing overflow items in a locker
    - But accessing locker (disk) is much slower than backpack (RAM)
- Impact:
  * System becomes sluggish
  * Apps take longer to respond
  * Mouse movements may stutter
- Solution:
  * Close unused Chrome tabs
  * Stop unused Docker containers
  * Limit VS Code extensions
  * Upgrade RAM to 16GB

**Case 2: Video Conferencing with Screen Share**
- Scenario: Microsoft Teams on dual-core Intel i5
- What's happening:
  * Screen recording needs to:
    - Capture screen (CPU task)
    - Compress video (CPU task)
    - Send data over network
    - Handle meeting audio/video
    - Show other participants
  * Like a chef trying to cook 5 dishes with 2 hands
- Problems:
  * CPU gets overwhelmed
  * Frame rate drops
  * Audio may stutter
  * App might freeze
- Solutions:
  * Close background applications
  * Lower video quality
  * Disable video effects
  * Use CPU with more cores

**Common Bottlenecks Explained:**
1. Memory Bus (Data Highway)
   * Like a road between CPU and RAM
   * More lanes (width) = more data per trip
   * Traffic jams cause slowdown

2. CPU Usage (Processing Power)
   * Like workers in a factory
   * More cores = more workers
   * Too many tasks = delayed work

3. Cache Size (Quick Access Storage)
   * Like a desk vs storage room
   * Frequently used items on desk (cache)
   * Limited desk space = more trips to storage


