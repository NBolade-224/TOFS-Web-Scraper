from requests_html import AsyncHTMLSession
import openpyxl, os, sys
from tkinter import *
from tkinter import filedialog




def GUI_Window():
    global MainWindow, LabelStatus

    MainWindow=Tk()
    MainWindow.title("Sending Emails") 
    MainWindow.geometry("600x700+600+200") 
    MainWindow.configure(bg="RoyalBlue4")

    label_file_explorer = Label(MainWindow,text = "Original Factory Shop: AOSOM Web Scraper",width = 100, height = 4,fg = "white",bg = 'RoyalBlue4', font=('Times', 13)) #RoyalBlue4
    main_script_button = Button(MainWindow,text = "AOSOM SKU File",bg = 'red3',width = 30, height = 2, command = Main_Script, font=('Times', 15, 'bold'), fg = "yellow2")
    button_exit = Button(MainWindow,text = "Exit",bg = 'snow4',width = 30,height = 2,command = sys.exit, font=('Times', 15, 'bold'), fg = "black")
    LabelStatus = Label(MainWindow,text = "",width = 75, height = 2,fg = "white",bg = 'RoyalBlue4', font=('Times', 16))
    LabelSpace0PDF = Label(MainWindow,text = "",width = 75, height = 1,fg = "red",bg = 'RoyalBlue4')
    LabelSpace1PDF = Label(MainWindow,text = "",width = 75, height = 1,fg = "red",bg = 'RoyalBlue4')
    LabelSpace2PDF = Label(MainWindow,text = "",width = 75, height = 1,fg = "red",bg = 'RoyalBlue4')

    label_file_explorer.pack()
    main_script_button.pack()
    LabelSpace0PDF.pack()
    LabelStatus.pack()
    LabelSpace1PDF.pack()
    LabelSpace2PDF.pack()
    button_exit.pack()
    MainWindow.mainloop()



def Main_Script():
    #########################################################################################################################################
    ################ EXCEL FILE: THIS FILE WILL PROVIDE THE SKUS THAT WILL BE SEARCHED, AND THEN THE PRICES FOUND WILL BE WRITTEN TO THIS FILE.
    #########################################################################################################################################
    MHStar_SKU_List = filedialog.askopenfilename(initialdir = "C:\\Users\\",title = "Select file",filetypes = (("Excel","*xlsx"),))
    ExcelFile = openpyxl.load_workbook(MHStar_SKU_List)
    ExcelSheet = ExcelFile.active

    LabelStatus.config(text="Processing")
    MainWindow.update()

    mylist = []
    dict2 = {}

    for col in ExcelSheet['A']:
        mylist.append(col.value)
        dict2[col.value] = "N/A"

    asession  = AsyncHTMLSession()

    urls1 = [
    "https://www.aosom.co.uk/category/home~420/",
    "https://www.aosom.co.uk/category/office~199/",
    "https://www.aosom.co.uk/category/sports-leisure~161/",
    "https://www.aosom.co.uk/category/health-beauty~208/",
    "https://www.aosom.co.uk/category/toys-games~230/",
    "https://www.aosom.co.uk/category/baby-products~250/",
    "https://www.aosom.co.uk/patio-lawn-garden/garden-shades-c789.html",
    "https://www.aosom.co.uk/patio-lawn-garden/garden-buildings-c798.html",
    "https://www.aosom.co.uk/patio-lawn-garden/garden-tools-c800.html",
    "https://www.aosom.co.uk/patio-lawn-garden/barbecues-c748.html",]

    ######## Two URL groups are used to prevent overload on requests to the website

    urls2 = [
    "https://www.aosom.co.uk/patio-lawn-garden/garden-decor-c801.html",
    "https://www.aosom.co.uk/patio-lawn-garden/garden-planters-stands-c799.html",
    "https://www.aosom.co.uk/category/fire-pits~132/",
    "https://www.aosom.co.uk/category/kitchen-equipment~443/",
    "https://www.aosom.co.uk/category/diy~215/",
    "https://www.aosom.co.uk/category/garden-furniture-accessories~131/",
    "https://www.aosom.co.uk/category/pet-supplies~184/",
    "https://www.aosom.co.uk/category/sofa-lounges~434/",
    "https://www.aosom.co.uk/category/home-furniture-all~423/",
    "https://www.aosom.co.uk/category/storage-cleaning-solutions~425/",
    "https://www.aosom.co.uk/category/shoe-bench~626/",
    "https://www.aosom.co.uk/category/bathroom~421/",]

    #########################################################################################################################################
    ################ THIS FUNCTION RUNS ASYNC AND WILL LOOP THROUGH EACH CATEGORY OF PRODUCTS UNTILL A MATCH IS FOUND (FROM SKUS LISTED IN EXCEL FILE)
    ################ WHEN A MATCH IS FOUND, THE SKU PRODUCT AND ITS PRICE ARE HELD IN A DICTIONARY TO BE LATER WRITTEN TO EXCEL
    #########################################################################################################################################

    async def Scraper1(vurl):
        m = 1
        for x in range(0,100):
            url = vurl+"?column=0&page=%d&psort=0" % int(m)
            page = await asession.get(url)
            products = page.html.find('.display-good-item')
            if products == []:
                break
            for x in products:
                if x.attrs.get('sellersku') in mylist:
                    print(x.attrs.get('sellersku'))
                    price = float(x.attrs.get('price')) / 100
                    print(price)
                    dict2[x.attrs.get('sellersku')] = price
                    print()
            m += 1

    asession.run(*[lambda vurl=vurl: Scraper1(vurl) for vurl in urls1])
    asession.run(*[lambda vurl=vurl: Scraper1(vurl) for vurl in urls2])

    #########################################################################################################################################
    ################ THIS FINAL PART WRITES ALL THE DATA FROM THE TEMP DICTIONARY, INTO THE EXCEL FILE FOR COMMERCIAL ANALYSIS
    #########################################################################################################################################

    for x in dict2:
        Row = mylist.index(x) + 1
        ExcelSheet['B%d' % int(Row)] = dict2.get(x)

    ExcelSheet['B1'] = "Price"

    ExcelFile.save(MHStar_SKU_List)

    LabelStatus.config(text="Finished")
    MainWindow.update()
GUI_Window()