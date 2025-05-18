# Introduction to Computer Systems and Operating Systems

## Overview
This document contains fundamental concepts of computer systems and operating systems covered in the introductory class.

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
    * The part of the CPU that actually executes intructions from CPU
  - Control Unit
    * Fetches program instructions from memory and them into control signals that tells CPU's
    subcomponents (ALU, registers) what to do and when to do 
    * Uses system clock to determine the sequence of intructions to execute 
    * Overall, it is responsible for managing data flow within the CPU and between the CPU and other hardware components
  - Registers (fastest memory)

### 2.2 Memory Hierarchy
1. **Registers**
   - Fastest access (~1 nanosecond)
   - Smallest storage capacity
   - Located within CPU

2. **Cache Memory**
   - L1/L2 Cache: ~1-10 nanoseconds
   - L3 Cache: ~10-100 nanoseconds
   - Bridges speed gap between CPU and RAM

3. **Main Memory (RAM)**
   - Access time: ~100-1000 nanoseconds
   - Volatile storage
   - Direct CPU access

4. **Secondary Storage**
   - SSDs: ~10-200 microseconds
   - Hard Drives: Slower but larger capacity
   - Non-volatile storage

## 3. Operating System Concepts

### Core Functions
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

## 4. Key Principles of Memory Organization

### Hierarchy Characteristics
1. **Speed vs Capacity**
   - Faster memory = Smaller capacity
   - Slower memory = Larger capacity

2. **Cost Implications**
   - Faster memory technologies cost more
   - Trade-off between performance and cost

### Access Patterns
- Temporal locality
- Spatial locality
- Cache hit/miss concepts

## Summary
Understanding these fundamental concepts provides the foundation for:
- Advanced operating system concepts
- System architecture
- Resource management
- Process scheduling
- Memory management

*Note: This document serves as a reference for basic concepts in computer systems and operating systems.*