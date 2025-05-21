# Introduction to Computer Systems and Operating Systems

## Table of Contents

- [Introduction to Computer Systems and Operating Systems](#introduction-to-computer-systems-and-operating-systems)
  - [Table of Contents](#table-of-contents)
  - [1. Computer System Fundamentals](#1-computer-system-fundamentals)
    - [Basic Definition](#basic-definition)
    - [Core Components](#core-components)
  - [2. Detailed Component Analysis](#2-detailed-component-analysis)
    - [2.1 CPU (Central Processing Unit)](#21-cpu-central-processing-unit)
    - [2.2 Memory Hierarchy](#22-memory-hierarchy)
    - [Memory Characteristics Comparison](#memory-characteristics-comparison)
  - [3. Operating System Concepts](#3-operating-system-concepts)
    - [3.1 Computer Booting Process](#31-computer-booting-process)
      - [Bootstrap Program](#bootstrap-program)
      - [Boot Sequence](#boot-sequence)
    - [3.2 Threads and Concurrency](#32-threads-and-concurrency)
    - [3.3 Difference between Concurrent and Parallel](#33-difference-between-concurrent-and-parallel)
    - [3.4 Multithreading](#34-multithreading)
    - [Core Functions of the Operating System](#core-functions-of-the-operating-system)
    - [Hotel Management Analogy](#hotel-management-analogy)



## 1. Computer System Fundamentals

### Basic Definition

- A computer system is an integrated combination of hardware and software components
- Designed to process, store, and handle information
- Works through coordinated interaction between components


### Core Components

1. **Hardware**
    - CPU (Central Processing Unit)
    - Memory units
    - Input/Output devices
    - Storage devices
2. **Software**
    - Operating System
    - Application programs
    - System utilities

## 2. Detailed Component Analysis

### 2.1 CPU (Central Processing Unit)

- **Main Functions**:
    - Executes program instructions
    - Performs data processing
    - Controls system operations
- **Key Components**:
    - Arithmetic Logic Unit (ALU)
        * The part of the CPU that actually executes instructions from CPU
    - Control Unit
        * Fetches program instructions from memory and converts them into control signals that tells CPU's subcomponents (ALU, registers) what to do and when to do
        * Uses system clock to determine the sequence of instructions to execute
        * Overall, it is responsible for managing data flow within the CPU and between the CPU and other hardware components
    - Registers (fastest memory)


### 2.2 Memory Hierarchy

1. **Registers**
    - Fastest access (~1 nanosecond)
    - Smallest storage capacity
    - Located within CPU
2. **Cache Memory**
    - Cache is a small, high-speed memory located close to or inside the CPU, used to temporarily store frequently accessed data and instructions.
    - **Types of Cache:**
        - **L1 Cache (Level 1):**
            * Smallest and fastest cache (typically 32KB–64KB per core)
            * Located directly on the CPU core
            * Split into instruction cache (I-cache) and data cache (D-cache)
            * Provides the quickest access to data for the CPU
        - **L2 Cache (Level 2):**
            * Larger than L1 (typically 256KB–512KB per core)
            * Slightly slower than L1 but still very fast
            * Can be dedicated per core or shared by a few cores
            * Acts as a backup for L1 cache, storing data not found in L1
        - **L3 Cache (Level 3):**
            * Largest and slowest among the three (several MB, e.g., 4MB–32MB)
            * Usually shared among all CPU cores on the processor
            * Helps reduce bottlenecks when multiple cores need access to the same data
            * Acts as a last-level cache before accessing main memory (RAM)

    - L1/L2 Cache: ~1-10 nanoseconds
    - L3 Cache: ~10-100 nanoseconds
3. **Main Memory (RAM)**
    - Access time: ~100-1000 nanoseconds
    - Volatile storage
    - Direct CPU access
4. **Secondary Storage**
    - SSDs: ~10-200 microseconds
    - Hard Drives: Slower but larger capacity
    - Non-volatile storage
### Memory Characteristics Comparison

| Type | Speed | Size | Cost/Byte | Volatility |
| :-- | :-- | :-- | :-- | :-- |
| Registers | Fastest | Smallest | Highest | Volatile |
| Cache | Very Fast | Small | Very High | Volatile |
| RAM | Fast | Medium | Moderate | Volatile |
| SSD | Slow | Large | Low | Non-volatile |
| HDD | Slowest | Largest | Lowest | Non-volatile |

## 3. Operating System Concepts

### 3.1 Computer Booting Process

#### Bootstrap Program

- **Definition**: Special program that initializes and starts the computer system
- **Location**: Initially invoked from firmware (ROM/EEPROM), with main bootloader components typically located in boot sectors of storage devices (MBR or ESP)
- **Functions**:
    - Performs basic hardware diagnostics
    - Initializes system components and registers
    - Loads the operating system kernel into memory
    - Transfers control to the OS


#### Boot Sequence

1. **Power-On (POST - Power-On Self-Test)**
    - User presses power button
    - CPU starts executing instructions from a hardwired memory address:
        * This address (usually 0xFFFF0 in x86 systems) is physically wired to a ROM chip
        * The ROM chip contains the firmware (BIOS/UEFI)
        * When CPU reads from this address, it's actually reading from the ROM chip
        * First instruction is usually a jump instruction that directs CPU to firmware's main code
2. **Firmware (BIOS/UEFI) Stage**
    - Firmware performs POST:
        * Tests critical hardware components
        * Checks CPU, memory, and basic hardware
        * If tests fail, system beeps or displays error codes
    - Identifies boot devices according to priority
    - Locates boot sector (MBR) or EFI System Partition
3. **Bootstrap/Bootloader Stage**
    - For BIOS systems:
        * Reads Master Boot Record
        * Executes bootloader
    - For UEFI systems:
        * Reads EFI System Partition
        * Executes bootloader
    - Bootloader (GRUB/NTLDR/Windows Boot Manager):
        * Locates OS kernel
        * Loads kernel into RAM
        * Transfers control to kernel
4. **Operating System Stage**
    - Kernel initialization:
        * Takes control from bootloader
        * Initializes system components
        * Sets up memory management
        * Loads essential drivers

    - System Initialization:
        * Kernel starts the first process (init/systemd in Linux, smss.exe in Windows)
        * This process becomes the parent of all other system processes
        * Starts essential system services in sequence:
            - File system services
            - Network services
            - Device drivers
            - System daemons/background services

    - User Space Initialization:
        * Starts user-space initialization process
        * Loads user environment settings
        * Initializes graphical subsystem:
            - Graphics drivers
            - Window system (X.org/Wayland in Linux, Windows GUI)
            - Desktop environment
        * Sets up user interface components

5. **Login Screen**
    - Display manager starts
    - Login interface appears
    - User authentication begins
    - Desktop environment loads after successful login

### 3.2 Threads and Concurrency

- *Threads*
    - **Definition**: Smallest unit of execution within a process
- *Concurrency*
    - **Definition**: Multiple computations happening within the same time period (not necessarily at the exact same time)
    - **Types**:
        * **Pseudo-parallelism**: CPU rapidly switches between tasks
        * **True parallelism**: Multiple tasks execute simultaneously on different processors


### 3.3 Difference between Concurrent and Parallel

- **Concurrent**: Tasks appear to run simultaneously but actually take turns on CPU
- **Parallel**: Tasks truly run simultaneously on multiple processors
- Example:
    * Concurrent: One chef juggling multiple dishes by switching between them
    * Parallel: Multiple chefs each working on different dishes simultaneously


### 3.4 Multithreading

- **Definition**: A programming concept where a process can have multiple threads running concurrently
- **Real-world Analogy**:
    * Process = Restaurant
    * Threads = Chefs working in the restaurant
    * Multithreading = Multiple chefs working in the same kitchen
        - Sharing same resources (kitchen equipment, ingredients)
        - Working independently but coordinated
        - Can communicate easily with each other
- **Key Characteristics**:
    * All threads share same process resources (like chefs sharing kitchen)
    * Each thread has its own:
        - Program counter (recipe step they're on)
        - Stack (personal workspace)
        - Registers (personal notes/memory)
    * Threads can communicate easily (like chefs talking to each other)


### Core Functions of the Operating System

1. Resource Management
    - CPU scheduling
    - Memory allocation
    - I/O device control
2. User Interface
    - Command-line interface
    - Graphical user interface
    - System calls
3. Process Management
    - Process creation and termination
    - Process scheduling
    - Inter-process communication

### Hotel Management Analogy

- **System = Hotel Building**
    - Physical infrastructure represents hardware
    - Management systems represent operating system
- **Processes = Hotel Guests**
    - Resources allocation similar to room assignments
    - Different priority levels like VIP guests
- **OS Functions = Hotel Staff**
    - Reception → Process management
    - Housekeeping → Memory management
    - Room service → Resource allocation




