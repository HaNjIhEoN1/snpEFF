# open snpEff database and find target organism
java -jar snpEff.jar databases
java -jar snpEff.jar databases | grep [organism]

# case 1 if your target organism is exist in data base
java -jar snpEff.jar download -v [organism]
java -Xmx4g -jar snpEff.jar -v [organism] input.vcf > output.ann.vcf

# case 2 if your target organism is not exist in data base
java -jar snpEff.jar -interval sacCer_features.gff sacCer my.vcf > my.ann.vcf
