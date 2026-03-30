# RF Gain Controlled Wi-Fi Interference Using HackRF One

## Overview

This project investigates the effect of controlled RF noise on Wi-Fi performance using Software Defined Radio (SDR). A HackRF One device is used to generate band-limited Gaussian noise to analyze signal degradation and throughput reduction.

The project focuses on:

- RF interference analysis
- Signal-to-noise ratio (SNR) estimation
- Throughput degradation measurement
- GNU Radio based noise generation

---

## Hardware Used

- HackRF One SDR
- 2.4 GHz Antenna
- Wi-Fi Router
- Client Device
- Shielded Environment

---

## Software Used

- GNU Radio
- Python
- iperf3
- Matplotlib

---

## Methodology

1. Establish Wi-Fi baseline connection
2. Configure GNU Radio receiver
3. Generate Gaussian noise using HackRF
4. Vary RF gain
5. Measure throughput using iperf3
6. Estimate SNR
7. Plot results

---

## Results

- Throughput decreases with increasing RF noise
- SNR reduces significantly with gain increase
- Wi-Fi performance degrades under interference

---

## Features

- Controlled RF noise generation
- SNR estimation
- Throughput vs SNR analysis
- GNU Radio based implementation

---

## Applications

- RF interference analysis
- Wireless performance testing
- SDR experimentation
- Communication system analysis

---

## Future Work

- Adaptive interference generation
- Multi-band analysis
- Modulation detection
- Real-time visualization

---

## Author

Shreyansh Khandelwal  
Electronics and Communication Engineering  
