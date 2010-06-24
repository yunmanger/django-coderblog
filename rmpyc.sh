#!/bin/bash

rm *.pyc
rm */*/*.pyc
git rm -- `git ls-files --deleted` 
