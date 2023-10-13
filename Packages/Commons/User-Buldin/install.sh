echo "Paramentro: $1"
for arg in "$@"
do
    case $arg in
        "--on" )
           echo "ON";;
        "--off" )
           echo "OFF";;
        *)
            echo "use: install --off";;
   esac
done