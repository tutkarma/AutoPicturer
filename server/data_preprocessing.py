import csv
import json
import collections

dict_labels = collections.defaultdict(list)
dict_urls = {}
dict_tages = {}

def get_labels(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            dict_labels[line["LabelName"]].append(line["ImageID"])


def get_urls(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            dict_urls[line["ImageID"]] = line["OriginalURL"]


def get_tages(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            dict_tages[line[1]] = line[0]

def save_to_json_file(file, data):
    with open(file, 'w') as fp:
        json.dump(data, fp)


if __name__ == "__main__":
    get_labels("./data/humanLabels/test-annotations-human-imagelabels.csv")
    get_labels("./data/humanLabels/train-annotations-human-imagelabels.csv")
    get_labels("./data/humanLabels/validation-annotations-human-imagelabels.csv")
    get_labels("./data/machineLabels/test-annotations-machine-imagelabels.csv")
    get_labels("./data/machineLabels/train-annotations-machine-imagelabels.csv")
    get_labels("./data/machineLabels/validation-annotations-machine-imagelabels.csv")
    #get_labels("testlabels.csv")
    dict_labels = dict(dict_labels)
    print("Labels are loaded")

    get_urls("./data/imageIDs/test-images-with-rotation.csv")
    get_urls("./data/imageIDs/train-images-with-labels-rotation.csv")
    get_urls("./data/imageIDs/validation-images-with-rotation.csv")
    #get_urls("testurls.csv")
    print("URLs are loaded")

    get_tages("./data/class-descriptions.csv")
    #get_tages("testtages.csv")
    print("Tages are loaded")

    for label in dict_labels:
        urls = []
        for imageID in dict_labels[label]:
            urls.append(dict_urls[imageID])
        dict_labels[label] = urls
    print("IDs replaced with labels")

    for tag in dict_tages:
        label = dict_tages[tag]
        dict_tages[tag] = dict_labels[label]
    print("Labels replaced with URLs")

    file_out = "./data/result.json"
    save_to_json_file(file_out, dict_tages)
    print("Final file is saved")
