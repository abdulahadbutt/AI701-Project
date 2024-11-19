conda activate llava
python src/llava_exp.py --question-file=custom --answers-file="llava-1.5-13b-hf-custom.jsonl"
python src/llava_exp.py --question-file=original --answers-file="llava-1.5-13b-hf-mmvp.jsonl"