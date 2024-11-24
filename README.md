# AI701 - You Can't See Me: Exploring Blindness of MLLMs 


# Abstract
This project aims to reveal the shortcomings in the visual capabilities of MultiModal Language Models (MLLMs). Our study rigorously evaluates a dataset based
on the characteristic of "CLIP-blindness" on State of the Art (SOTA) MLLMs.
It reveals that state-of-the-art systems struggle with basic visual patterns, often
providing incorrect answers and hallucinations. We also evaluate a Mixture of
Features approach to address these issues, highlighting the importance of accurate
visual grounding for future successful multi-modal systems.



# Setup
## Dataset
We used the [MMVP](https://huggingface.co/datasets/MMVP/MMVP) dataset as a benchmark for our project
```
git clone https://huggingface.co/datasets/MMVP/MMVP
```
In addition to this, we have created our custom question set for these Clip-Blind pairs
## Custom Question Pair Set




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


