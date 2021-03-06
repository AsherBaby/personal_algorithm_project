datetime=$(date +"%Y%m%d%H%M%S")
HADOOP_HOME=/usr/local/hadoop/
hadoop jar ${HADOOP_HOME}contrib/streaming/hadoop-*streaming*.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input anagrams/input/* \
-output hadoop-streaming/anagrams_${datetime}/

