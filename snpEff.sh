# open snpEff database and find target organism
java -jar snpEff.jar databases
java -jar snpEff.jar databases | grep [organism]

# case 1 if your target organism is exist in data base
java -jar snpEff.jar download -v [organism]
java -Xmx4g -jar snpEff.jar -v [organism] input.vcf > output.ann.vcf

# case 2 if your target organism is not exist in data base
cd ~/snpEff
mkdir data/[organism]
cd data/[organism]
wget [organism feature gff]
mv [organism feature gff] gene.gff
cd ../..
echo '[organism.genome] : [organism]' >> snpEff.config
java -Xmx1G -jar snpEff.jar build -gff3 [organism]
java -jar snpEff.jar -interval [organism].gff [organism] my.vcf > my.ann.vcf
