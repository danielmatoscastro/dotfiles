#!/usr/bin/env python3

from datetime import datetime
from filecmp import dircmp
import json
import os
import pprint

BLOATED_DIRS_LIST = {
    '.venv',
    '.git'
    'node_modules',
    'bin',
    'obj',
    '.idea',
    'cmake-build-debug',
    'build',
    '__pycache__',
    '$RECYCLE.BIN',
    '.vs',
    '.vscode'
}

# BLOATED_EXT_LIST = {
#     'dll',
#     'o',
#     'exe',
#     'jar',
#     'apk'
# }

class BackupChecker:
    def __init__(self, source, backup, ignore_list):
        self._source = source
        self._backup = backup
        self._ignore_list = ignore_list
        self._report_result = None

    def report(self):
        self._report_result = {
            "bloated_dirs": [],
            #"bloated_ext": [],
            "left_only": [],
            "common_funny": [],
            "diff_files": [],
            "funny_files": []
        }

        comparison = dircmp(self._source, self._backup, ignore=self._ignore_list)
        print(f'Starting to check differences between {self._source} and {self._backup}.')
        start_time = datetime.now()
        self._check_for_problems(comparison)
        end_time = datetime.now()
        print(f'Done. Elapsed time: {end_time - start_time}')
        return self._report_result

    def _check_for_problems(self, cmp):
        left = cmp.left
        print(f'Checking {left}...')
        
        if os.path.basename(left) in BLOATED_DIRS_LIST:
            self._report_result["bloated_dirs"].append(left)
        if cmp.left_only:
            self._report_result["left_only"] += [os.path.join(left, leaf) for leaf in cmp.left_only]
        if cmp.common_funny:
            self._report_result["common_funny"] += [os.path.join(left, leaf) for leaf in cmp.common_funny]
        if cmp.diff_files:
            self._report_result["diff_files"] += [os.path.join(left, leaf) for leaf in cmp.diff_files]
        if cmp.funny_files:
            self._report_result["funny_files"] += [os.path.join(left, leaf) for leaf in cmp.funny_files]

        for sd in cmp.subdirs.values():
            self._check_for_problems(sd)

if __name__ == '__main__':
    SOURCE = '/home/drenim/storage'
    BACKUP = '/home/drenim/storage'
    IGNORE_LIST = ['/home/drenim/storage/SteamLibrary', '/home/drenim/storage/storage']
    REPORT_OUTPUT = 'report_differences_result.json'

    checker = BackupChecker(SOURCE, BACKUP, IGNORE_LIST)
    result = checker.report()
    pprint.pprint(result)
    with open(REPORT_OUTPUT, mode='w') as output:
        json.dump(result, output)