from lxml import html #import librarie
import requests #import librarie
import xlrd, xlwt #import librarie
def directory():
    userchoice = int(input("\nPlease type the number appropriate to your wanted function, select 0 for all available functions"))
    if userchoice == 0:
        print("Select 1 to find up to date individual stock information")
        print("Select 2 to view your portfolio")
        usermenupick(int(input("Select a function")))
    else:
        usermenupick(userchoice)

def usermenupick(value):
    if value == 1:
        initialsearch = str(input("\nWhat is the name of the company?"))
        gosearch(initialsearch)
    elif value == 2:
        print("Function is in Development")

def Search(stockticker): # definiton of seach function
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0',
    })
    print('Stock ticker: ', stockticker)
    url = ("https://finance.yahoo.com/quote/%s" % stockticker)
    print(url)
    urlopen = requests.get(url, headers = headers)
    tree = html.fromstring(urlopen.content, "lxml")
    price = tree.xpath('//span[@class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]/text()')
    #description = tree.xpath('//p[@class="description__text"]/text()')
    day_low = tree.xpath('//span[@class="Trsdu(0.3s) "]/text()')
    low_high = tree.xpath('//td[@class="Ta(end) Fw(b) Lh(14px)"]/text()')
    #print('Description: ', description)
    print('Current stock price: $',price[0])
    print('Open stock price: $', day_low[1])
    print("Today's high and low prices: Low", low_high[0], 'High')

def portfolio():
    pf = xlwt.Workook()
    pfdata = pf.add_sheet("Stock Names")
    book.save("porfoliobase.xlsx")

def gosearch(a):
    usersearch = a.title()
    print(usersearch)
    workbook = xlrd.open_workbook('CompanyFile.xlsx', on_demand=True)
    worksheet = workbook.sheet_by_index(0)
    i = 0
    g = 0
    counter = 0
    for i in range(worksheet.nrows):
        if usersearch in worksheet.cell(i,1).value:
            try:
                ticker = worksheet.cell_value(i,0)
                print("Your company is: ", worksheet.cell_value(i,1))
                Search(ticker)
            except:
                print("hello")
                #str(input("\nWhat is the name of the company?"))
        else:
            counter += 1
        if counter == 3312:
            print("Company not found")
while 1 == 1:
    directory()

##def newportfolio():
##    name = input("Name your new portfolio")
##    porfolio = []
##    wallet = int(input("Enter your initial investment amount"))
##    def addcompany():
##        newcompany = input("Enter company name")
##        portfolio.append(name)
##        #search(name)
##        return portfolio
##    return portfolio
##def showportfolio():
##    #ALEC IS DOING THIS
##    #ART STUFF TO DISPLAY THE USERS PORTFOLIO
##    #USER SHOULD BE ABLE TO SELECT BEWTWEEN ALL THEIR PORFOLIOS
##    
##def userportfolio(portfolio):
##    for name in portfolio: 

    
