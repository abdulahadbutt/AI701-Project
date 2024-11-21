# AI701 - Clip Blind Pairs




# Setup
## Dataset
We used the [MMVP](https://huggingface.co/datasets/MMVP/MMVP) dataset as a benchmark for our project
```
git clone https://huggingface.co/datasets/MMVP/MMVP
```

In addition to this, we have created our questions for these clip blind pairs



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


# Running
After Installing dependencies for LLaVA and MMVP, we use the code in src/ directories to benchmark each of these. Since we are running on multiple models and two datasets, we have added .sh files for ease. To run the LLaVA LLM simply input
```
source run_llava.sh
```

Similarly, to run MoF models, run
```
source run_mof.sh
```

The results are saved in the dataset directory



