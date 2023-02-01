
import string
from unidecode import unidecode
from sklearn.base import BaseEstimator,TransformerMixin
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize

class BodyPreprocessor(BaseEstimator,TransformerMixin):
    ''' Preprocessor with multiple options for gridSearchCv
    - remove_stopwords : {True,False}. Can keep stopwords if set to false. Default=True.
    - negation: {'keep','remove'}. Choose to keep or remove (no,not) from text. Default='keep'.
    - numbers: {'keep','remove'}. Choose to keep or remove numbers from the text. Default='keep'.
    - punctuation: {'keep','remove'}. Choose to keep or remove punctuation from the text. Default='remove'.
    - accents: {'keep','remove'}. Choose to keep or remove accents from the text. Default='keep'.
    - html: {'keep','remove'}. Choose to keep or remove html tags from the text. Default='keep'.
    - lemma: {True, False}. Choose to lemmatize or not. Default=False.
    - stem: {True, False}. Choose to stem or not. Default=False.
    '''
    def __init__(self,remove_stopwords=True,negation = 'keep',numbers='remove',punctuation='remove',accents='keep', html='keep',lemma=False, stem=True):
        
        self.negation_list = ['no','not']
        self.remove_stopwords = remove_stopwords
        self.numbers = numbers
        self.html = html
        self.accents = accents
        self.lemma = lemma
        self.stem = stem
        self.punctuation = punctuation
        self.negation = negation
        if self.negation == 'keep' :
            self.stop_words = [word for word in stopwords.words('english') if word not in self.negation_list]
        if self.negation == 'remove' :
            self.stop_words ==  stopwords.words('english')
        
        
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        
        if self.numbers == 'remove':
            X = X.replace(r'\d+', '')
           
        if self.punctuation == 'remove':
            X = X.translate(str.maketrans('', '', string.punctuation))
            
        if self.html == 'remove':
            X = X.replace(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});','')
           
        if self.lemma :
            self.lemmatizer = WordNetLemmatizer()
            X = ' '.join([self.lemmatizer.lemmatize(word) for word in X.split()])
           
        if self.stem :
            self.stemmer = PorterStemmer()
            X = ' '.join([self.stemmer.stem(word) for word in X.split()])    
              
        
        if self.remove_stopwords:
            X = ' '.join([word for word in word_tokenize(X) if word.lower() not in self.stop_words])
            

        if self.accents == 'remove':
            X = unidecode(X)
            
        return X


class DataFramePreprocessor(BaseEstimator,TransformerMixin):
    ''' Preprocessor with multiple options for gridSearchCv
    - remove_stopwords : {True,False}. Can keep stopwords if set to false. Default=True.
    - negation: {'keep','remove'}. Choose to keep or remove (no,not) from text. Default='keep'.
    - numbers: {'keep','remove'}. Choose to keep or remove numbers from the text. Default='keep'.
    - punctuation: {'keep','remove'}. Choose to keep or remove punctuation from the text. Default='remove'.
    - accents: {'keep','remove'}. Choose to keep or remove accents from the text. Default='keep'.
    - html: {'keep','remove'}. Choose to keep or remove html tags from the text. Default='keep'.
    - lemma: {True, False}. Choose to lemmatize or not. Default=False.
    - stem: {True, False}. Choose to stem or not. Default=False.
    '''
    def __init__(self,remove_stopwords=True,negation = 'keep',numbers='remove',punctuation='remove',accents='keep', html='keep',lemma=False, stem=True):
        
        self.negation_list = ['no','not']
        self.remove_stopwords = remove_stopwords
        self.numbers = numbers
        self.html = html
        self.accents = accents
        self.lemma = lemma
        self.stem = stem
        self.punctuation = punctuation
        self.negation = negation
        if self.negation == 'keep' :
            self.stop_words = [word for word in stopwords.words('english') if word not in self.negation_list]
        if self.negation == 'remove' :
            self.stop_words ==  stopwords.words('english')
        
        
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        
        if self.numbers == 'remove':
            X['sentence'] = X['sentence'].str.replace(r'\d+', '', regex=True)
           
        if self.punctuation == 'remove':
            X['sentence'] = X['sentence'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
            
        if self.html == 'remove':
            X['sentence'] = X['sentence'].str.replace(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});','', regex=True)
           
        if self.lemma :
            self.lemmatizer = WordNetLemmatizer()
            X['sentence'] = X['sentence'].apply(lambda  x: ' '.join([self.lemmatizer.lemmatize(word) for word in x.split()]))
           
        if self.stem :
            self.stemmer = PorterStemmer()
            X['sentence'] = X['sentence'].apply(lambda x: ' '.join([self.stemmer.stem(word) for word in x.split()]))    
              
        
        if self.remove_stopwords:
            X['sentence'] = X['sentence'].apply(lambda x: ' '.join([word for word in word_tokenize(x) if word.lower() not in self.stop_words]))
            

        if self.accents == 'remove':
            X['sentence'] = X['sentence'].apply(lambda x: unidecode(x))
            
        return X['sentence'].values

