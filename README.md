# Potholes-Detection

### Dataverse Hack: Build an AI Model to Save Lives

## Description: 
Over the past few years, the increase in the number of vehicles on road gave rise to the number of road accidents. According to a study, one fatal road accident occurs every 5 minutes in the country, and 8 die on roads every hour. This has become a major concern in the country. One of the primary causes of these road accidents is the management and maintenance of the roads. Potholes on roads can cause serious accidents, and any vehicle traveling at some decent speed can lose its track due to them. In the case of four-wheeler vehicles, potholes can cause severe damage to wheels and tires. More specifically, when it comes to two-wheelers like motorbikes, these vehicles are more prone to accidents due to potholes as the tendency to cause imbalance is very high and can lead to fatalities. In this [Dataverse Hack](https://datahack.analyticsvidhya.com/contest/dataverse-hack/) presented by Analytics Vidhya we build a computer vision model to detect pothole.

## My Approach:
For our final submission, we employed `YOLOv7`. We started with the YOLOv5. The outcome was encouraging, but further accuracy was anticipated. The given CSV file was initially converted to the YOLO format. Despite the application of image processing, the accuracy did not improve. Thus, we utilized the provided images without any preprocessing. Image augmentation was carried out using the `albumentations` library, which significantly boosted the score. src folder contains all the helper scripts.

Tranning hyperparameters:
- Environment: Google Colab
- Epochs: 50
- batch_size : 16
- img: 640
- lr: 0.01
- conf: 0.005

## Final Result:
 - Leaderboard Standing: `6th among 1145 teams`
 - Final Score: 0.4357561564 (Team name: `Caraxes`)

## Sample detection:
![alt text]()