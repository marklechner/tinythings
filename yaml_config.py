#!/usr/local/bin/python3

# dynamic config parser model for YAML based CMDB

import yaml

class Config():
  def __init__(self, config_file):
    self.config_file = config_file
    with open(config_file, 'r') as yamlfile:
      self.cfg = yaml.load(yamlfile)

  def get_config(self, *args):
    self.data = []
    for arg in args:
      self.data.append(self.cfg[arg])
    return self.data

conf = Config("samples/config.yaml")

song, artist, tags = conf.get_config("song","artist","tags")

print(song, artist, tags)
