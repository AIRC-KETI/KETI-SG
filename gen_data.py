import os
import shutil
from tqdm import tqdm



# data sources : original DB
PATH_DB_IMAGENET = '/media/hanmu/storage2/PanopticSeg/raw_images/imagenet'
PATH_DB_VG = '/media/hanmu/storage2/PanopticSeg/raw_images/visualgenome'
# PATH_DB_IMAGENET = './source/imagenet'
# PATH_DB_VG = './source/visualgenome'

PATH_DB_SOURCES = [PATH_DB_IMAGENET + '/train',
                   PATH_DB_IMAGENET + '/val',
                   PATH_DB_IMAGENET + '/test',
                   PATH_DB_VG + '/VG_100K',
                   PATH_DB_VG + '/VG_100K_2']

# data target : KETI-SG DB
PATH_DB_KETI_SG = './data'
PATH_DB_KETI_SG_SPLITS = [PATH_DB_KETI_SG + '/train',
                          PATH_DB_KETI_SG + '/val',
                          PATH_DB_KETI_SG + '/test']

# copy raw images
for db_split in PATH_DB_KETI_SG_SPLITS:
    json_files = os.listdir(db_split + '/json')
    for json_file in tqdm(json_files):
        image_filename = json_file[:-4] + 'jpg'
        for source_path in PATH_DB_SOURCES:
            if os.path.exists(source_path + '/' + image_filename):
                shutil.copyfile(source_path + '/' + image_filename, db_split + '/image/' + image_filename)
            elif os.path.exists(source_path + '/' + image_filename[:-3] + 'JPEG'):
                shutil.copyfile(source_path + '/' + image_filename[:-3] + 'JPEG', db_split + '/image/' + image_filename)
