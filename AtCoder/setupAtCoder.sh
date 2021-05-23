#Usage: [Directory Name] [Problem Name]; problem name is a letter from A to F
#
#Creates a new directory with the given name, with files A, B, C... problem name
#Each has the contents of 'AtCoderTemplate.py'

arr=('A' 'B' 'C' 'D' 'E' 'F')
read -r input
IFS=' '
read -ra arrIN<<<"$input"

dirname="${arrIN[0]}"
lastchar="${arrIN[1]}"

mkdir "$dirname"

i=0
while [ "${arr[$i]}" != "$lastchar" ]
do
  cp AtCoderTemplate.py "${arr[$i]}"".py"
  mv "${arr[$i]}"".py" ./"$dirname"
  i=$((i+1))
done

cp AtCoderTemplate.py "${arr[$i]}"".py"
mv "${arr[$i]}"".py" ./"$dirname"
