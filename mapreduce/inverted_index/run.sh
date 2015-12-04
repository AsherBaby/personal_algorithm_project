datetime=$(date +"%Y%m%d%H%M%S")
HADOOP_HOME=/usr/local/hadoop/
${HADOOP_HOME}bin/hadoop jar ${HADOOP_HOME}contrib/streaming/hadoop-*streaming*.jar \
-file mapper.py -mapper mapper.py \
-input inverted-index/input/* \
-output hadoop-streaming/inverted-index_${datetime}/ \
-numReduceTasks 0
