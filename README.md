# Impact of RACH Jamming on Network Access and Energy Saving

**Abstract:**

The 5G New Radio (NR) standard relies on the Random Access Channel (RACH) to establish user equipment (UE) connections, synchronize timing, and trigger gNB wake-up in energy-saving modes. However, the contention-based nature of RACH makes it vulnerable to targeted jamming attacks. This paper investigates the impact of RACH jamming on network access reliability and gNB energy efficiency, with a focus on the Msg1 and Msg3 stages. This study develops analytical models to quantify how attack parameters, such as transmit power and timing, affect key performance indicators: Msg1 success rate, Msg3 success rate, and gNB energy consumption. To validate these models, this research builds a standalone 5G testbed using OpenAirInterface (OAI), a USRP B210, and a commercial UE. By modifying OAI nrUE, this study implements a protocol-aware attacker capable of transmitting Msg1 or Msg3 at specific intervals. The gNB is enhanced with a sleep and wake-up mechanism to evaluate the effect of wakeup signal attacks. Experimental results show that Msg1 and Msg3 jamming significantly reduce UE access success, while repeated Msg1 transmissions prevent the gNB from remaining in sleep, negating the energy-saving effect. The findings demonstrate that RACH jamming compromises both network access reliability and energy efficiency in 5G networks, highlighting the importance of strengthening RACH protection.

**Problem Statement:**
- Existing RACH jamming studies focus on implementation, not mathematical modeling.
- No predictive framework exist to generally evaluate the impact of attacker parameters.

**Contribution:**
- Proposed first analytical models to investigate impact of RACH jamming on network access and energy saving.
- Experimental validation using an open-source 5G testbed with overthe-air (OTA) setup.

**System Architecture:**

<img width="1245" height="576" alt="image" src="https://github.com/user-attachments/assets/0e98ac1a-f05e-43a0-ab2d-b2b69a94d52b" />

<!--
```mermaid
flowchart TD
    A("`**Basestation:**
    -----------
    *N* - preamble ID
    *P_noise* - threshold
    *α* - noise threshold update factor
    *delta* - Msg1 threshold`")
    B["`**UE (M=1):**
    -------
    *P_UE* - msg1 power`"]
    C[["`**Attacker:**
    ---------
    *O* - number of msg1 attacked
    *P_attacker* - msg1 power
    *j* - time early start
    *T_a* - attack period`"]]
    B--A
    C--A
```
-->

**Repository Structure:**
```
wilfrid-prach-attack-analysis
├── docs            : Notes for the thesis development, including installation guide, user manual, etc
├── attacker        : source code for attacker
├── gnb             : source code for gnb
├── dataset         : CSV files containing dataset from experiment
├── old-files       : Old files for thesis development
├── code-review.md  : Meeting minutes of code review
```

**User Manual and Documentation:**

You can read user manual and other documents for this source and thesis in `docs`

**Download the Experiment Figures:**

You can download the experiment result figures in the simulation-guide.ipynb Jupyter Notebook inside `docs/simulation-guide.ipynb`
