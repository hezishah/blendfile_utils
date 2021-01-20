#!/bin/bash

find $1 -name "*.blend" -exec echo -n '"{}" ' \; |xargs python3 /Users/hezishahmoon/Downloads/blenderaid-py-20110211/extractBlendPy.py