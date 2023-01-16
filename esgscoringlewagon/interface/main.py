import justpy as jp

from layout.header import Header
from pages.components.article import Article
from pages.components.companyProfile import CompanyProfile
from pages.components.scoreSeries import ScoreSeries
from pages.components.form import Form

def app():
    wp = jp.WebPage()
    Header(a=wp)
    Form(a=wp)
    CompanyProfile(a=wp)
    ScoreSeries(a=wp)
    for i in range(5):
        Article(a=wp)
    
   
    return wp

if __name__=='__main__':
    jp.justpy(app)
