#!/bin/bash

# Setup experiment
correctness_flag=1
src_dir=`pwd`
result_dir=result_spec
mkdir -p $result_dir
experiment=baseline
current_time=`date +%b%d_%Hh%Mm`

num_bench=0
num_correct=0
cd $result_dir
mkdir -p ${experiment}_${current_time}
cd ../

# Run multiple iterations of specbench (let's limit it by two to save some simulation time
for num in $( seq 1 1 )
do

	for bench_name in ${src_dir}/*; do
		workload=${bench_name##*/}
		if [ -d $workload ]; then
			if [[ "$workload" != "$result_dir" && "$workload" != "gcc" && "$workload" != "perlbench" && "$workload" != "sphinx3" ]]; then
			#if [ "$workload" != "$result_dir" ]; then
			#if [ "$workload" = "astar" ]; then
				cd $src_dir/${workload}
				echo "[run]" $workload iteration $num
				
				(/usr/bin/time -v ./run.sh) &> $src_dir/$result_dir/${experiment}_${current_time}/${workload}_${num}.txt  
				sleep 1;

				# compare result with ref_result and report
				ref_result_dir=data/ref/output
				run_result_dir=result
				if [ "$workload" = "povray" ]; then
					mv run/SPEC-benchmark.tga $run_result_dir/povray.ref.SPEC-benchmark.tga
				fi
				if [ "$workload" = "mcf" ]; then
				    mv run/mcf.out $run_result_dir/mcf.ref.mcf.out
				fi
				for output_name in ${ref_result_dir}/*; do
					output_file=${output_name##*/}
					if [ -e $run_result_dir/${workload}.ref.$output_file ]; then
						num_bench=$[$num_bench+1];
						diff $ref_result_dir/$output_file $run_result_dir/${workload}.ref.$output_file > $src_dir/re_tmp.txt
						if test -s $src_dir/re_tmp.txt; then
					    		echo $output_file run result wrong!
							correctness_flag=0
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
	echo compare result $num_correct/$num_bench
	# compare result with ref_result and report
	if [ $correctness_flag -eq 1 ]; then
		echo iteration $num result all correct! >> $src_dir/$result_dir/${experiment}_${current_time}/compare.txt
	fi
done
rm $src_dir/re_tmp.txt
echo benchmark running completed
