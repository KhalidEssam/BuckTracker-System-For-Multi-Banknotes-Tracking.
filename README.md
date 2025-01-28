
# BuckTracker: Multi Banknote Tracking System

## Description
BuckTracker is an AI-powered banknote tracking system designed to securely track money transactions and prevent theft. The system utilizes Optical Character Recognition (OCR) and Convolutional Neural Networks (CNNs) to scan banknotes, extract serial numbers, and detect currency denominations. It also integrates GPS location tracking to record where each banknote was scanned, providing a traceable record of cash transactions.

This project was published at the IMSA Conference, demonstrating a significant improvement over previous models with an accuracy of 92% in banknote recognition.

## Features
**Real-Time Banknote Scanning:** Detects and extracts serial numbers from cash using OCR.

**Multi-Currency Recognition:** Supports USD, GBP, and Euro banknotes.

**GPS-Based Tracking:** Logs the location where each banknote was last scanned.

**Secure Transactions:** Uses hashed tables to store transaction data securely.

**Improved OCR Accuracy:** Achieves higher accuracy than previous approaches using advanced preprocessing techniques.

## Technology Stack

**Computer Vision:** OpenCV for image preprocessing.

**OCR Engine:** Tesseract OCR for serial number recognition.

**Deep Learning:** CNN-based text recognition.

**Security:** Hash tables for transaction storage.

**Hardware Integration:** Mobile camera for real-time scanning.

## How It Works
**User scans a banknote** using their mobile camera.
<img src="https://github.com/Abdullahelbarrany/BuckTracker-Multi-Banknote-Tracking-System/blob/main/sxreenshots/m1%20(4).png?raw=true"  align="center" width="300" height="600">


**Preprocessing is applied** (grayscale conversion, noise reduction, and image segmentation).

**OCR extracts the serial number** and determines the currency type.
<img src="https://github.com/Abdullahelbarrany/BuckTracker-Multi-Banknote-Tracking-System/blob/main/sxreenshots/Screenshot%202022-09-22%20234214.png?raw=true"  align="center" width="300" height="600">


**GPS location is recorded** along with the scanned banknote.

A **hashed transaction** is created storing:

    Serial Number
    Timestamp
    Old and New Owner
    GPS Location
    Unique Transaction ID

**All transactions are securely logged**, allowing banknotes to be traced if stolen.

## Citation
This project was published at the **IMSA Conference**. Please cite our paper if you use this system in your research.
```sql
@inproceedings{inproceedings,
author = {Elbarrany, Abdullah and Mosallam, Khaled and Atia, Ayman},
year = {2023},
month = {07},
pages = {406-411},
title = {BuckTracker: System For Multi Banknotes Tracking},
doi = {10.1109/IMSA58542.2023.10217421}
}
```
## Contributors
**Abdullah Magdy Elbarrany** (Faculty of Computer Science, MSA University)

**Khaled Mosallam** (Faculty of Computer Science, MSA University)

**Ayman Atia** (HCI-LAB, Faculty of Computers and Artificial Intelligence, Helwan University)
