#!/usr/bin/env python
"""Сборка расширения oxt в каталоге src.

"""
# TODO: version.

import os
from shutil import make_archive, copy, copytree, rmtree
from pathlib import Path

ext_name = 'Csl2Pdf'
zip_file = Path(f'{ext_name}.zip')
ext_file_name = Path(f'{ext_name}.oxt')
tmp_dir_path = Path('tmp~~')

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
        return
    
    try:
        tmp_dir_path.mkdir(exist_ok=True)
    except Exception as e:
        print(f'Error {e}')
        return

    for _dir in dirs_list:
        try:
            copytree(_dir, tmp_dir_path.joinpath(_dir).as_posix(), dirs_exist_ok=True)
        except Exception as e:
            print(f'Error {e}')
            return

    for _file in files_list:
        try:
            copy(_file, tmp_dir_path.as_posix())
        except Exception as e:
            print(f'Error {e}')
            return

    try:
        print(f'Make OXT ... ', end='')
        make_archive(base_name=ext_name, format='zip', root_dir=tmp_dir_path)
    except Exception as e:
        print('NO')
    else:

        if zip_file.exists:
            zip_file.rename(ext_file_name)
        print('OK')
        try:
            copy(ext_file_name, '..')
        except Exception as e:
            print(f'Error {e}')

    finally:
        try:
            rmtree(tmp_dir_path)
        except Exception as er:
            print(f'Error {er}')
        return


if __name__ == '__main__':
    main()


