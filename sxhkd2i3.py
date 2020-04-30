#!/bin/python

import sys
import os

I3_CONFIG_FILE_PATH = ''.join([os.getenv('XDG_CONFIG_HOME'),'/i3/config'])

# creates a list of keybind objects from i3 config file
def i3configToShortcutList(i3_config_file_path):
    
  i3_shortcut_list = []

  with open(i3_config_file_path) as i3_config_file:

    for line in i3_config_file.read().split('\n'):

      i3_shortcut_list.append(parseShortcut(line, 'i3'))
  
  return i3_shortcut_list
