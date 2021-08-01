#!/usr/bin/env python3
import os
import shutil
import logging
import argparse
from gitignore_parser import parse_gitignore
from git import Repo

BACKUP_IGNORE_FILE = ".backupignore"
TIMESHIFT_FOLDER_SRC = "/home/daniel/data/timeshift"
TIMESHIFT_FOLDER_DST = "/media/daniel/hd-externo-ext4"
REGULAR_BACKUP_FOLDER_SRC = "/home/daniel/data"
REGULAR_BACKUP_FOLDER_DST = "/media/daniel/hd-externo/backup"
REPOS_FOLDER = "/home/daniel/data/meus-repositorios"

should_ignore = parse_gitignore(BACKUP_IGNORE_FILE)


def backup_file(full_path_src, path_dst):
    full_path_dst = os.path.join(path_dst, os.path.basename(full_path_src))

    if os.path.exists(full_path_dst):
        logging.debug(f'deleting {full_path_dst}')
        os.remove(full_path_dst)

    logging.debug(f'copying {full_path_src} to {full_path_dst}')
    shutil.copy2(full_path_src, path_dst)


def ignore(src, names):
    return [name for name in names if should_ignore(name)]


def backup_dir(full_path_src, full_path_dst):
    if os.path.exists(full_path_dst):
        logging.debug(f'deleting {full_path_dst}')
        shutil.rmtree(full_path_dst)

    logging.debug(f'copying {full_path_src} to {full_path_dst}')
    shutil.copytree(full_path_src, full_path_dst, ignore=ignore)


def backup_regular_files():
    logging.info('starting regular files backup')

    for path in os.listdir(REGULAR_BACKUP_FOLDER_SRC):
        if not should_ignore(path):
            full_path_src = os.path.join(REGULAR_BACKUP_FOLDER_SRC, path)
            full_path_dst = os.path.join(REGULAR_BACKUP_FOLDER_DST, path)

            if os.path.isfile(full_path_src):
                backup_file(full_path_src, REGULAR_BACKUP_FOLDER_DST)
            else:
                backup_dir(full_path_src, full_path_dst)
        else:
            logging.debug(f'ignoring {path}')

    logging.info('ending regular files backup')


def backup_timeshift_files():
    logging.info('starting timeshift files backup')
    logging.info(f'deleting timeshift backup folder at {TIMESHIFT_FOLDER_DST}')
    shutil.rmtree(TIMESHIFT_FOLDER_DST)
    logging.info(
        f'copying timeshift files from {TIMESHIFT_FOLDER_SRC} to {TIMESHIFT_FOLDER_DST}')
    shutil.copytree(TIMESHIFT_FOLDER_SRC, TIMESHIFT_FOLDER_DST)
    logging.info('ending timeshift files backup')


def locals_and_remotes_match(repo):
    repo.remotes['origin'].fetch()
    local_commits = [local.commit.hexsha for local in repo.branches]
    remote_commits = set(
        [remote.commit.hexsha for remote in repo.remotes['origin'].refs])

    if len(local_commits) != len(remote_commits):
        return False

    for local in local_commits:
        if local not in remote_commits:
            return False

    return True


def check_git_repos():
    logging.info('checking git repos')

    for path in os.listdir(REPOS_FOLDER):
        full_path = os.path.join(REPOS_FOLDER, path)

        repo = Repo(full_path)
        if repo.is_dirty(untracked_files=True) or not locals_and_remotes_match(repo):
            logging.warning(f'repo {path} is not up-to-date.')
        else:
            logging.info(f'repo {path} is ok')

    logging.info('git repos checks finished')


def parse_args():
    parser = argparse.ArgumentParser(
        description='Backup script. You know how to use.')
    parser.add_argument('--log-level',
                        dest='log_level',
                        type=str,
                        help='Log level. Default: INFO.',
                        default='INFO',
                        choices=['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])

    parser.add_argument('--timeshift',
                        dest='enable_timeshift',
                        action='store_true',
                        help='Enable timeshift folder backup. If you set this flag, don\'t forget sudo.')

    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=args.log_level)

    try:
        backup_regular_files()
        if args.enable_timeshift:
            backup_timeshift_files()
        check_git_repos()
    except Exception as err:
        logging.error(f'exception: {str(err)}')


if __name__ == '__main__':
    main()
