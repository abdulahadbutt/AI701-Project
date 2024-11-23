import pandas as pd 
from openai import OpenAI
import glob 
import argparse
import re 
import time 
import string 
from tqdm import tqdm 



NUM_SECONDS_TO_SLEEP = 10
def get_yes_no_answer(question):
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    'role': 'system',
                    'content': 'You are a helpful and precise assistant for checking the quality of the answer. Please answer in only yes or no.'
                }, {
                    'role': 'user',
                    'content': question,
                }],
            )
            break 
        except Exception as e:
            print(e)
        time.sleep(NUM_SECONDS_TO_SLEEP)

    answer = response.choices[0].message.content
    # print(f'GPT Answer: {answer}')
    # print(repr(answer))
    answer = answer.translate(str.maketrans('', '', string.punctuation))
    yes_no_regex = re.compile(r"^(?:Yes|No)$", re.IGNORECASE)
    # print(yes_no_regex.match(answer))

    if yes_no_regex.match(answer):
        return answer.lower()
    else:
        return "Could not determine yes or no."


parser = argparse.ArgumentParser(description='Process OpenAI API key and JSONL file path.')
parser.add_argument('--openai_api_key', default = "", help='Your OpenAI API key')
args = parser.parse_args()
api_key = args.openai_api_key

for file_path in glob.glob('dataset/csvs/*.csv'):

    print(file_path)
    save_path = file_path.split('/')[-1]
    save_path = f'dataset/scored/{save_path}'
    # print(save_path)
    # break 
    client = OpenAI(
        api_key=api_key
    )
    df = pd.read_csv(file_path)
    df['Score'] = '0'
    df['GPT_Grade'] = ''
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        question = row['Question']
        corr_answer = row['Correct Answer']
        model_response = row['Response']
        question4gpt = f"Given the following question {question}, the correct answer is {corr_answer}. Does the following answer correctly answers the question, answer:{model_response}?"
        # print(question, corr_answer)
        # print(question4gpt)
        gpt_grade = get_yes_no_answer(question4gpt)
        df.iloc[i, df.columns.get_loc('GPT_Grade')] = gpt_grade
        if gpt_grade=="yes":
            df.iloc[i, df.columns.get_loc('Score')] = '1'
        elif gpt_grade == 'Could not determine yes or no.':
            df.iloc[i, df.columns.get_loc('Score')] = 'NA'
        
    df.to_csv(save_path, index=False)

