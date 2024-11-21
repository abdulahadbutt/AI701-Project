conda activate mmvp
python src/mof_exp.py --directory MMVP --model-path MMVP/MoF_Models --question-file custom --answers-file='MoF_Models-custom.jsonl'
python src/mof_exp.py --directory MMVP --model-path MMVP/MoF_Models --question-file original --answers-file='MoF_Models-mmvp.jsonl'
