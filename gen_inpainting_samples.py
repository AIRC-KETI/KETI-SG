import os
import shutil
import numpy as np
import json
import csv
import cv2
from tqdm import tqdm


PATH_DB_TARGET = './data/val/'

# data sources : raw images
PATH_DB_IMAGE = PATH_DB_TARGET + '/image/'

# data target : inpainting samples
PATH_DB_INPAINT = PATH_DB_TARGET + 'inpainting_samples/'
PATH_DB_INPAINT_JSON = PATH_DB_TARGET + 'inpainting_samples/json_samples/'
PATH_DB_INPAINT_MASK = PATH_DB_TARGET + 'inpainting_samples/mask/'
PATH_DB_INPAINT_SAMPLE_IMG = PATH_DB_TARGET + 'inpainting_samples/masked_image/'


json_files = os.listdir(PATH_DB_INPAINT_JSON)

for json_file in tqdm(json_files):
    # sample path
    path_img = PATH_DB_IMAGE + json_file[:-len(json_file.split('_')[-1])-1] + '.jpg'
    path_mask = PATH_DB_INPAINT_MASK + json_file[:-5] + '.png'
    path_sample_img = PATH_DB_INPAINT_SAMPLE_IMG + json_file[:-5] + '.jpg'
    
    img_origin = cv2.imread(path_img)
    with open(PATH_DB_INPAINT_JSON + json_file,'r') as f:
        json_sample = json.load(f)
        masked_obj = json_sample['masked_object']
        x = masked_obj['object_bbox']['x']
        y = masked_obj['object_bbox']['y']
        w = masked_obj['object_bbox']['width']
        h = masked_obj['object_bbox']['height']
        
        tmp_mask = np.zeros(img_origin.shape)
        cv2.rectangle(tmp_mask, (x, y, w, h), (255,255,255), -1)
        cv2.imwrite(path_mask, tmp_mask)
        masked_img = np.clip(img_origin + tmp_mask, 0, 255)
        cv2.imwrite(path_sample_img, masked_img)