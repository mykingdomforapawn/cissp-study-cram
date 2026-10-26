Memory holds the instructions and data the processor works on, and it comes in several kinds that differ in speed, cost, volatility, and whether they can be written. Security concerns follow from what memory holds and who else can reach it. Enforcing separation between processes is covered in [[Security Capabilities of Information Systems]].

## ROM

**Read-only memory (ROM)** is **nonvolatile**, so it keeps its contents without power, and is written either at manufacture or only under special conditions. It typically holds firmware (see [[Firmware]]).

| Type | Writable how |
|---|---|
| **ROM** (mask ROM) | Contents fixed at manufacture and cannot be changed |
| **PROM** (programmable ROM) | Written **once** after manufacture, then permanent |
| **EPROM** (erasable PROM) | Erased by exposing the chip to **ultraviolet light** (UVEPROM), then rewritten |
| **EEPROM** (electrically erasable PROM) | Erased and rewritten **electrically**, in place, without removing the chip |
| **Flash memory** | A form of EEPROM erased and written in **blocks**, so it is fast and dense. It is used in SSDs, USB drives, and memory cards |

Fixed ROM is tamper-proof but cannot be patched, while rewritable types can be updated and so can also be altered by an attacker.

## RAM

**Random access memory (RAM)** is the working memory. It is **volatile**: its contents are lost when power is removed.

| | Dynamic RAM (DRAM) | Static RAM (SRAM) |
|---|---|---|
| **Storage cell** | A capacitor, which leaks charge | A flip-flop circuit, which holds its state while powered |
| **Refresh** | Must be refreshed constantly | No refresh needed |
| **Speed and cost** | Slower and cheaper, and denser | Faster and more expensive |
| **Typical use** | Main system memory | **Cache** memory and CPU registers |

- **Real memory** is the physical RAM installed. The main memory is DRAM.
- **Cache memory** is a small, fast layer (SRAM) between the CPU and main memory holding frequently used data, to hide the speed gap.
- **Registers** are the processor's own tiny, very fast storage locations, built into the CPU. The arithmetic logic unit works directly on them. Some are general purpose, and others have special roles, such as the program counter (the next instruction) and the stack pointer.

Speed, cost, and scarcity fall in this order: registers, cache, main memory, secondary storage.

## Memory Addressing

The processor must be told where data is. The addressing mode describes how the instruction identifies the location.

| Mode | How the data is found |
|---|---|
| **Register addressing** | The data is in a CPU register, and the instruction names the register |
| **Immediate addressing** | The data is part of the instruction itself, with no lookup |
| **Direct addressing** | The instruction gives the actual memory address of the data |
| **Indirect addressing** | The instruction gives the address of a location that holds *another address*, which points to the data |
| **Base + offset addressing** | The address is a value in a base register plus an offset, so the location is relative to a starting point |

A **pointer** is a value that holds a memory address instead of the data itself. Indirect addressing follows a pointer: the instruction names the location holding the pointer, and the processor reads that address and then fetches the data from it. Programs use pointers for arrays, buffers, and linked structures. Pointer mistakes cause real flaws: a **null pointer** (pointing at nothing) crashes the program, a **dangling pointer** refers to memory already freed, and a pointer moved past the end of a buffer reads or overwrites memory that belongs to something else.

Base + offset matters for security because the base register marks the start of a process's allocated range and the offset is checked against its limit. That is how **memory bounds** are enforced (see [[Techniques for Ensuring CIA]]): a process that tries to address beyond its limit is stopped.

## Secondary Memory and Virtual Memory

**Secondary memory** is nonvolatile bulk storage, such as hard disks and SSDs, that the processor cannot address directly (see [[Data Storage Devices]]). **Virtual memory** uses part of it, a **page file** or **swap space**, as an extension of RAM. The OS moves inactive pages out to disk, and the process sees a larger continuous address space than the physical RAM.

Virtual memory is a security concern because anything in memory, including keys, passwords, and decrypted documents, can be written to disk and can stay there after the process ends. The page file therefore needs the same protection as the data and should be encrypted or cleared on shutdown.

## Memory Security Issues

- **Data remanence.** Memory contents do not always vanish instantly when power is lost, and RAM can retain data for seconds to minutes, longer when chilled. A **cold boot attack** reads keys out of RAM shortly after the system is powered off or restarted.
- **Object reuse.** Memory released by one process and given to another may still hold the previous contents. The OS must clear it before reassignment so that no data leaks between processes.
- **Residual data in swap.** As above, paged-out memory may persist on disk.
- **Direct memory access (DMA).** Some interfaces, such as Thunderbolt and older FireWire, let peripherals read system memory without going through the CPU, so a malicious device can read RAM (including keys) directly. Controls include port disabling and IOMMU protection.
- **Unprotected data in use.** Data in RAM is normally unencrypted, so anyone who can read another process's memory can read it, which is why process isolation matters. Hardware features can encrypt memory or run sensitive code in a protected enclave (see [[Security Capabilities of Information Systems]]).
- **Memory errors in code.** Programs that write past the end of their buffers can corrupt memory or run attacker code. This is a software flaw, but memory protection is the hardware-assisted defense.

## Key Points

- **ROM family** goes from fixed to once-writable (PROM) to UV-erasable (EPROM) to electrically erasable (EEPROM) and block-erased flash. Rewritable means updatable and also alterable.
- **DRAM vs SRAM.** DRAM is cheap, dense, needs refresh, and serves as main memory. SRAM is fast, expensive, and serves as cache and registers.
- **A pointer holds an address**, not data. Indirect addressing follows one, and pointer errors lead to memory corruption.
- **Base + offset addressing** is what makes memory bounds enforceable.
- **Volatile does not mean instantly gone.** Remanence makes RAM contents recoverable briefly, which is why keys in memory can be attacked.
- **Cleared on reuse.** Memory must be cleared before a different process gets it, and swap space needs protection too.
