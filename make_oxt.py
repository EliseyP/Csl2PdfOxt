#!/usr/bin/env python

import os
from shutil import make_archive, copy, copytree, rmtree
from zipfile import ZipFile
# from distutils.dir_util import copy_tree
from pathlib import Path

ext_name = 'Csl2Pdf'
ext_file_name = Path(f'{ext_name}.oxt')
_tmp_dir_path = Path('tmp~~')

dirs_list = [
    'Csl2Pdf',
    'Images',
    'META-INF',
    'pkg-description',
    'registration',  
]

files_list = [
    'Addons.xcu',
    'description.xml'
]
update_file_name = f'{ext_name}.update.xml'

def main():
    try:
        os.chdir('src')
    except Exception as e:
        print(f'Error {e}')
    
    try:
        _tmp_dir_path.mkdir(exist_ok=True)
    except Exception as e:
        print(f'Error {e}')

    # try:
    #     os.chdir('src')
    # except Exception as e:
    #     print(f'Error {e}')

    for _dir in dirs_list:
        # copy_tree(_dir, _tmp_dir_path.as_posix())
        copytree(_dir, _tmp_dir_path.joinpath(_dir).as_posix(), dirs_exist_ok=True)

    for _file in files_list:
        copy(_file, _tmp_dir_path.as_posix())    

    try:
        print(f'Zip tmp dir ... ', end='')
        make_archive(base_name=ext_name, format='zip', root_dir=_tmp_dir_path)
    except Exception as err:
        print('NO')
        # raise MyErrorOperation from err
    else:
        print('OK')

    zip_file = Path(f'{ext_name}.zip')
    if zip_file.exists:
        zip_file.rename(f'{ext_name}.oxt')

    rmtree(_tmp_dir_path)

if __name__ == '__main__':
    main()


