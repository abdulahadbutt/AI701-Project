# AI701 - You Can't See Me: Exploring Blindness of MLLMs 


# Abstract
This project aims to reveal the shortcomings in the visual capabilities of MultiModal Language Models (MLLMs). Our study rigorously evaluates a dataset based
on the characteristic of "CLIP-blindness" on State of the Art (SOTA) MLLMs.
It reveals that state-of-the-art systems struggle with basic visual patterns, often
providing incorrect answers and hallucinations. We also evaluate a Mixture of
Features approach to address these issues, highlighting the importance of accurate
visual grounding for future successful multi-modal systems.

# Problem Framework
![image](https://github.com/user-attachments/assets/32ecdc59-177d-4390-93bc-93c04478f1f6)

# Evaluation Pipeline
![image](https://github.com/user-attachments/assets/fef8b4d5-0ecd-438b-811f-0b26e68a8fd2)

# Interleaved Mixing of Features (MoF)
![image](https://github.com/user-attachments/assets/055df65c-284f-4984-b134-583e5e0b34c7)

# Experimental Setup
## Dataset
We used the [MMVP](https://huggingface.co/datasets/MMVP/MMVP) dataset as a benchmark for our project
```
git clone https://huggingface.co/datasets/MMVP/MMVP
```
In addition to this, we have created our custom question set for these Clip-Blind pairs
## Custom Question Pair Set
![image](https://github.com/user-attachments/assets/3b155745-0223-4fb3-bf96-ac40c84c9d7f)

## MMVP-VLM Bench Mark (Visual Categories)
![image](https://github.com/user-attachments/assets/644e5367-22c1-4a99-8f9b-8913cdbafe39)

# Results
![image](https://github.com/user-attachments/assets/de3ec131-eb75-408b-9044-3431028971ec)
![image](https://github.com/user-attachments/assets/0b77c3f9-1d1b-4e6d-946f-096be1f2bc1f)
![image](https://github.com/user-attachments/assets/f893475e-520f-4d06-98fe-b3a186d1ce25)


# Installation
First, you need to install LLaVA
```
https://github.com/haotian-liu/LLaVA.git
cd LLaVA
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # enable PEP 660 support
pip install -e .
```


# Inference
After Installing dependencies for LLaVA and MMVP, we use the code in src/ directories to benchmark each of these. Since we are running on multiple models and two datasets, we have added .sh files for ease. To run the LLaVA LLM simply input
```
source run_llava.sh
```

Similarly, to run MoF models, run
```
source run_mof.sh
```

The results are saved in the dataset directory


# Citation
```
@misc{YCSM,
      title={You Can't See Me: Exploring Blindness of MLLMs }, 
      author={Abdul Ahad Butt, Muhammad Abdullah Sohail, Raamy Kachwa},
      year={2024},
}
```


