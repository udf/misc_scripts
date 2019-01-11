import re

from glob import glob
from configparser import ConfigParser


for path in glob('**/.git/config', recursive=True):
    config = ConfigParser()
    config.read(path)
    for section in config.sections():
        if not section.startswith('remote '):
            continue
        match = re.match(r'https://github.com/(.+?)/(.+)', config[section]['url'])
        if not match:
            continue
        repo = match[2]
        if not repo.endswith('.git'):
            repo += '.git'
        config[section]['url'] = f'git@github.com:{match[1]}/{repo}'
    with open(path + '.bk', 'w') as fbk, open(path, 'r') as f:
        fbk.write(f.read())
    with open(path, 'w') as f:
        config.write(f)
