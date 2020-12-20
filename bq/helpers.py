#!/bin/python3
#Author: ashwinmishra
#Last revised: 12/20/20

'''
This file hosts a set of bq functions found helpful for data analysis.
'''

from google.cloud import bigquery

def bq_to_df(query):
    '''
    Input: query in text
    Output: pandas dataframe
    Description: Function that converts bq query into df
    Example: df = bq_to_df(sql)
    '''
    df = bigquery.Client().query(query).to_dataframe()
    return df

def parameterized_bq(query, column_name):
    '''
    Input: query in txt but with a {0} for the parameter name in bq, this can be adjusted.
    Output: pandas dataframe
    Description: Function that converts bq query into df
    Example query: SELECT {0}, COUNT(1) AS num_babies, AVG(weight_pounds) AS avg_wt FROM publicdata.samples.natality WHERE year > 2000 GROUP BY {0}"""
    '''
    sql = query.format(column_name)
    return bigquery.Client().query(sql).to_dataframe()
