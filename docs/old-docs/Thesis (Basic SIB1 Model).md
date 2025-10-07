# Thesis (Basic SIB1 Model)

###### tags: `2025`

**Goal:**
- [x] Write Basic SIB1 Model for Analysis of PRACH Attack on Network Energy Saving

**References:**
- [A Power Consumption Model and Energy Saving Techniques for 5G-Advanced Base Stations](https://ieeexplore.ieee.org/document/10283643)

**Table of Contents:**
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 1. System Model

### 1.2. PRACH Msg3 Attack Overview

#### 1.2.1. Normal

```mermaid
sequenceDiagram
    gNB->>UE: [1] SSB/PBCH<br/>System Information
    Note over UE: Synchronization
    UE->>gNB: [2] Wake Up Signal<br/>Random Access Preamble (Msg1)
    gNB->>UE: [3] PDSCH<br/>System Information Block 1
    UE->>gNB: [4] PRACH<br/>Random Access Preamble (Msg1)
```

#### 1.2.2. Under Attack

```mermaid
sequenceDiagram
    gNB->>Attacker: [1] SSB/PBCH<br/>System Information
    Note over Attacker: Synchronization
    loop Repeat j times
        Attacker->>gNB: [2] Wake Up Signal<br/>Random Access Preamble (Msg1)
        gNB->>Attacker: [3] PDSCH<br/>System Information Block 1
    end
    gNB->>UE: [4] SSB/PBCH<br/>System Information
    Note over UE: Synchronization
    UE->>gNB: [5] Wake Up Signal<br/>Random Access Preamble (Msg1)
    gNB->>UE: [6] PDSCH<br/>System Information Block 1
    UE->>gNB: [7] PRACH<br/>Random Access Preamble (Msg1)
```
### 1.2. Actors


## 2. Basic Model

### 2.1. Model Parameters

#### 2.1.1. Assumptions or Constant Input Parameter
