#!/bin/sh

declare -a num_As
declare -a num_Bs
python_script="./probset6.py"
testNum=1
num_As=(2 4 7 9)
num_Bs=(2000000 200000 20000 2000)
for num_A in ${num_As[@]}
do
for num_B in ${num_Bs[@]}
do
mkdir "./test_result_$testNum"
folder="./test_result_$testNum"
echo -e "This is experiment for setting num_A is $num_A and num_B is $num_B" > $folder"/README.md"

#uniform test
python $python_script --num_A $num_A --num_B $num_B --data_generator uniform_generator --result_path $folder"/result_uniform.csv"

#exponential test
python $python_script --num_A $num_A --num_B $num_B --data_generator exponential_generator --result_path $folder"/result_exponential.csv"

#real world data test
python $python_script --num_A $num_A --num_B $num_B --data_generator real_world_data_generator --real_world_data_input "./shakespeare.txt" --result_path $folder"/result_real_world.csv"

testNum=$(expr $testNum + 1)
done
done




