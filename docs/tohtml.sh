#!/usr/bin/bash
pandoc -s --metadata title="420-951-VA Transaction Web Applications" --mathjax -c github.css "$1".md -o "$1".html

