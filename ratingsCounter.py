# This program can be run in interactive shell
# or can be submitted from the command line using 'spark-submit ratingsCounter.py'
# where ratingsCounter.py contains the contents of this file

from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("RatingsCount")
sc = SparkContext(conf = conf)

# Interactive session can start from here,
# sc (SparkContext object)  is already provided for us in the interactive shell

lines = sc.textFile("/wsu/ratings.csv")
type(lines) # what data type do you see?

# to remove the header line, first get the header and then filter it out
headerline = lines.first()
linesWithoutHeader = lines.filter(lambda x: x != headerline)

# Get the ratings column values - the third column that is the index number 2
ratings = linesWithoutHeader.map(lambda x: x.split(",")[2])
# The above statement returns quickly as it is not doing anything at this time as it is LAZY

result = ratings.countByValue()
# CountByValue is an action call, This will kickstart the map process from the previous line

print(result)
sorted_results = sorted(result.items())

for key, value in sorted_results:
    print(" {}   {}".format(key,value))