# SETUPPC - TODO

## Info

It's a good idea to configure Git to use SSH for pushing (uploading) and HTTPS for pulling (downloading), use Git's insteadOf and pushInsteadOf configuration options.

```git config --global url."https://github.com/".insteadOf git@github.com:```

```git config --global url."git@github.com:".pushInsteadOf https://github.com/```

## Latex and vimtex (\ll)

install TexLive

`sudo pacman -S texlive-meta`

install TexLive "Full"

`sudo pacman -S texlive-basic texlive-latexextra texlive-fontsrecommended texlive-fontsextra texlive-langgerman texlive-luatex texlive-bibtexextra texlive-pictures biber`

install zathura for pdf preview ()

`sudo pacman -S zathura zathura-pdf-poppler`

add magic comment to .tex file to force lualatex

`%! TeX program = lualatex`

## allow "localsend" in firewall

```sudo ufw allow 53317/tcp```

```sudo ufw allow 53317/udp```

