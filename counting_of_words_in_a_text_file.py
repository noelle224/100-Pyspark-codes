# -*- coding: utf-8 -*-
"""Counting of words in a text file

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jVrLPKUiltHlpuabTKRp6V4-6ZO6-L35
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()

class wordCount:
  def __init__(self):
    self.file_path = '/content/Lady Lazarus BY SYLVIA PLATH.txt'

  def read_file(self):
    lines = spark.read.text(self.file_path)
    rdd_lines = lines.rdd.map(lambda row: row.value)
    return rdd_lines

  def flapmapping(self, rdd_lines):
    rdd_array = rdd_lines.flatMap(lambda line: line.split(" "))
    return rdd_array

  def reducekey(self, rdd_array):
    rdd_array = rdd_array.map(lambda word: (word, 1))
    rdd_array = rdd_array.reduceByKey(lambda a, b: a + b)
    return rdd_array

  def create_dataframe(self, rdd_array):
    worddf = spark.createDataFrame(rdd_array, ['word', 'counting'])
    return worddf

  def top5(self, worddf):
    max_word = worddf.orderBy(desc(col('counting'))).limit(5)
    return max_word


countob = wordCount()
rdd_lines = countob.read_file()
rdd_array = countob.flapmapping(rdd_lines)
rdd_array = countob.reducekey(rdd_array)
worddf = countob.create_dataframe(rdd_array)
worddf = countob.top5(worddf)
worddf.show()