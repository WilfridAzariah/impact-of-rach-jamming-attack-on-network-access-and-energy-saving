# Thesis (Test of PRACH Attacker for Basic Energy Saving Model)

###### tags: `2025`


**Goal:**
- [x] [Test PRACH Attacker for Basic Msg1 Model]()

**References:**
- [OAI 5G NR SA tutorial with OAI nrUE](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/NR_SA_Tutorial_OAI_nrUE.md?ref_type=heads)
- [OAI UE + USRP B210 Installation Guide](https://hackmd.io/@zhongxin/BJSPWUy90)
- [Attacker guide for Wilfrid paper](https://ntust-bmwlab.notion.site/Attacker-guide-for-Wilfrid-paper-12d1009831438064b6afcf322b4fa252)
- [MTK UE Guide](https://github.com/bmw-ece-ntust/o-ran-docs/blob/2022-MS-Summer-OAI/UE/MTK%20UE/MTK%20UE%20Guide.md)

**Table of Contents:**
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 0. Summary

1. Moabc

## 1. PRACH Attacker for Basic Energy Saving Model

```mermaid
flowchart TD
    A((nr-softmodem)) --> B["//load configurations"]
    B --> C["start_RU_proc()
    //create ru_thread"]
    C --> D["init_gNB_Tpool()
    //create L1_rx_thread
    //and L1_tx_thread"]
    D --> E[...]
```

```mermaid
flowchart TD
    A[...] --> B["term_gNB_Tpool()
    //destroy L1_rx_thread
    //and L1_tx_thread"]
    B --> C["kill_NR_RU_proc()
    //destroy ru_thread"]
    C --> D((end))
```

```mermaid
flowchart TD
    A(("stop_modem()")) --> B["term_gNB_Tpool()
    //destroy L1_rx_thread
    //and L1_tx_thread"]
    B --> C["kill_NR_RU_proc()
    //destroy ru_thread"]
    C --> D((end))
```

```mermaid
flowchart TD
    A(("start_modem()")) --> B["//load configurations"]
    B --> C["start_RU_proc()
    //create ru_thread"]
    C --> D["init_gNB_Tpool()
    //create L1_rx_thread
    //and L1_tx_thread"]
    D --> E((end))
```

```mermaid
flowchart TD
    A(("L1_nr_prach_
    procedures()")) --> B["//check if this
    //is PRACH slot"]
    B --> C["rx_nr_prach()
    //receive Msg1 with
    //the max energy"]
    C --> D{"preamble_id == 1
    && gnb_mode == 1"}
    D --> |yes| E["wus_detected = 1"]
    E --> F["//estimate PRACH noise
    //for next slot"]
    F --> G((return))
    D --> |no| H["//process PRACH
    //as usual"]
    H --> F
```

```mermaid
flowchart TD
    A(("gnb_mode_
    thread()")) --> B{"gnb_mode == ?"}
    B --> |"1 (sleep)"| C{"wus_detected == 1"}
    C --> |yes| D["wus_detected == 0"]
    D --> E["//change gNB state
    //to 2 (active)"]
    E --> F["//do nothing"]
    F --> B
    C --> |no| F
    B --> |"2 (active)"| G["sleep
    (inactivity_timer)"]
    G --> H["//change gNB state
    //to 1 (sleep)"]
    H --> B
```
