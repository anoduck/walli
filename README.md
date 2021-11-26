Walli
=====

A friendly wallpaper changer for your desktop, with a friendly name.
----------------------------------------------------------------------

### Dependencies

You will need to install some additional software for this script to run. They are:

* pywal
* python3(obviously)

### Installation

No installation script has been provided in order to allow users to customize the installation process as much as they desire.

1. Ensure you have satisfied all the requirements listed above. 
2. Either create the directory `$HOME/.config/walli/images` or use the `-d` flag to specify where your directory of wallpaper images are located.
3. Place `walli.py` or rename `walli.py` to `walli` and place somewhere inside your path. If you have a `$HOME/bin` This is preferable.
4. The following needs to be included in your i3 config, ensuring that the path to your python is correct:

```config
exec_always /usr/local/bin/python3.9 ~/bin/walli

```

#### Customization

More configuration options can be discovered by using the `-h` flag.

