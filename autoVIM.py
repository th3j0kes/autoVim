import subprocess
import tempfile
import shlex
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("interface", choices=["Pathogen", "VimPlug"])
args = parser.parse_args()
interface = args.interface

#Currently only handles Pathogen or VimPlug install
print("Interface: {}".format(interface))
#https://github.com/tpope/vim-pathogen
#https://github.com/junegunn/vim-plug

try:
    os.chdir("~/.vim")
except:
    os.makedirs("~/.vim")
    os.chdir("~/.vim")

#os.makedirs("bundle")
#os.makedirs("autoload")

#pathogen_vimrc = """execute pathogen#infect()
#syntax on
#filetype plugin indent on
#""")

#vimplug_vimrc = """plug#begin()
#Plug '{}'
#call plug#end
#""".format(plugin)
#********MUST RELOAD .VIMRC and :PlugInstall to install plugins*************

def vimrc_config(interface):
    if interface == "Pathogen":
#        with open("/home/noeortega/.vimrc", "w") as vimrc:
#            vimrc.write(pathogen_vimrc)

vimrc_config(interface)


def download_interface(interface):
    if interface == "Pathogen":
        print("[*]-----Downloading Pathogen-----[*]")
        #subprocess.Popen(
        #    "curl -LSso ~/.vim/autoload/pathogen.vim \
        #    https://tpo.pe/pathogen.vim"
        #)
        print("[*]-----Download Complete-----[*]")
    elif interface == "VimPlug":
        print("[*]-----Downloading VimPlug-----[*]")
        # subprocess.Popen(
        #     "curl -fLo ~/.vim/autoload/plug.vim \
        #     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
        # )
        print("[*]-----Download Complete-----[*]")

#download_interface(interface)

#list of popular VIM plugins
plugins = [
    "https://github.com/tpope/vim-fugitive.git",
    "https://github.com/scrooloose/nerdtree.git",
    "https://github.com/vim-airline/vim-airline.git",
    "https://github.com/vim-airline/vim-airline-themes.git",
    "https://github.com/ervandew/supertab.git",
    "https://github.com/tpope/vim-commentary.git",
    "https://github.com/SirVer/ultisnips.git",
    "https://github.com/xuyuanp/nerdtree-git-plugin",
    "https://github.com/ntpeters/vim-better-whitespace.git"
]

#for plugin in plugins:
#    os.chdir("~/.vim/bundle")
#    args = shlex.split("git clone " + repo)
#    p = subprocess.Popen(args)
