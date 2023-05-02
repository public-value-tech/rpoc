#!/bin/sh
gen-project -d rpoc rpoc.yaml
gen-yuml -d . rpoc.yaml -f svg --diagram-name rpoc