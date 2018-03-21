#!/bin/bash

src_dir=~/spec2006/benchspec/CPU2006
dest_dir=./
build_dir=build/build_base_arm64_fsl.0000

for file_name in ${src_dir}/*; do
        name_dir=${file_name##*/}
        name_prefix=${name_dir##*.}
        #cp $src_dir/RUN$name_prefix  $file_name
        if [ -d $src_dir/$name_dir/$build_dir ]; then
                mkdir $dest_dir/$name_prefix
                cp -r $src_dir/$name_dir/$build_dir $dest_dir/$name_prefix/
                cp -r $src_dir/$name_dir/data $dest_dir/$name_prefix/
		#echo $name_prefix
        fi
        #echo $name_prefix
done
