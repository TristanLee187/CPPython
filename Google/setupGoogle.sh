#Usage: [Platform name] [Directory Name] [Problem Name]; problem name is a letter from A to F
#
#Creates a new directory with the given name, with files A, B, C... problem name,
# in the specified platform directory
#Each has the contents of 'Template.py'

arr=('A' 'B' 'C' 'D' 'E' 'F')
read -r input
IFS=' '
read -ra arrIN<<<"$input"

platname="${arrIN[0]}"
year="${arrIN[1]}"
dirname="${arrIN[2]}"
lastchar="${arrIN[3]}"

mkdir "$dirname"

i=0
while [ "${arr[$i]}" != "$lastchar" ]
do
  cp Template.py "${arr[$i]}"".py"
  mv "${arr[$i]}"".py" ./"$dirname"
  i=$((i+1))
done

cp Template.py "${arr[$i]}"".py"
mv "${arr[$i]}"".py" ./"$dirname"
mv ./"$dirname" ./"$platname"/"$year"
