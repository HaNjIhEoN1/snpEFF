# snpEff
Genetic variant annotation and functional effect prediction toolbox. It annotates and predicts the effects of genetic variants on genes and proteins (such as amino acid changes).

[manual](https://pcingola.github.io/SnpEff/)
[manual(kor)](https://korbillgates.tistory.com/61)

## Index
1. Install Java
2. Install snpEff
3. In Linux shell 

## 1. Install Java
    1. apt-get update
  

    2. sudo apt-get install openjdk-8-jdk


    3. which javac  or  readlink -f /usr/bin/javac # javac path
    
    4. sudo vi /etc/oprofile
        add export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
            export PATH=$JAVA_HOME/bin/:$PATH
            export CLASS_PATH=$JAVA_HOME/lib:$CLASS_PATH
            
    5. source /etc/profile
        echo $JAVA_HOME

## 2. Install snpEff
    1. wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip
    
    2. unzip snpEff_latest_core.zip
