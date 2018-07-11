from BeautifulSoup import BeautifulSoup
import urllib2
import subprocess
import tempfile
import shlex
import os

page = urllib2.urlopen("https://github.com/tpope/vim-fugitive")
soup = BeautifulSoup(page)
soup = soup.prettify()
pwd = os.getcwd()
os.chdir("/home/noeortega/.vim")
os.makedirs("bundle")
os.makedirs("autoload")

subprocess.Popeon("curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim")

repos = [
    "https://github.com/tpope/vim-fugitive.git",
    "https://github.com/scrooloose/nerdtree.git",
    "https://github.com/vim-airline/vim-airline.git",
    "https://github.com/vim-airline/vim-airline-themes.git",
    "https://github.com/ervandew/supertab.git"
]
for repo in repos:
    os.chdir("/home/noeortega/.vim/testing")
    args = shlex.split("git clone " + repo)
    p = subprocess.Popen(args)
