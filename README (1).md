# 🔗 SDN Link Failure Detection and Recovery
### Software Defined Networking | Mininet Project

![Mininet](https://img.shields.io/badge/Mininet-2.3.1-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square)
![OVS](https://img.shields.io/badge/OVS-OpenVSwitch-orange?style=flat-square)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

---

## 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Network Topology](#-network-topology)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Demo Commands](#-demo-commands)
- [Expected Output](#-expected-output)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Author](#-author)

---

## 📖 About the Project

This project demonstrates **Link Failure Detection and Recovery** in a Software Defined Network using **Mininet** and **Open vSwitch (OVS)**.

When a link (cable) between two switches fails:
- The failure is **detected** immediately
- Traffic is **rerouted** through alternate paths
- When the link is **restored**, full connectivity recovers automatically

> This project was built as part of an SDN lab assignment worth **10 marks**.

---

## 🌐 Network Topology

```
        h1                        h2
        |                          |
      s1 ──────────────────────── s2
      |  ╲                         |
      |   ╲ (backup diagonal)      |
      s4   ╲──────────── s3 ───────╯
      |                  |
      h4                 h3
```

| Component | Details |
|-----------|---------|
| Switches  | s1, s2, s3, s4 (OVS Kernel Switch) |
| Hosts     | h1 (10.0.0.1), h2 (10.0.0.2), h3 (10.0.0.3), h4 (10.0.0.4) |
| Ring Links | s1↔s2, s2↔s3, s3↔s4, s4↔s1 — 10Mbps, 5ms delay |
| Backup Link | s1↔s3 — 5Mbps, 10ms delay |

---

## ✨ Features

- ✅ Ring topology with 4 switches and 4 hosts
- ✅ Link failure simulation using Mininet CLI
- ✅ Automatic traffic rerouting on link failure
- ✅ Link recovery detection and restoration
- ✅ Flow rule management with OVS
- ✅ Bandwidth and delay configured on all links

---

## 🛠 Prerequisites

- Ubuntu 20.04 (or any Linux system)
- Python 3.8+
- Mininet 2.3+
- Open vSwitch (OVS)

---

## ⚙️ Installation

**Step 1 — Update your system:**
```bash
sudo apt-get update
```

**Step 2 — Install Mininet:**
```bash
sudo apt-get install mininet -y
```

**Step 3 — Verify installation:**
```bash
sudo mn --version
```
You should see: `2.3.1b4`

**Step 4 — Clean up any previous Mininet sessions:**
```bash
sudo mn -c
```

---

## 🚀 How to Run

**Step 1 — Clone this repository:**
```bash
git clone https://github.com/sanskarghenappagol/sdn-link-failure.git
cd sdn-link-failure
```

**Step 2 — Start Mininet with the custom topology:**
```bash
sudo mn --topo linear,4 --switch ovsk,failMode=standalone --controller=none --mac
```

**Step 3 — Add flow rules to all switches (inside Mininet CLI):**
```
mininet> sh ovs-ofctl add-flow s1 action=flood
mininet> sh ovs-ofctl add-flow s2 action=flood
mininet> sh ovs-ofctl add-flow s3 action=flood
mininet> sh ovs-ofctl add-flow s4 action=flood
```

---

## 🎮 Demo Commands

Run these commands inside the Mininet CLI to demonstrate link failure and recovery:

### 1️⃣ Check network structure
```
mininet> net
mininet> nodes
```

<img width="601" height="221" alt="one" src="https://github.com/user-attachments/assets/720d3ff2-74ca-45dc-b4e4-b377d8b7817a" />


### 2️⃣ Test baseline connectivity (all links UP)
```
mininet> pingall
```
Expected: `0% dropped (12/12 received)`

<img width="509" height="131" alt="two" src="https://github.com/user-attachments/assets/d6455c3c-0cc4-4ec5-8f90-8d7977d224d9" />


### 3️⃣ Simulate link failure
```
mininet> link s1 s2 down
```

### 4️⃣ Test after failure (traffic reroutes)
```
mininet> pingall
```
Expected: partial drops — h1 affected, others reroute

<img width="456" height="145" alt="three" src="https://github.com/user-attachments/assets/292ce3e9-e600-4704-bd4f-d0366c2faac3" />


### 5️⃣ Check flow rules on switches
```
mininet> sh ovs-ofctl dump-flows s1
mininet> sh ovs-ofctl dump-flows s2
```

<img width="922" height="95" alt="four" src="https://github.com/user-attachments/assets/1f6d2f03-e076-40d2-abf1-87e9341d877c" />


### 6️⃣ Restore the link (recovery)
```
mininet> link s1 s2 up
```

### 7️⃣ Test after recovery (full connectivity)
```
mininet> pingall
```
Expected: `0% dropped (12/12 received)`

<img width="434" height="149" alt="five" src="https://github.com/user-attachments/assets/3cb27f8f-008a-4273-a4b5-94bda3a94601" />


### 8️⃣ Exit
```
mininet> exit
```

<img width="466" height="197" alt="six" src="https://github.com/user-attachments/assets/89ea3d03-5e58-4e70-a448-d6df17b218e6" />


---

## 📊 Expected Output

```
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4
h2 -> h1 h3 h4
h3 -> h1 h2 h4
h4 -> h1 h2 h3
*** Results: 0% dropped (12/12 received)

mininet> link s1 s2 down

mininet> pingall
*** Ping: testing ping reachability
h1 -> X  X  X
h2 -> X  h3 h4
h3 -> X  h2 h4
h4 -> X  h2 h3
*** Results: 50% dropped (6/12 received)

mininet> link s1 s2 up

mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4
h2 -> h1 h3 h4
h3 -> h1 h2 h4
h4 -> h1 h2 h3
*** Results: 0% dropped (12/12 received)
```

---

## 📁 Project Structure

```
sdn-link-failure/
│
├── topo.py          # Custom ring topology definition
├── README.md        # Project documentation (this file)
```

---

## 🔍 How It Works

### Normal Operation
All switches have flood flow rules installed. Packets from any host reach all other hosts through the ring.

### Link Failure
When `link s1 s2 down` is run:
- The physical port between s1 and s2 is brought down
- OVS detects the port status change
- Packets destined via s1↔s2 are dropped
- Other hosts reroute through remaining links

### Recovery
When `link s1 s2 up` is run:
- The port is restored
- OVS detects the link is back
- Flood rules propagate packets through all paths again
- Full connectivity is restored — 0% packet loss

---

## 👤 Author

**Sanskar**
- GitHub: [@sanskarghenappagol](https://github.com/YOUR_USERNAME)
- SDN Lab Project — 2026

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
