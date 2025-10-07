# Integration Guide for RACH Attacker and Other Related Components

**References:**
- [OAI 5G NR SA tutorial with OAI nrUE](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/NR_SA_Tutorial_OAI_nrUE.md?ref_type=heads)
- [Attacker guide for Wilfrid paper](https://ntust-bmwlab.notion.site/Attacker-guide-for-Wilfrid-paper-12d1009831438064b6afcf322b4fa252)
- [MTK UE Guide](https://github.com/bmw-ece-ntust/o-ran-docs/blob/2022-MS-Summer-OAI/UE/MTK%20UE/MTK%20UE%20Guide.md)

**Table of Contents:**
- [Integration Guide for RACH Attacker and Other Related Components](#integration-guide-for-rach-attacker-and-other-related-components)
  * [1. System Architecture](#1-system-architecture)
    + [1.1. Msg1 Attack on Network Access Message Sequence Chart](#11-msg1-attack-on-network-access-message-sequence-chart)
    + [1.2. Msg3 Attack on Network Access Message Sequence Chart](#12-msg3-attack-on-network-access-message-sequence-chart)
    + [1.3. Msg1 or WUS Attack on Network Energy Saving Message Sequence Chart](#13-msg1-or-wus-attack-on-network-energy-saving-message-sequence-chart)
  * [2. Integration Guide](#2-integration-guide)
    + [2.1. IMPORTANT NOTE ABOUT WILFRID REPOSITORY](#21-important-note-about-wilfrid-repository)
    + [2.2. Run gNB Attacker and UE](#22-run-gnb-attacker-and-ue)
  * [3. Checking Data of Attack Result](#3-checking-data-of-attack-result)
    + [3.1. Msg1 Attack on Network Access](#31-msg1-attack-on-network-access)
    + [3.2. Msg3 Attack on Network Access](#32-msg3-attack-on-network-access)
    + [3.3. Msg1 Attack on Network Energy Saving](#33-msg1-attack-on-network-energy-saving)
  * [4. Experiment Result Variation](#4-experiment-result-variation)
    + [4.1. Msg1 Attack on Network Access](#41-msg1-attack-on-network-access)
    + [4.2. Msg3 Attack on Network Access](#42-msg3-attack-on-network-access)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 1. System Architecture

<img width="1355" height="758" alt="image" src="https://github.com/user-attachments/assets/73fe30a0-4dcc-4e5b-9ae3-763926387a48" />

### 1.1. Msg1 Attack on Network Access Message Sequence Chart

<img width="1315" height="642" alt="image" src="https://github.com/user-attachments/assets/f47b41db-587a-4345-9f1e-00286b7da98b" />

### 1.2. Msg3 Attack on Network Access Message Sequence Chart

<img width="1315" height="629" alt="image" src="https://github.com/user-attachments/assets/6220ebc4-8dad-42f5-90c7-d78895f12862" />

### 1.3. Msg1 or WUS Attack on Network Energy Saving Message Sequence Chart

<img width="1293" height="609" alt="image" src="https://github.com/user-attachments/assets/478273c4-6975-43d6-8a81-b07270ab5047" />

## 2. Integration Guide

### 2.1. IMPORTANT NOTE ABOUT WILFRID REPOSITORY

<b>My repo consist of 4 different components (2 attackers, 2 gNBs). Please pay attention to the directory of the component you want to run. The integration steps below are common to all components.</b>

```
wilfrid-prach-attack-analysis
├── attacker       : attacker code directory
    ├── msg1       : Msg1 attacker code
    ├── msg3       : Msg3 attacker code
├── gnb            : gNB code directory
    ├── regular    : regular OAI gNB code
    ├── msg3       : OAI gNB with NES feature (sleep) code
```

### 2.2. Run gNB Attacker and UE

<b>0. Be aware of the source code or config file edit for changing gNB or attacker parameters that you are currently using. Please see details in [User Manual](https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis/blob/master/docs/user-manual.md).</b>

<b>1. Run OAI gNB</b>

```shell=
cd gnb/regular/cmake_target/ran_build/build
#
# if you want to run the energy saving gNB please use the command below
# cd gnb/energySaving/cmake_target/ran_build/build
```
```shell=
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 -E --continuous-tx --log_config.PRACH_debug
#
# if you want to run the energy saving gNB please use the command below
# sudo ./nr-softmodem -O ../../../ci-scripts/conf_files/gnb.sa.band78.51prb.usrpb200.conf --gNBs.[0].min_rxtxtime 6 -E --continuous-tx --log_config.PRACH_debug
```
![image](https://github.com/user-attachments/assets/6650b2f5-90a0-4db5-a9bd-91a7ba9d81a4)

<b>2. Run Attacker</b>

```shell=
cd attacker/msg1/cmake_target/ran_build/build
#
# if you want to run the msg3 attacker please use the command below
# cd attacker/msg3/cmake_target/ran_build/build
```
```shell=
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --ssb 516 -E --ue-fo-compensation
#
# if you want to run the wus attacker for network energy saving please use the command below
# sudo ./nr-uesoftmodem -r 51 --numerology 1 --band 78 -C 3609120000 --ssb 234 -E --ue-fo-compensation
```
![image](https://github.com/user-attachments/assets/ec91cf07-b6c8-4070-927d-c75f945939fe)

<b>3. Run UE by switching off airplane mode</b>

```shell=
# you do not need to do this if you want to test the wus attacker
```
![image](https://github.com/user-attachments/assets/6703b62d-206b-4d91-97e8-0949ce5d468a)

## 3. Checking Data of Attack Result

### 3.1. Msg1 Attack on Network Access

<b>1. After you run gNB, if you do not run attacker, you turn off UE airplane mode to check noise power and UE msg1 power.</b>

```
[PHY]   prach_I0 = 17.0 dB
[NR_PHY]   [RAPROC] 635.19 Initiating RA procedure with preamble 12, energy 52.7 dB (I0 173, thres 120), delay 0 start symbol 2 freq index 0
```
<img width="1365" height="764" alt="image" src="https://github.com/user-attachments/assets/e0ebd4ce-31e1-4260-a7e6-ea2b1e45cebb" />

<b>2. To check if gNB successfully receive Msg1 Attacker preamble, run gNB and attacker without turn off UE airplane mode.</b>

```
[NR_PHY]   [RAPROC] 318.19 Initiating RA procedure with preamble 1, energy 45.7 dB (I0 304, thres 120), delay 0 start symbol 2 freq index 0
```
<img width="1371" height="769" alt="image" src="https://github.com/user-attachments/assets/d35299f8-9131-4634-a60b-5664f8345260" />

<b>3. To check if Msg1 Attacker successfully jam UE Msg1, turn off UE airplane mode while running gNB and attacker.</b>

```
[PHY]   prach_I0 = 49.0 dB
```
<img width="1369" height="766" alt="image" src="https://github.com/user-attachments/assets/06958200-8d3e-4978-8fdc-8b9d53f5a6df" />

<b>4. Based on the example above, the input parameters of the model are:</b>

```shell=
# p_(noise)       = 17 dB
# p_(UE)          = 52.7 dB
# p_(attacker)    = 49 dB
# T_(a)           = 1
# beta            = 0.12
# delta           = 12 dB
```

### 3.2. Msg3 Attack on Network Access

<b>1. After you run gNB, if you do not run attacker, you turn off UE airplane mode to check UE msg3 power.</b>

```
80.17: Estimated SNR for PUSCH is = 20.500000 dB (ulsch_power 45.600000, noise 25.100000) delay 2
```
<img width="1368" height="767" alt="image" src="https://github.com/user-attachments/assets/ea9317a8-b523-4539-b9a9-a02271c591d7" />

<b>2. To check if Msg3 Attacker successfully jam UE Msg3, turn off UE airplane mode while running gNB and attacker.</b>

```
778.17: Estimated SNR for PUSCH is = 39.600000 dB (ulsch_power 64.700000, noise 25.100000) delay 3
```
<img width="1370" height="770" alt="image" src="https://github.com/user-attachments/assets/06821231-ce97-46d3-9f50-8e4e384873ea" />

<b>3. Based on the example above, the input parameters of the model are:</b>

```shell=
# p_(RX,UE)          = 45.6 dB
# p_(RX,attacker)    = 64.7 dB
# d_(attacker)       = check gNB to attacker physical distance
```

### 3.3. Msg1 Attack on Network Energy Saving

<b>1. After you run gNB, if you do not run attacker, you can check gNB sleep power.</b>

```
==========gNB operating in sleep==========
```
<img width="1371" height="759" alt="image" src="https://github.com/user-attachments/assets/b92afc51-9dfe-4eea-8617-8fc4d467989c" />

<b>2. To check if gNB successfully receive Msg1 Attacker WUS preamble and change to active, run gNB, wait a while, and run attacker.</b>

```
570.19 Received WUS preamble 1
```
<img width="1368" height="763" alt="image" src="https://github.com/user-attachments/assets/f23ae0b9-eaae-4bce-ae84-832f5b467564" />

```
==========gNB operating in active==========
```
<img width="1369" height="765" alt="image" src="https://github.com/user-attachments/assets/cb6cd52a-8854-49bb-96d1-d057d9fcc3fd" />

<b>3. To check if gNB return to sleep after being in active, turn off attacker while running gNB.</b>

```
[GNB_APP]   stopping nr-softmodem
```
<img width="1367" height="765" alt="image" src="https://github.com/user-attachments/assets/d30f612c-ab6a-4020-a030-fd2a659f4493" />

```
==========gNB operating in sleep==========
```
<img width="1365" height="764" alt="image" src="https://github.com/user-attachments/assets/988f2930-f70d-4dca-81f1-d1bf132790ae" />

<b>4. Based on the example above, the input parameters of the model are:</b>

```shell=
# p_(sleep)        = 514 mA * 110 V
#                  = 56 Watts
# p_(active)       = 643 mA * 110 V
#                  = 70 Watts
```

## 4. Experiment Result Variation

### 4.1. Msg1 Attack on Network Access

<b>1. To vary attacker period T_a, see Controlling Msg1 Attacker prach-ConfigurationIndex in [User Manual](https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis/blob/master/docs/user-manual.md#212-controlling-msg1-attacker-prach-configurationindex)</b>

```
int config_index = 149; ///// WILFRID - Hardcode prach_ConfigIndex /////
// if gNB index is 160
// T_a = 1 -> config_index = 160
// T_a = 2 -> config_index = 149
```
<img width="1466" height="723" alt="image" src="https://github.com/user-attachments/assets/983020ca-d715-4c20-92b0-94d5e23fdf42" />

<b>2. To vary gNB noise update factor beta, see Controlling gNB's noise threshold update factor in [User Manual](https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis/blob/master/docs/user-manual.md#512-controlling-gnbs-noise-threshold-update-factor)</b>

```
const int wilfrid_beta = 124; // beta = 0.12
                              ///// WILFRID - Msg1 beta /////
// beta = 0.12 -> wilfrid_beta = 124
// beta = 0.24 -> wilfrid_beta = 248
```
<img width="1485" height="729" alt="image" src="https://github.com/user-attachments/assets/221b7d35-388a-4968-bdf7-0fde6dd5d76c" />

<b>3. To vary gNB Msg1 detection margin delta, see Controlling gNB's Msg1 power detection threshold in [User Manual](https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis/blob/master/docs/user-manual.md#513-controlling-gnbs-msg1-power-detection-threshold)</b>

```
prach_dtx_threshold   = 120; ##### WILFRID - Msg1 delta #####
// delta = 12 -> prach_dtx_threshold   = 120
// delta = 24 -> prach_dtx_threshold   = 240
```
<img width="1489" height="722" alt="image" src="https://github.com/user-attachments/assets/39ca9ff5-916d-4840-82db-9cce1fc34813" />

### 4.2. Msg3 Attack on Network Access

<b>1. To vary attacker distance to gNB d_(attacker), physically move and measure the gNB to attacker distance</b>

<img width="1515" height="568" alt="image" src="https://github.com/user-attachments/assets/085ec5fd-ba1c-4119-9075-2fb8581684cf" />

<b>2. To vary UE Msg3 target power p_(RX,UE), see Controlling UE Msg1 & Msg3 Transmit Power in [User Manual](https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis/blob/master/docs/user-manual.md#411-controlling-ue-msg1--msg3-transmit-power)</b>

```
preambleReceivedTargetPower                               = -96; ##### WILFRID - Msg1 p_(UE) #####
// you need to test this value (preambleReceivedTargetPower) a few times to get what is the value of p_(RX,UE)
msg3_DeltaPreamble                                          = 1; ##### WILFRID - related to Msg3 p_(RX,UE) #####
// you need to test this value (preambleReceivedTargetPower) a few times to get what is the value of p_(RX,UE)
```
<img width="1494" height="639" alt="image" src="https://github.com/user-attachments/assets/498c63f4-38bd-4d73-b1c8-728754786b1e" />

