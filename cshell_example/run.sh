#!/bin/bash

cd /run/spec2006/perlbench/run/
./perlbench -I./lib checkspam.pl 2500 5 25 11 150     1 1 1 1 >a.out 2>a.err

cd /run/spec2006/povray/run/
./povray SPEC-benchmark-ref.ini

cd /run/spec2006/sjeng/run/
./sjeng ref.txt >a.out 2>a.err

cd /run/spec2006/soplex/run
./soplex -m3500 ref.mps >a.out 2>a.err

cd /run/spec2006/sphinx3/run
./sphinx_livepretend ctlfile . args.an4 >a.out 2>a.err



