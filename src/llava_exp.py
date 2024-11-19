import requests
from PIL import Image
import torch
import os
import pandas as pd 
from tqdm import tqdm 
from transformers import AutoProcessor, LlavaForConditionalGeneration
import shortuuid
import json 

# # Load the model in half-precision
model = LlavaForConditionalGeneration.from_pretrained("llava-hf/llava-1.5-13b-hf", torch_dtype=torch.float16, device_map="auto")
processor = AutoProcessor.from_pretrained("llava-hf/llava-1.5-13b-hf")

DATA_DIR = '/home/paperspace//MMVP/MMVP'
IMGS_PATH = f'{DATA_DIR}/MMVP Images'

benchmark_dir = os.path.join(DATA_DIR, 'Questions.csv')
df = pd.read_csv(benchmark_dir) 
answers_file = 'answers.jsonl'
ans_file = open(answers_file, "w")

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    torch.cuda.empty_cache()
    # Construct the 'prompts' string

    cur_prompt = row['Question'] + " " + row['Options']
    qs = cur_prompt
    print(qs)

    photo_id = index+1

    # image_path = os.path.join(IMGS_PATH, f"{photo_id}.jpg")
    image_path = f'{IMGS_PATH}/{photo_id}.jpg'
    print(IMGS_PATH)
    image = Image.open(image_path)

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
    outputs = outputs.split("ASSISTANT: ")[-1]

    ans_id = shortuuid.uuid()
    ans_file.write(json.dumps({"question_id": photo_id,
                                   "prompt": cur_prompt,
                                   "answer": row["Correct Answer"], 
                                   "response": outputs,
                                   "answer_id": ans_id,
                                   "model_id": "llava-hf/llava-1.5-13b-hf",
                                   }) + "\n")
    ans_file.flush()
ans_file.close()
