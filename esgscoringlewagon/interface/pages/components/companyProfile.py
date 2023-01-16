import justpy as jp

class CompanyProfile(jp.Section):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_classes('text-gray-600')
        self.div1 = jp.Div(a=self, classes = 'container px-5 mx-auto')
        self.h1 = jp.H1(a=self.div1,classes='flex flex-wrap -m-4 text-center title-font font-medium sm:text-5xl text-4xl p-4',text='CompanyName')
        self.div11 = jp.Div(a=self.div1, classes = 'flex flex-wrap -m-4 text-center')
        self.div111 = jp.Div(a=self.div11, classes = 'p-4 sm:w-1/4 w-1/2')
        self.h2_1 = jp.H2(a=self.div111,classes = 'title-font font-medium sm:text-4xl text-3xl text-gray-900',text='9.8')
        self.p1 = jp.P(a=self.div111,classes='leading-relaxed',text='Enviroment')
        self.div112 = jp.Div(a=self.div11, classes = 'p-4 sm:w-1/4 w-1/2')
        self.h2_2 = jp.H2(a=self.div112,classes = 'title-font font-medium sm:text-4xl text-3xl text-gray-900',text='6.5')
        self.p2 = jp.P(a=self.div112,classes='leading-relaxed',text='Social')
        self.div113 = jp.Div(a=self.div11, classes = 'p-4 sm:w-1/4 w-1/2')
        self.h2_3 = jp.H2(a=self.div113,classes = 'title-font font-medium sm:text-4xl text-3xl text-gray-900',text='7.2')
        self.p3 = jp.P(a=self.div113,classes='leading-relaxed',text='Governance')
        self.div114 = jp.Div(a=self.div11, classes = 'p-4 sm:w-1/4 w-1/2')
        self.h2_4 = jp.H2(a=self.div114,classes = 'title-font font-medium sm:text-4xl text-3xl text-gray-900',text='8.3')
        self.p4 = jp.P(a=self.div114,classes='leading-relaxed',text='ESG')


# <section class="text-gray-600 body-font">
#   <div class="container px-5 py-24 mx-auto">
#     <div class="flex flex-wrap -m-4 text-center">
#       <div class="p-4 sm:w-1/4 w-1/2">
#         <h2 class="title-font font-medium sm:text-4xl text-3xl text-gray-900">2.7K</h2>
#         <p class="leading-relaxed">Users</p>
#       </div>
#       <div class="p-4 sm:w-1/4 w-1/2">
#         <h2 class="title-font font-medium sm:text-4xl text-3xl text-gray-900">1.8K</h2>
#         <p class="leading-relaxed">Subscribes</p>
#       </div>
#       <div class="p-4 sm:w-1/4 w-1/2">
#         <h2 class="title-font font-medium sm:text-4xl text-3xl text-gray-900">35</h2>
#         <p class="leading-relaxed">Downloads</p>
#       </div>
#       <div class="p-4 sm:w-1/4 w-1/2">
#         <h2 class="title-font font-medium sm:text-4xl text-3xl text-gray-900">4</h2>
#         <p class="leading-relaxed">Products</p>
#       </div>
#     </div>
#   </div>
# </section>
