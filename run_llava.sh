conda activate llava
python src/llava_exp.py --question-file=custom --answers-file="llava-1.5-13b-hf-custom.jsonl"
python src/llava_exp.py --question-file=original --answers-file="llava-1.5-13b-hf-mmvp.jsonl"
python src/llava_exp.py --model-path='llava-hf/llava-1.5-7b-hf' --answers-file='llava-1.5-7b-hf-custom.jsonl' --question-file=custom 
python src/llava_exp.py --model-path='llava-hf/llava-1.5-7b-hf' --answers-file='llava-1.5-7b-hf-mmvp.jsonl' --question-file=original 
# python src/llava_exp.py --model-path='llava-hf/llava-v1.6-vicuna-7b-hf' --answers-file='llava-v1.6-vicuna-7b-hf-mmvp.jsonl' --question-file=original 
# python src/llava_exp.py --model-path='llava-hf/llava-v1.6-vicuna-7b-hf' --answers-file='llava-v1.6-vicuna-7b-hf-custom.jsonl' --question-file=custom 
