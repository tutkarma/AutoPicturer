import pandas as pd
import numpy as np
import itertools
import gc

def get_tag_lists(df):
    keys, values = df.sort_values('Tag').values.T
    ukeys, index = np.unique(keys,True)
    arrays = np.split(values, index[1:])
    df2 = pd.DataFrame({'Tag' : ukeys, 'URLs' : [list(itertools.chain.from_iterable(a)) for a in arrays]})
    return df2


if __name__ == "__main__":
    label1 = pd.read_csv("D:/prac/server/data/humanLabels/test-annotations-human-imagelabels.csv", sep=',', encoding='utf-8', usecols=['ImageID', 'LabelName'])
    label2 = pd.read_csv("D:/prac/server/data/humanLabels/train-annotations-human-imagelabels.csv", sep=',', encoding='utf-8', usecols=['ImageID', 'LabelName'])
    label3 = pd.read_csv("D:/prac/server/data/humanLabels/validation-annotations-human-imagelabels.csv", sep=',', encoding='utf-8', usecols=['ImageID', 'LabelName'])
    label4 = pd.read_csv("D:/prac/server/data/machineLabels/test-annotations-machine-imagelabels.csv", sep=',', encoding='utf-8', usecols=['ImageID', 'LabelName'])
    label5 = pd.read_csv("D:/prac/server/data/machineLabels/train-annotations-machine-imagelabels.csv", sep=',', encoding='utf-8', usecols=['ImageID', 'LabelName'])
    label6 = pd.read_csv("D:/prac/server/data/machineLabels/validation-annotations-machine-imagelabels.csv", sep=',', encoding='utf-8', usecols=['ImageID', 'LabelName'])
    df_label = pd.concat([label1, label2, label3, label4, label5, label6])
    del label1
    label1 = pd.DataFrame()
    gc.collect()
    del label2
    label2 = pd.DataFrame()
    gc.collect()
    del label3
    label3 = pd.DataFrame()
    gc.collect()
    del label4
    label4 = pd.DataFrame()
    gc.collect()
    del label5
    label5 = pd.DataFrame()
    gc.collect()
    del label6
    label6 = pd.DataFrame()
    gc.collect()
    #df_label = pd.read_csv("D:/prac/server/testlabels.csv", sep=',', encoding='utf-8')
    print("Labels are loaded")

    url1 = pd.read_csv("D:/prac/server/data/imageIDs/test-images-with-rotation.csv", sep=',', encoding='utf-8', usecols=['ImageID','OriginalURL'])
    url2 = pd.read_csv("D:/prac/server/data/imageIDs/train-images-with-labels-with-rotation.csv", sep=',', encoding='utf-8', usecols=['ImageID','OriginalURL'])
    url3 = pd.read_csv("D:/prac/server/data/imageIDs/validation-images-with-rotation.csv", sep=',', encoding='utf-8', usecols=['ImageID','OriginalURL'])
    df_url = pd.concat([url1, url2, url3])

    del url1
    url1 = pd.DataFrame()
    gc.collect()
    del url2
    url2 = pd.DataFrame()
    gc.collect()
    del url3
    url3 = pd.DataFrame()
    gc.collect()
    #df_url = pd.read_csv("D:/prac/server/testurls.csv", sep=',', encoding='utf-8', usecols=['ImageID','OriginalURL'])
    print("URLs are loaded")

    # imageID -> url
    df_label['ImageID'] = df_label['ImageID'].map(df_url.set_index('ImageID')['OriginalURL'])
    df_label.rename(columns={'ImageID': 'URL'}, inplace=True)
    print("IDs replaced with labels")
    # label -- [urls]
    df_label = df_label['URL'].groupby([df_label.LabelName]).apply(list).reset_index()
    print("URLs concatinated")

    df_tag = pd.read_csv("D:/prac/server/data/class-descriptions.csv", sep=',', encoding='utf-8', names=['LabelName','Tag'])
    print("Tags are loaded")
    #df_tag = pd.read_csv("D:/prac/server/testtages.csv", sep=',', names=['LabelName','Tag'])
    df_tag = df_tag[['Tag', 'LabelName']]
    # tag -- [urls]
    df_tag['LabelName'] = df_tag['LabelName'].map(df_label.set_index('LabelName')['URL'])
    print("Labels replaced with URLs")
    df_tag.rename(columns={'LabelName': 'URLs'}, inplace=True)
    df_tag = get_tag_lists(df_tag)

    #df_tag.set_index('Tag')['URLs'].to_json("D:/prac/server/test.json")
    df_tag.to_json("D:/prac/server/new_data.json", orient='records', lines=True)
    print("Final file is saved")