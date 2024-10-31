import os
import glob

def cleaner():
    print("Cleaning old .npy files:")
    
    train_dir = '/Users/asheraugustusholtham/Desktop/Avian-Classifier-CNN-Model/data/train'
    val_dir = '/Users/asheraugustusholtham/Desktop/Avian-Classifier-CNN-Model/data/validation'
    test_dir = '/Users/asheraugustusholtham/Desktop/Avian-Classifier-CNN-Model/data/test'

    test_files = glob.glob(os.path.join(test_dir, '*.npy'))
    for f in test_files:
        os.remove(f)

    print(f'{len(test_files)} testing.npy files Removed')

    val_files = glob.glob(os.path.join(val_dir, '*.npy'))
    for f in val_files:
        os.remove(f)

    print(f'{len(val_files)} validation.npy files Removed')

    train_files = glob.glob(os.path.join(train_dir, '*.npy'))
    for f in train_files:
        os.remove(f)

    print(f'{len(train_files)} training.npy files Removed')