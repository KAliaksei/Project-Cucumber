from lxml import html #import librarie
import requests #import librarie
import xlrd, xlwt #import librarie
def directory():
    userpick = int(input("Please type the number appropriate to your wanted function, select 0 for all available functions"))
    if userpick == 0:
        print("Select 1 to find up to date individual stock information")
        print("Select 2 to view your portfolio")
        userpick = int(input("Select a function"))
    if userpick == 1:
        initialsearch = str(input("\nWhat is the name of the company?"))
        gosearch(initialsearch)
    elif userpick == 2:
        print("Function is in Development")

def Search(stockticker): # definiton of seach function
    print('Stock ticker: ', stockticker)
    url = ("https://www.marketwatch.com/investing/stock/%s" % stockticker)
    urlopen = requests.get(url)
    tree = html.fromstring(urlopen.content)
    price = tree.xpath('//span[@class="last-value"]/text()')
    description = tree.xpath('//p[@class="description__text"]/text()')
    low_high = tree.xpath('//span[@class="kv__value kv__primary "]/text()')
    print('Description: ', description[0])
    print('Current stock price: $',price[0])
    print('Open stock price: $', low_high[0])
    print("Today's high and low prices: Low", low_high[1], 'High')
def portfolio():
    pf = xlwt.Workook()
    pfdata = pf.add_sheet("Stock Names")
    book.save("porfoliobase.xlsx")

def gosearch(a):
    usersearch = a.title()
    print(usersearch)
    workbook = xlrd.open_workbook('testcompanylist.csv.xlsx', on_demand = True)
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
                print("This company is not in our database or you are attempting to view the market outside of trading hours.")
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

    
