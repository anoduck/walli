Walli
=====

A wallpaper changer of sorts.
-----------------------------

I totally ripped the idea for this from another user of github, and frankly, I cannot remember who that person was. So, in advance, thanks bud.


### Dependencies

You will need to install some additional software for this script to run. They are:

* hsetroot
* pywal
* python(obviously)
* bash
* Dual Monitors

### Installation

Installation of Walli is accomplished through the installation script `install.sh`. After installation the script `run.sh` needs to be configured to fit your tastes, and finally a few lines of code need to be added to your i3 configuration file.

#### Prerequisites

1. The first thing that needs to be handled is locating the path `env` for your system. This is often found in `/usr/bin/env` and `/usr/env`. Once located this path needs to compared with the first line of the installation script `#!/usr/bin/env bash`. The path of env for your system and the path for env used in the configuration script must be the same.
2. Finally, make the install script executable. `chmod +x install.sh`
3. Before running the installation script, make sure that `$home/bin` exists, is writable, and is located within your `$PATH`. If not, make it so. `mkdir -p ~/bin && chmod -R 755 ~/bin && echo "export PATH=$PATH:$HOME/bin >> ~/.bashrc"` If using zsh, use `zshrc` instead of `bashrc`, you know.
4. Simply run `install.sh`, the installation script. This will install walli to `$home/bin/walli` and the other required files to `$HOME/.config/walli`. Images that you want displayed as wallpaper/backgrounds need to be copied to `$HOME/config/walli/images` or change the `run.sh` script to fit your tastes. 


#### I3 Configuration

The following needs to be included in your i3 config:

```config
exec_always --no-startup-id hsetroot -screens0 -cover ~/.config/walli/background1
exec_always --no-startup-id hsetroot -screens1 -cover ~/.config/walli/background2
exec_always --no-startup-id wal -c -g -i ~/.config/walli -a 70 -o ~/.config/walli/run.sh
exec_always --no-startup-id bash ~/.config/walli/run.sh

```
