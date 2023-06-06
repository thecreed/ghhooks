#!/bin/env python3

from json import dumps
from sys import argv
import os
from pprint import pprint
from utils import get_logger,load_conf,conf_yaml

logger = get_logger()

os.system("./tools/create_artifacts.sh %s"  %(conf_yaml['host']))