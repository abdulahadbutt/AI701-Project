import glob 
import pandas as pd 

scored_paths = glob.glob('dataset/scored/*.csv')
for path in scored_paths:
    df = pd.read_csv(path)

    correct = 0
    total = df.shape[0] // 2

    # print(df['Score'].sum() / df.shape[0])
    for i in range(0, total, 2):
        is_correct_0 = df.iloc[i]['Score']
        is_correct_1 = df.iloc[i+1]['Score']

        # print(is_correct_0)
        # print(is_correct_1)
        if is_correct_1 == 1 and is_correct_0 == 1:
            correct += 1
    print(f'[{path}]: {correct}/{total} : {correct/total:.2f} |||| {df['Score'].sum()}/{df.shape[0]} : {df['Score'].sum()/df.shape[0]:.2f}')
    # print(f'[{path}]: {df['Score'].sum()}/{df.shape[0]} : {df['Score'].sum()/df.shape[0]:.2f}')

         