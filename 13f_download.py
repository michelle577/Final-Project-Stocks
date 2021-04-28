import threading
import time

from lxml import html, etree
import requests
from bs4 import BeautifulSoup
import pandas as pd
listtime = None
count = 0
lock = threading.Lock()
import pandas as pd

def waitrequest():
    global lock
    lock.acquire()
    global listtime
    global count
    if listtime == None or count >= 8:
        if listtime != None:
            n = (listtime + 1) - time.time()
            if n > 0:
                count = 0
                print("sleep for ", n)
                time.sleep(n)
        listtime = time.time()
    if time.time() - listtime >= 1:
        listtime = time.time()
        count = 0
    count += 1
    lock.release()
def testF13(companyid):
    filetype = "13F-HR"
#    request = requests.get(
 #       r"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=" + companyid + "&type=" + filetype + "&owner=exclude&count=100")
  #  content = request.content
    waitrequest()
    request = requests.get(
        r"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=" + companyid + "&type=" + filetype + "&owner=exclude&count=100")
    page = html.fromstring(request.content)
    fileurls = []
    # get the html elements that have the class interactiveDataBtn in the html and from that get the parent object tr from that we pull all the data
    for tr_element in page.xpath("//*[@id='documentsbutton']/ancestor::tr"):
        filetype_tr = tr_element[0].text
        if filetype_tr == filetype:
            spliturl = tr_element[1][0].attrib.get("href").rsplit('/', 1)
            firsthalf = spliturl[0]
            secfillingid = firsthalf[firsthalf.rindex("/") + 1:]
            waitrequest()
            request = requests.get( "https://www.sec.gov" + firsthalf)
            bs = BeautifulSoup(request.content,features="lxml")
            print(bs)
            t = bs.find("table")
            rows = t.find_all("tr")
            url = "NotSet"
            for row in reversed(rows):
                if row.contents[0].text.split(".")[-1] == "xml" and "primary" not in row.contents[0].text:
                    url =  "https://www.sec.gov" + row.contents[0].contents[0].attrs["href"]
                    date = row.contents[-1].text.split(" ")[0]
                    break
                print("e")
            fileurls.append((url,date))


    waitrequest()
   # request = requests.get(fileurls[0])
  #  if request.status_code == 404:
   #   raise NameError('404 ' + documents_url + " Not Found In site")
    #master_reports = []

    import xmltodict

  #  url = "https://yoursite/your.xml"
    bigvalue = []
    datafield = []
    fields = []
    for fileurl in fileurls:
        if fileurl[0] == "NotSet":
            continue
        response = requests.get(fileurl[0])
        data = xmltodict.parse(response.content)
        dic = data[list(data)[-1]]
        dic = dic[list(dic)[-1]]


        if len(datafield) == 0:
            fields = list(dic[0])
            for field in fields:
                if isinstance(dic[0][field], xmltodict.OrderedDict):
                    subdfields = list(dic[0][field])
                    for subdfield in subdfields:
                        datafield.append(field + " " + subdfield)
                else:
                    datafield.append(field)
            datafield.append("Date")
        for row in dic:
            values = []
            for field in fields:
                try:
                    if isinstance(row[field], xmltodict.OrderedDict):
                        subdfields = list(row[field])
                        for subdfield in subdfields:
                            values.append(row[field][subdfields])
                    else:
                        values.append(row[field])
                except:
                   # values.append("")
                    print("oops " + field)
            values.append(fileurl[1])
            bigvalue.append(values)
    dataframe = pd.DataFrame(bigvalue)
    dataframe.columns = datafield
    print(dataframe)
    dataframe.to_csv("13-f.csv")

   # for report in list(BeautifulSoup(request.content).contents[1].contents[0].contents[0]):  # [:-1]:
    print("e")

































testF13("0000072971")