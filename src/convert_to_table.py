import glob 
import pandas as pd 
import json 
from tqdm import tqdm 

answers_file_glob = glob.glob(
    'dataset/*.jsonl'
)

for answer_path in tqdm(answers_file_glob):
    data = open(answer_path, 'r').read().split('\n')[:-1]
    file_name = answer_path.split('.json')[0].split('dataset')[-1]
    new_data = []
    # print(data)
    for line in data:
        line_dict = json.loads(line)
        item = {
            'Index': line_dict['question_id'],
            'Question': line_dict['prompt'],
            # 'Question': line_dict['prompt'].split(' (a')[0],
            'Correct Answer': line_dict['answer'],
            'Response': line_dict['response']
        }

        # print(item)
        new_data.append(item)

        # break 
    df = pd.DataFrame.from_dict(new_data)
    df.to_csv(f'dataset/csvs/{file_name}.csv', index=False)
    # break 