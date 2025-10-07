# Installation Guide for RACH Attacker and Other Related Components

**References:**
- [OAI 5G NR SA tutorial with OAI nrUE](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/NR_SA_Tutorial_OAI_nrUE.md?ref_type=heads)
- [Attacker guide for Wilfrid paper](https://ntust-bmwlab.notion.site/Attacker-guide-for-Wilfrid-paper-12d1009831438064b6afcf322b4fa252)
- [MTK UE Guide](https://github.com/bmw-ece-ntust/o-ran-docs/blob/2022-MS-Summer-OAI/UE/MTK%20UE/MTK%20UE%20Guide.md)

**Table of Contents:**
- [Installation for RACH Attacker and Other Related Components](#installation-for-rach-attacker-and-other-related-components)
  * [1. HW and SW Specifications](#1-hw-and-sw-specifications)
    + [1.0. IMPORTANT NOTE ABOUT OAI VERSION](#10-important-note-about-oai-version)
    + [1.1. OAI gNB with USRP](#11-oai-gnb-with-usrp)
      - [1.1.1. Hardware](#111-hardware)
      - [1.1.2. Software](#112-software)
    + [1.2. OAI UE with USRP for attacker](#12-oai-ue-with-usrp-for-attacker)
      - [1.2.1. Hardware](#121-hardware)
      - [1.2.2. Hardware](#122-hardware)
  * [2. Installation Guide](#2-installation-guide)
    + [2.1. USRP Dependencies and Library](#21-usrp-dependencies-and-library)
    + [2.2. Download and Install Attacker or gNB](#22-download-and-install-attacker-or-gnb)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## 1. HW and SW Specifications

### 1.0. IMPORTANT NOTE ABOUT OAI VERSION

<b>Please note that I develop my source code based on OAI `2025.w11`. If you want to compare what I edit from OAI source code, please diff my code from original OAI `2025.w11`</b>

### 1.1. OAI gNB with USRP

#### 1.1.1. Hardware

| Item         | Info                                     |
| ------------ | ---------------------------------------- |
| CPU          | Intel(R) Core(TM) i7-7567U CPU @ 3.50GHz |
| Memory       | 8GB                                      |
| Disk         | 922GB                                    |
| Server Model | Intel Corporation NUC7i7BNH J31153-310   |

#### 1.1.2. Software

| Item       | Info                       |
| ---------- | -------------------------- |
| OS         | Ubuntu 22.04.4 LTS (jammy) |
| Kernel     | 6.8.0-52-generic           |
| OAI Commit | 82fb9fcc7c0c5576007fcdb0521e84809751d57e (HEAD, tag: 2025.w11)                           |

### 1.2. OAI UE with USRP for attacker

#### 1.2.1. Hardware

| Item         | Info                                     |
| ------------ | ---------------------------------------- |
| CPU          | Intel(R) Core(TM) i7-7567U CPU @ 3.50GHz |
| Memory       | 8GB                                      |
| Disk         | 922GB                                    |
| Server Model |                                          |

#### 1.2.2. Hardware

| Item       | Info                       |
| ---------- | -------------------------- |
| OS         | Ubuntu 22.04.4 LTS (jammy) |
| Kernel     | 6.8.0-52-generic           |
| OAI Commit | 82fb9fcc7c0c5576007fcdb0521e84809751d57e (HEAD, tag: 2025.w11)                           |

## 2. Installation Guide

### 2.1. USRP Dependencies and Library

<b>1. Install USRP B210 dependency</b>

```shell=
sudo apt install -y autoconf automake build-essential ccache cmake cpufrequtils doxygen ethtool g++ git inetutils-tools libboost-all-dev libncurses5 libncurses5-dev libusb-1.0-0 libusb-1.0-0-dev libusb-dev python3-dev python3-mako python3-numpy python3-requests python3-scipy python3-setuptools python3-ruamel.yaml
```

<b>2. Build UHD from source</b>

```shell=
git clone https://github.com/EttusResearch/uhd.git
cd uhd
git checkout v4.6.0.0
cd host
mkdir build
cd build
cmake ../
make -j $(nproc)
make test # This step is optional
sudo make install
sudo ldconfig
```

<b>3. Download FPGA Image</b>

```shell=
sudo uhd_images_downloader
```

<b>4. Install Gnuradio</b>

```shell=
sudo apt install gnuradio
```

<b>5. Check if the system can recognise B210 through USB</b>

```shell=
lsusb
```
![image](https://github.com/user-attachments/assets/62f7b806-ded9-47db-a60b-be403876438d)

<b>6. Test the device with uhd to see if it works</b>

```shell=
sudo uhd_find_devices
```
![image](https://github.com/user-attachments/assets/a7924ed6-28cf-4a0c-993a-6d680106dbc4)

### 2.2. Download and Install Attacker or gNB

<b>0. My repo consist of 4 different components (2 attackers, 2 gNBs). Please pay attention to the directory of the component you want to install. The installation steps below are common to all components.</b>

```
wilfrid-prach-attack-analysis
├── attacker          : attacker code directory
    ├── msg1          : Msg1 attacker code
    ├── msg3          : Msg3 attacker code
├── gnb               : gNB code directory
    ├── regular       : regular OAI gNB code
    ├── energySaving  : OAI gNB with NES feature (sleep) code
```

<b>1. Download My Repo from BMW Lab Github</b>

```shell=
git clone https://github.com/bmw-ece-ntust/wilfrid-prach-attack-analysis.git
cd wilfrid-prach-attack-analysis
```

<b>2. Change directory to the directory of component you want to build. In this example, I use Msg1 Attacker</b>

```shell=
# Change to msg1 attacker directory below
# ├── attacker
#    ├── msg1

cd attacker/msg1
# These are the other options
#cd attacker/msg3
#cd gnb/regular
#cd gnb/energySaving
```

<b>3. OAI Dependency</b>

```shell=
cd cmake_targets
# "sudo chmod +x build_oai" is optional
# sometimes, sudo do not get permission to execute build_oai, so will result in error of step 4
sudo chmod +x build_oai
sudo ./build_oai -I
```

![image](https://github.com/user-attachments/assets/8f365538-230e-4a47-a42b-9d4e2930d6f9)

<b>4. Install nrscope</b>

```shell=
sudo apt install -y libforms-dev libforms-bin
```

![image](https://github.com/user-attachments/assets/ea4316bb-e8e9-4aa3-a274-238768dfef43)

<b>5. Optional Reinstall yaml-cpp</b>

```shell=
# this is optional
# sometimes, the yaml-cpp library is broken, so will result in error of step 6
sudo apt update
sudo apt install --reinstall libyaml-cpp-dev
```

![image](https://github.com/user-attachments/assets/221673fa-ad55-4d89-9802-d0c45e66c127)

<b>6. Build attacker and gNB with USRP mode</b>

```shell=
sudo ./build_oai -w USRP --ninja --nrUE --gNB --build-lib "nrscope" -C
```

![image](https://github.com/user-attachments/assets/f5a08d78-d968-4c93-b1cc-72d2d69c3c21)

