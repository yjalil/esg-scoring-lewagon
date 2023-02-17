import requests
import zipfile
import io
import pandas as pd
import time
import os
import re
import trafilatura
import numpy as np
from datetime import date

def range_dates():
    start_date = date.today()
    end_date = date.today()
    return  pd.date_range(start=start_date, end=end_date, freq='D')

def gdelt_columns():
    list_columns = 'GLOBALEVENTID	SQLDATE	MonthYear	Year	FractionDate	Actor1Code	Actor1Name	Actor1CountryCode	Actor1KnownGroupCode	Actor1EthnicCode	Actor1Religion1Code	Actor1Religion2Code	Actor1Type1Code	Actor1Type2Code	Actor1Type3Code	Actor2Code	Actor2Name	Actor2CountryCode	Actor2KnownGroupCode	Actor2EthnicCode	Actor2Religion1Code	Actor2Religion2Code	Actor2Type1Code	Actor2Type2Code	Actor2Type3Code	IsRootEvent	EventCode	EventBaseCode	EventRootCode	QuadClass	GoldsteinScale	NumMentions	NumSources	NumArticles	AvgTone	Actor1Geo_Type	Actor1Geo_FullName	Actor1Geo_CountryCode	Actor1Geo_ADM1Code	Actor1Geo_Lat	Actor1Geo_Long	Actor1Geo_FeatureID	Actor2Geo_Type	Actor2Geo_FullName	Actor2Geo_CountryCode	Actor2Geo_ADM1Code	Actor2Geo_Lat	Actor2Geo_Long	Actor2Geo_FeatureID	ActionGeo_Type	ActionGeo_FullName	ActionGeo_CountryCode	ActionGeo_ADM1Code	ActionGeo_Lat	ActionGeo_Long	ActionGeo_FeatureID	DATEADDED	SOURCEURL'
    return list_columns

def nasdaq_companies():
    with open('dicts/list_nasdaq100.txt','r') as cfile:
        lst_companies = [line.rstrip() for line in cfile]
    return lst_companies

def get_csv(date):
    r = requests.get(f"http://data.gdeltproject.org/events/{date}.export.CSV.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(f"./Data/{date}")
    
def filter_csv(date):
    df_articles = pd.read_csv(f'Data/{date}/{date}.export.CSV',sep='\t', header=None, low_memory=False)
    df_articles.columns = gdelt_columns().split('\t')
    df_articles = df_articles[(df_articles['Actor1Name']=='COMPANY')  | (df_articles['Actor1Name']=='COMPANY')]
    return df_articles[['SQLDATE','SOURCEURL']].values.tolist()

def get_urls(range_dates):
    lst_urls_in_range_dates = []
    try :   
        for date in range_dates:
            str_date = date.strftime('%Y%m%d')
            get_csv(date.strftime('%Y%m%d'))
            lst_urls_in_date = filter_csv(str_date)
            lst_urls_in_range_dates = lst_urls_in_range_dates + lst_urls_in_date
            os.remove(f'Data/{str_date}/{str_date}.export.CSV')
            os.rmdir(f'Data/{str_date}')
        return lst_urls_in_range_dates
    except :
        with open('error_log.txt','a') as efile:
            efile.write('error on date : ' + date.strftime('%Y%m%d') + '\n')
            
def nasdaq_filter(url):
    for substring in nasdaq_companies() :
        if substring.strip().lower() in url.replace('-',' ') :
            return substring
    return 'None'

def parse_title_from_url(url):
   lst = url.split('/')
   title = max(lst, key = len)
   m = re.findall('(.*).', title)
   return m[-1].replace('-',' ')

def scrape_body_from_url(url):
    body =trafilatura.fetch_url(url)
    if body :
        return trafilatura.extract(body)
    return 'None'

def build_df():
    df = pd.DataFrame(get_urls(range_dates()),columns=['date','sourceURL'])
    df.drop_duplicates(inplace=True, ignore_index=True)
    df['company'] = df['sourceURL'].apply(nasdaq_filter)
    df = df[df['company']!='None']
    df['title'] = df['sourceURL'].apply(parse_title_from_url)
    df['body'] = df['sourceURL'].apply(scrape_body_from_url)
    df = df[df['body']!='None']
    return df
    