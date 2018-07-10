#!/usr/bin/env bash

mkdir -p data
cd data
mkdir -p imageIDs
mkdir -p machineLabels
mkdir -p humanLabels
#wget https://storage.googleapis.com/openimages/2018_04/image_ids_and_rotation.csv
wget https://storage.googleapis.com/openimages/2018_04/class-descriptions.csv

wget https://storage.googleapis.com/openimages/2018_04/test/test-images-with-rotation.csv
mv test-images-with-rotation.csv imageIDs
wget https://storage.googleapis.com/openimages/2018_04/validation/validation-images-with-rotation.csv
mv validation-images-with-rotation.csv imageIDs
wget https://storage.googleapis.com/openimages/2018_04/train/train-images-with-labels-with-rotation.csv
mv train-images-with-labels-with-rotation.csv imageIDs

wget https://storage.googleapis.com/openimages/2018_04/test/test-annotations-machine-imagelabels.csv
mv test-annotations-machine-imagelabels.csv machineLabels
wget https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-machine-imagelabels.csv
mv validation-annotations-machine-imagelabels.csv machineLabels
wget https://storage.googleapis.com/openimages/2018_04/train/train-annotations-machine-imagelabels.csv
mv train-annotations-machine-imagelabels.csv machineLabels

wget https://storage.googleapis.com/openimages/2018_04/test/test-annotations-human-imagelabels.csv
mv test-annotations-human-imagelabels.csv humanLabels
wget https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-human-imagelabels.csv
mv validation-annotations-human-imagelabels.csv humanLabels
wget https://storage.googleapis.com/openimages/2018_04/train/train-annotations-human-imagelabels.csv
mv train-annotations-human-imagelabels.csv humanLabels
