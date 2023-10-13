echo "Paramentros: $1 $2 $3"

do
    case $1 in
        "--on" )
           echo "ON";;
        "--off" )
           echo "OFF";;
        *)
            echo "use: install --off";;
   esac
done