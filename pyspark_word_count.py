from pyspark.sql import SparkSession

def word_count(input_file, output_dir):
    # Create a SparkSession (Note, the config section is only for Windows!)
    spark = SparkSession.builder \
        .appName("PythonWordCount") \
        .getOrCreate()

    # Read data and create an RDD from the text file
    text_file = spark.sparkContext.textFile(input_file)

    # Perform the word count
    counts = text_file.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)

    # Save the counts to output
    counts.saveAsTextFile(output_dir)

    # Stop the SparkSession
    spark.stop()


if __name__ == "__main__":
    input_file = 's3://awsbucket1-stevensonch/bios.txt'  # Replace with your input file path
    output_dir = 's3://awsbucket1-stevensonch/bios_output'  # Replace with your desired output directory

    word_count(input_file, output_dir)
