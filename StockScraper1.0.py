from lxml import html #import librarie
import requests #import librarie
import xlrd, xlwt #import librarie
from openpyxl import *
def directory():
    intitialportfolio()
    try:
        userchoice = int(input("\nPlease type the number appropriate to your wanted function, select 0 for all available functions"))
        if userchoice == 0:
            print("Select 1 to find up to date individual stock information")
            print("Select 2 to view your portfolio")
            usermenupick(int(input("Select a function")))
        else:
            usermenupick(userchoice)
    except:
        print("Invalid input")

def usermenupick(value):
    if value == 1:
        initialsearch = str(input("\nWhat is the name of the company?"))
        gosearch(initialsearch)
    elif value == 2:
        myportfolio()
        print("Your current portfolio is:", portfolio)
        userchoice = int(input(" Select 1 - To add a company to your portfolio\n "
                               "Select 2 - To remove a company from your portfolio IN DEVELOPMENT\n"
                               " Select 3 to return to main menu"))
        if userchoice == 1:
            addtoportfolio()

def search(stockticker): # definiton of seach function
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0',
    })
    print('Stock ticker: ', stockticker)
    url = ("https://finance.yahoo.com/quote/%s" % stockticker)
    print(url)
    urlopen = requests.get(url, headers = headers)
    tree = html.fromstring(urlopen.content, "lxml")
    global price
    price = tree.xpath('//span[@class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]/text()')
    #description = tree.xpath('//p[@class="description__text"]/text()')
    day_low = tree.xpath('//span[@class="Trsdu(0.3s) "]/text()')
    low_high = tree.xpath('//td[@class="Ta(end) Fw(b) Lh(14px)"]/text()')
    #print('Description: ', description)
    print('Current stock price: $', price[0])
    print('Open stock price: $', day_low[1])
    print("Today's high and low prices: Low", low_high[0], 'High')
    mportfolio = portfolio
    if stockticker not in mportfolio:
        searchaddtoportfolio(stockticker)

def intitialportfolio():
    global portfolio
    portfolio = []
    workbook = xlrd.open_workbook('CompanyFile.xlsx', on_demand=True)
    global row_count
    worksheet = workbook.sheet_by_index(1)
    global row_count
    row_count = worksheet.nrows
    if row_count != 0:
        for i in range(worksheet.nrows):
            cell = worksheet.cell(i, 0).value
            portfolio.append(cell)



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
            ticker = worksheet.cell_value(i,0)
            print("Your company is: ", worksheet.cell_value(i,1))
            search(ticker)
        else:
            counter += 1
        if counter == 3312:
            print("Company not found")

def searchaddtoportfolio(stockticker):
    userchoice = int(input("Would you like to add this stock to your portfolio?\n 1 - Yes. 2 - No"))
    if userchoice == 1:
        wb = load_workbook(filename='CompanyFile.xlsx')
        sheet_ranges = wb['Sheet2']
        i = row_count
        if i == 0:
            sheet_ranges.cell(1, 1).value = stockticker
            wb.save('CompanyFile.xlsx')
        else:
            sheet_ranges.cell(i+1, 1).value = stockticker
            wb.save('CompanyFile.xlsx')

def addtoportfolio():
    searchtype = int(input("To search by ticker select 1 \n To search by company name select 2"))
    if searchtype == 1:
        companysearch = input("What is the company's ticker?").upper()
        search(companysearch)
        #validate ticker
    elif searchtype == 2:
        companysearch = input("What is the name of the company?")
        gosearch(companysearch)
        #validate company\

#def myportfolio():
 #   portfolio = []
###WATCHLIST###
def myportfolio():
    global portfolio
    portfolio = []
    workbook = xlrd.open_workbook('CompanyFile.xlsx', on_demand=True)
    global row_count
    worksheet = workbook.sheet_by_index(1)
    global row_count
    row_count = worksheet.nrows
    if row_count != 0:
        for i in range(worksheet.nrows):
            cell = worksheet.cell(i,0).value
            portfolio.append(cell)


while 1 == 1:
    directory()


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

    
