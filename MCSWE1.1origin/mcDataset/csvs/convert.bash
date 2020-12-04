for value in {0..1200}
do
    sed -i 's/1/0/g' label$value.csv
    sed -i 's/2/1/g' label$value.csv
done

echo All done
