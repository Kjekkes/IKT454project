This repository contains the implementation of a **Generative Semantic Communication** system. This framework addresses the challenges of next-generation 6G networks by shifting from traditional "bit-level" transmission to "semantic-level" transmission.

> **Attribution:** This project is an implementation and adaptation of the paper **"Generative Semantic Communication: Diffusion Models for Semantic Image Transmission"** by Grassucci et al. (2023). It builds upon the [guided-diffusion](https://github.com/openai/guided-diffusion) codebase by OpenAI.

### Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

Install dependencies:

pip install -r requirements.txt

This project utilizes the Cityscapes Dataset. Due to license restrictions, you must download it manually.

Register and download gtFine_trainvaltest.zip and leftImg8bit_trainvaltest.zip from the Cityscapes Website.

Extract them into a ./data folder.

Ensure the directory structure looks like this:

Plaintext
/data
   /leftImg8bit
   /gtFine

To train the diffusion model from scratch using our custom robustness parameters:

Bash
python image_train.py \
    --data_dir ./data \
    --dataset_mode cityscapes \
    --image_size 128 --num_channels 128 --num_res_blocks 2 \
    --attention_resolutions "16,8" \
    --lr 1e-4 --batch_size 2 --lr_anneal_steps 150000 \
    --save_interval 10000 --use_fp16 true \
    --class_cond true --num_classes 35 \
    --cond_noise_std 0.1 \
    --cond_dropout_rate 0.25
Key Flags:

--cond_noise_std: Variance of Gaussian noise added to semantics during training.

--cond_dropout_rate: Probability of zeroing out semantic information (forcing the model to learn robustness).

2. Sampling / Inference (The "Receiver" Simulation)

To simulate the communication channel and generate images using a trained model:

Bash
python image_sample.py \
    --model_path ./checkpoints/your_model.pt \
    --results_path ./results_snr10 \
    --snr 10 \
    --num_samples 50 --batch_size 1 \
    --image_size 128 --class_cond true --num_classes 35 \
    --num_channels 128 --num_res_blocks 2 \
    --attention_resolutions "16,8" \
    --noise_schedule linear --use_scale_shift_norm true \
    --use_fp16 true

If you find this code useful, please credit the original authors of the GESCO framework:

@article{grassucci2023generative,
  title={Generative Semantic Communication: Diffusion Models for Semantic Image Transmission},
  author={Grassucci, Eleonora and others},
  journal={arXiv preprint},
  year={2023}
}
Base Codebase

OpenAI Guided Diffusion: https://github.com/openai/guided-diffusion

Acknowledgments

This project was developed at [University of Agder].
