#!/bin/bash

if [ $(id -u) -ne 0 ]; then
  echo Please run this script as root or using sudo!
  exit
fi

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}\n+++ INSTALL REQUIREMENTS +++${NC}\n"
add-apt-repository -y ppa:neovim-ppa/unstable
apt update

for app in neovim curl git fzf ripgrep fd-find xclip; do
  (apt-get install -y $app >/dev/null && echo -e "${GREEN}DONE${NC} install $app") || echo -e " ${RED}ERROR${NC} install $app"
done

echo -e "${GREEN}\n+++ NERD-FONTS +++${NC}\n"
wget -P ~/.fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip
cd ~/.fonts
unzip JetBrainsMono.zip
rm JetBrainsMono.zip
fc-cache -fv

echo -e "${GREEN}\n+++ ALSO CHOOSE NERD-FONTS IN/FOR TREMINAL! +++${NC}\n"
