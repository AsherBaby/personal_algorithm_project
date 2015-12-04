datetime=$(date +"%Y%m%d%H%M%S")
HADOOP_HOME=/usr/local/hadoop/
${HADOOP_HOME}bin/hadoop jar ${HADOOP_HOME}contrib/streaming/hadoop-*streaming*.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input word-count/input/* \
-output hadoop-streaming/output-wc_${datetime}/

