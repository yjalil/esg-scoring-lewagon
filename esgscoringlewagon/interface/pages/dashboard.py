import justpy as jp

from components.article import Article

class Dashboard(jp.Section):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.article = Article()
        
        