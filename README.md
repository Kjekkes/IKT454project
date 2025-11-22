# Generative Semantic Communication: A Diffusion-Based Framework for 6G

This repository contains the implementation of a **Generative Semantic Communication** system. This framework addresses the challenges of next-generation 6G networks by shifting from traditional "bit-level" transmission to "semantic-level" transmission.

Instead of transmitting raw pixels, this system transmits compact **semantic segmentation maps**. The receiver then utilizes a **Denoising Diffusion Probabilistic Model (DDPM)**, guided by the received semantics, to hallucinate and reconstruct a photorealistic image.

> **Attribution:** This project is an implementation and adaptation of the paper **"Generative Semantic Communication: Diffusion Models for Semantic Image Transmission"** by Grassucci et al. (2023). It builds upon the [guided-diffusion](https://github.com/openai/guided-diffusion) codebase by OpenAI.

## 🚀 Key Features

* **Extreme Bandwidth Efficiency:** Transmits only sparse semantic class labels instead of RGB pixel data.
* **Channel Robustness:** capable of reconstructing recognizable images even in low Signal-to-Noise Ratio (SNR) environments (e.g., SNR = 10 dB).
* **Generative Reconstruction:** Uses SPADE-guided diffusion models to synthesize high-fidelity textures from semantic layouts.
* **Custom Training Logic:** Includes modified training loops with **Semantic Dropout** and **Noise Injection** to improve receiver robustness.

## 📂 System Architecture

The framework consists of three logical blocks:

1.  **Sender (Semantic Encoder):** Extracts and compresses the semantic map from the source image (Cityscapes dataset).
2.  **Channel (Simulation):** Simulates a noisy wireless channel (AWGN) by corrupting the semantic map.
3.  **Receiver (Generative Decoder):** A U-Net based Diffusion Model that acts as a decoder, using the corrupted map to guide the reverse diffusion process.

## 🛠️ Installation

### Prerequisites
* Linux or macOS
* Python 3.8+
* PyTorch 1.12+ (with CUDA support recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
