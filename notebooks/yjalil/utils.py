import pandas as pd

def combine_labels(df):
    df_copy = df.copy()
    df_copy['combined_label'] = df_copy['topic_label'] + df_copy['sentiment_label']
    return df_copy
