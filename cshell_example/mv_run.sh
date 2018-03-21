#!/bin/bash

dst_dir=.
src_dir=../spec2006_x86

for bench_name in ${src_dir}/*; do
	workload=${bench_name##*/}
	if [ -d $workload ]; then
		if [ "$workload" != "$result_dir" ]; then
			cp $src_dir/$workload/run.sh $dst_dir/$workload/run.sh
			#echo $src_dir/$workload/run.sh
			#echo $dst_dir/$workload/run.sh
		fi
	fi

done
