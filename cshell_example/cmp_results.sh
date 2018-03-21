#!/bin/bash

# Setup experiment
src_dir=`pwd`
result_dir=result_spec
num_bench=0;
num_correct=0;

# Compare all the result folders

for bench_name in ${src_dir}/*; do
	workload=${bench_name##*/}
	if [ -d $workload ]; then
		#if [ "$workload" = "bzip2" ]; then
		if [ "$workload" != "$result_dir" ]; then
		#if [[ "$workload" = "milc" || "$workload" = "milc" || "$workload" = "namd" || "$workload" = "omnetpp" || "$workload" = "povray" || "$workload" = "perlbench" || "$workload" = "sjeng" || "$workload" = "soplex" || "$workload" = "sphinx3" || "$workload" = "xalancbmk" ]]; then
			cd $src_dir/${workload}
			echo "[compare]" $workload 

			# compare result with ref_result and report
			ref_result_dir=data/ref/output
			run_result_dir=result
			for output_name in ${ref_result_dir}/*; do
				output_file=${output_name##*/}
				if [ -e $run_result_dir/${workload}.ref.$output_file ]; then # exist file
					num_bench=$[$num_bench+1];
					diff $ref_result_dir/$output_file $run_result_dir/${workload}.ref.$output_file > $src_dir/re_tmp.txt
					if test -s $src_dir/re_tmp.txt ; then
				    		echo $output_file run result wrong!
					else
						echo $output_file run result correct!
						num_correct=$[$num_correct+1];
					fi
				fi
			done
			cd ../
		fi
	fi
done
rm $src_dir/re_tmp.txt
echo compare result $num_correct/$num_bench
