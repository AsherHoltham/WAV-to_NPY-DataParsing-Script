import pandas as pd
import processing as p

# Parse the metadata from CSV and produce a CSV with just the file and label
print("Removing old .npy files")
p.cleaner()
print("Parsing new random odered .wav files from .csv file")
p.parser("/Users/asheraugustusholtham/Desktop/data/bird_songs_metadata.csv")
df = pd.read_csv('data.csv')
print("Allocating new .npy files fractionally proportional to their respecive data groups")
print("Please wait this may take a few moments")
p.allocator(df)