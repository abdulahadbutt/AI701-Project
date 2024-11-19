import requests
from PIL import Image
import torch
import os
import pandas as pd 
from tqdm import tqdm 
from transformers import AutoProcessor, LlavaForConditionalGeneration
import shortuuid
import json 
import argparse

def eval_model(args):
    data_directory = args.directory
    imgs_path = f'{data_directory}/MMVP Images'

    print(data_directory)
    if args.question_file.lower() == 'custom':
        benchmark_dir = '/home/paperspace/AI701/dataset/CustomQuestions.csv'
    elif args.question_file.lower() == 'original':
        benchmark_dir = os.path.join(data_directory, 'Questions.csv')
    else:
        print('Question File not listed or is incorrect')
        exit()


    # * Load the model in half-precision
    model_path = args.model_path
    model = LlavaForConditionalGeneration.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")
    processor = AutoProcessor.from_pretrained(model_path)




    df = pd.read_csv(benchmark_dir) 
    answers_file = args.answers_file
    ans_file = open(f'dataset/{answers_file}', "w")

    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        torch.cuda.empty_cache()

        # Construct the 'prompts' string
        cur_prompt = row['Question'] + " " + row['Options']
        qs = cur_prompt
        # print(qs)

        photo_id = index+1

        image_path = f'{imgs_path}/{photo_id}.jpg'
        image = Image.open(image_path)

        # * Prepping for LLaVA entry
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "image"},
                    {"type": "text", "text": qs},
                ],
            },
        ]

        prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
        # print(prompt)
        inputs = processor(images=[image], text=prompt, padding=True, return_tensors="pt").to(model.device, torch.float16)
        generate_ids = model.generate(**inputs, max_new_tokens=30)
        outputs = processor.batch_decode(generate_ids, skip_special_tokens=True)
        outputs = outputs[0]
        # print(outputs)
        # * Stripping output to get what we want
        outputs = outputs.split("ASSISTANT: ")[-1]

        ans_id = shortuuid.uuid()
        ans_file.write(json.dumps({"question_id": photo_id,
                                    "prompt": cur_prompt,
                                    "answer": row["Correct Answer"], 
                                    "response": outputs,
                                    "answer_id": ans_id,
                                    "model_id": "llava-hf/llava-1.5-13b-hf",
                                    "dataset": args.question_file.lower(),
                                    }) + "\n")
        ans_file.flush()
        break 
    ans_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="llava-hf/llava-1.5-13b-hf")
    parser.add_argument("--directory", type=str, default="/home/paperspace/AI701/MMVP")
    parser.add_argument("--question-file", type=str, default="MMVP")
    parser.add_argument("--answers-file", type=str, default="answer.jsonl")
    args = parser.parse_args()

    eval_model(args)