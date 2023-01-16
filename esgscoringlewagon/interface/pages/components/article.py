import justpy as jp

class Article(jp.Section):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_classes('text-gray-600 mt-12 overflow-hidden')
        self.div1 = jp.Div(a=self,classes='container px-5 mb-2 mx-auto border-solid rounded border-2 border-indigo-600')
        self.div2 = jp.Div(a=self.div1,classes='my-8 divide-y-2 divide-gray-100')
        self.div3 = jp.Div(a=self.div2,classes='py-8 flex flex-wrap md:flex-nowrap')
        self.div31 = jp.Div(a=self.div3,classes='md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col')
        self.span1 = jp.Span(a=self.div31,classes='font-semibold title-font text-gray-700',text='Category : ENV')
        self.span2 = jp.Span(a=self.div31,classes='font-semibold title-font text-gray-700',text='Score : 0.7')
        self.span3 = jp.Span(a=self.div31,classes='mt-1 text-gray-500 text-sm', text='12 Jun 2019')
        self.div32 = jp.Span(a=self.div3,classes='md:flex-grow')
        self.h2 = jp.H2(a=self.div32,classes='text-2xl font-medium text-gray-900 title-font mb-2',text='Bitters hashtag waistcoat fashion axe chia unicorn')
        self.body = jp.P(a=self.div32,classes='leading-relaxed',text='Glossier echo park pug, church-key sartorial biodiesel vexillologist pop-up snackwave ramps cornhole. Marfa 3 wolf moon party messenger bag selfies, poke vaporware kombucha lumbersexual pork belly polaroid hoodie portland craft beer...')
        self.span4 = jp.Span(a=self.div32,classes='text-blue-500 inline-flex items-center mt-4 mr-4', text='Include : ')
        in1 = jp.Input(type='checkbox',a=self.div32, classes='border block text-blue-500 inline-flex items-center mt-4')
        self.a1 = jp.A(a = self.div32,classes='text-blue-500 inline-flex items-center mt-4 ml-4', text='| Read article')
        
# <section class="text-gray-600 body-font overflow-hidden">
#   <div class="container px-5 py-24 mx-auto">
#     <div class="-my-8 divide-y-2 divide-gray-100">
#       <div class="py-8 flex flex-wrap md:flex-nowrap">
#         <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
#           <span class="font-semibold title-font text-gray-700">CATEGORY</span>
#           <span class="mt-1 text-gray-500 text-sm">12 Jun 2019</span>
#         </div>
#         <div class="md:flex-grow">
#           <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">Bitters hashtag waistcoat fashion axe chia unicorn</h2>
#           <p class="leading-relaxed">Glossier echo park pug, church-key sartorial biodiesel vexillologist pop-up snackwave ramps cornhole. Marfa 3 wolf moon party messenger bag selfies, poke vaporware kombucha lumbersexual pork belly polaroid hoodie portland craft beer.</p>
#           <a class="text-blue-500 inline-flex items-center mt-4">Learn More
#             <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
#               <path d="M5 12h14"></path>
#               <path d="M12 5l7 7-7 7"></path>
#             </svg>
#           </a>
#         </div>
#       </div>
      
#       </div>
#     </div>
#   </div>
# </section>
