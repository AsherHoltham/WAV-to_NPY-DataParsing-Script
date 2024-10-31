import numpy as np
import pandas as pd
import math
import os
import shutil


import processing as p

def allocator(df):
    set_len = len(df)
    
    train_len =  math.floor(set_len * .7)
    validation_len =  math.floor(set_len * .15)

    df.set_index(df.columns[1], inplace=True)

    index = 1
    for f in df.index:
        folder = 'train'

        filename = str(f)
        filename = filename[:-4]

        label = int(df.loc[f].iloc[0])
        label = str(label)

        file = label + filename + '.npy'
        np.save(file,  p.converter('/Users/asheraugustusholtham/Desktop/data/wavfiles/' + f))

        if(index < train_len): folder = 'train'
        elif(index < train_len + validation_len): folder = 'validation'
        else: dest = folder = 'test'

        file_loc = '/Users/asheraugustusholtham/Desktop/Avian-Classifier-CNN-Model/data/' + file
        folder_loc = '/Users/asheraugustusholtham/Desktop/Avian-Classifier-CNN-Model/data/' + folder

        dest = os.path.join(folder_loc, os.path.basename(file_loc))
        shutil.move(file, dest)
        
        index += 1