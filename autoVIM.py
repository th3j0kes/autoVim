import subprocess
import tempfile
import shlex
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("interface", choices=["Pathogen", "VimPlug"])
args = parser.parse_args()
interface = args.interface

#Currently only handles Pathogen install
print("Interface: {}".format(interface))

try:
    os.chdir("/home/noeortega/.vim")
except:
    os.makedirs("~/.vim")
    os.chdir("~/.vim")

os.makedirs("bundle")
os.makedirs("autoload")

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


def download_interface():
    if interface == "Pathogen":
        subprocess.Popen(
            "curl -LSso ~/.vim/autoload/pathogen.vim \
            https://tpo.pe/pathogen.vim"
        )
    elif interface == "VimPlug":
        subprocess.Popen(
            "curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
            https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
        )
