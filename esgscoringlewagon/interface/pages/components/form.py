import justpy as jp

# <section class="text-gray-600 body-font">
#   <div class="container px-5 py-24 mx-auto">
#     <div class="flex flex-col text-center w-full mb-12">
#       <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Master Cleanse Reliac Heirloom</h1>
#       <p class="lg:w-2/3 mx-auto leading-relaxed text-base">Whatever cardigan tote bag tumblr hexagon brooklyn asymmetrical gentrify, subway tile poke farm-to-table. Franzen you probably haven't heard of them man bun deep.</p>
#     </div>
#     <div class="flex lg:w-2/3 w-full sm:flex-row flex-col mx-auto px-8 sm:space-x-4 sm:space-y-0 space-y-4 sm:px-0 items-end">
#       <div class="relative flex-grow w-full">
#         <label for="full-name" class="leading-7 text-sm text-gray-600">Full Name</label>
#         <input type="text" id="full-name" name="full-name" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-transparent focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
#       </div>
#       <div class="relative flex-grow w-full">
#         <label for="email" class="leading-7 text-sm text-gray-600">Email</label>
#         <input type="email" id="email" name="email" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-transparent focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
#       </div>
#       <button class="text-white bg-blue-500 border-0 py-2 px-8 focus:outline-none hover:bg-blue-600 rounded text-lg">Button</button>
#     </div>
#   </div>
# </section>

class Form(jp.Section):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_classes('text-gray-600')
        self.div1 = jp.Div(a=self,classes='container px-5 py-24 mx-auto')
        self.div11 = jp.Div(a=self.div1,classes='flex flex-col text-center w-full mb-12')
        self.p1 = jp.P(a=self.div11,classes='lg:w-2/3 mx-auto leading-relaxed text-base',text= 'Choose a company and a time period for analysis')
        self.div12 = jp.Div(a=self.div1,classes='flex lg:w-2/3 w-full sm:flex-row flex-col mx-auto px-8 sm:space-x-4 sm:space-y-0 space-y-4 sm:px-0 items-end')
        self.div121 = jp.Div(a=self.div12,classes='relative flex-grow w-full')
        input_classes = 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-transparent focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
        self.start_date = jp.Input(a=self.div121, classes=input_classes, placeholder='Start Date')
        self.div122 = jp.Div(a=self.div12,classes='relative flex-grow w-full')
        self.end_date = jp.Input(a=self.div122, classes=input_classes, placeholder='End Date')
        self.div123 = jp.Div(a=self.div12,classes='relative flex-grow w-full')
        self.company = jp.Input(a=self.div123, classes=input_classes, placeholder='Company Name')
        self.submit = jp.Button(a=self.div12,classes='text-white bg-blue-500 border-0 py-2 px-8 focus:outline-none hover:bg-blue-600 rounded text-lg',text='Analyze')
