# 💤 LazyVim

A starter template for [LazyVim](https://github.com/LazyVim/LazyVim).
Refer to the [documentation](https://lazyvim.github.io/installation) to get started.

# install requirements
**simple run:**
```sh
sudo ./install_requirements.sh
```
**or**
<details><summary>install manual</summary>


### install neovim (apt)



also see official [nvim-site](https://github.com/neovim/neovim/blob/master/INSTALL.md#ubuntu)

```sh
sudo add-apt-repository ppa:neovim-ppa/unstable
sudo apt update
sudo apt install neovim
```


### recommended apps

Also see official [LazyVim-site](https://www.lazyvim.org/#%EF%B8%8F-requirements)

- install rg, curl, fzf and co
```sh
sudo apt install curl git fzf ripgrep fd-find
```

- install nerdfonts (also choose in/for treminal)
```sh
wget -P ~/.fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip
cd ~/.fonts
unzip JetBrainsMono.zip
rm JetBrainsMono.zip
fc-cache -fv
```

</details>

# install LazyVim

- (optional) save neovim files:

  ```sh
  mv ~/.config/nvim ~/.config/nvim.bak
  mv ~/.local/share/nvim ~/.local/share/nvim.bak
  ```

- clone starter:

  ```sh
  git clone git@gitlab.com:dog42/lazyvim.git ~/.config/nvim  
  ```
  OR
  ```sh
  git clone https://gitlab.com/dog42/lazyvim.git ~/.config/nvim
  ```


- run neovim!

  ```sh
  nvim
  ```
