#!/bin/sh
gen-project -d rpoc rpoc.yaml
mkdir -p rpoc/typescript
gen-typescript rpoc.yaml > rpoc/typescript/rpoc.ts
gen-yuml -d . rpoc.yaml -f svg --diagram-name rpoc
# rename -f 'y/A-Z/a-z/' Rpoc*