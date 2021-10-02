from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from decimal import Decimal
import re


def cityToCode(cityName):
    switcher = {
        "İSTANBUL": "1",
        "ANKARA": "2",
        "İZMİR": "3",
        "ADANA": "4",
        "ADIYAMAN": "5",
        "AFYONKARAHİSAR": "6",
        "AĞRI": "7",
        "AKSARAY": "8",
        "AMASYA": "9",
        "ANTALYA": "10",
        "ARDAHAN": "11",
        "ARTVİN": "12",
        "AYDIN": "13",
        "BALIKESİR": "14",
        "BARTIN": "15",
        "BATMAN": "16",
        "BAYBURT": "17",
        "BİLECİK": "18",
        "BİNGÖL": "19",
        "BİTLİS": "20",
        "BOLU": "21",
        "BURDUR": "22",
        "BURSA": "23",
        "ÇANAKKALE": "24",
        "ÇANKIRI": "25",
        "ÇORUM": "26",
        "DENİZLİ": "27",
        "DİYARBAKIR": "28",
        "DÜZCE": "29",
        "EDİRNE": "30",
        "ELAZIĞ": "31",
        "ERZİNCAN": "32",
        "ERZURUM": "33",
        "ESKİŞEHİR": "34",
        "GAZİANTEP": "35",
        "GİRESUN": "36",
        "GÜMÜŞHANE": "37",
        "HAKKARİ": "38",
        "HATAY": "39",
        "IĞDIR": "40",
        "ISPARTA": "41",
        "KAHRAMANMARAŞ": "42",
        "KARABÜK": "43",
        "KARAMAN": "44",
        "KARS": "45",
        "KASTAMONU": "46",
        "KAYSERİ": "47",
        "KİLİS": "48",
        "KIRIKKALE": "49",
        "KIRKLARELİ": "50",
        "KIRŞEHİR": "51",
        "KOCAELİ": "52",
        "KONYA": "53",
        "KÜTAHYA": "54",
        "MALATYA": "55",
        "MANİSA": "56",
        "MARDİN": "57",
        "MERSİN": "58",
        "MUĞLA": "59",
        "MUŞ": "60",
        "NEVŞEHİR": "61",
        "NİĞDE": "62",
        "ORDU": "63",
        "OSMANİYE": "64",
        "RİZE": "65",
        "SAKARYA": "66",
        "SAMSUN": "67",
        "ŞANLIURFA": "68",
        "SİİRT": "69",
        "SİNOP": "70",
        "SİVAS": "71",
        "ŞIRNAK": "72",
        "TEKİRDAĞ": "73",
        "TOKAT": "74",
        "TRABZON": "75",
        "TUNCELİ": "76",
        "UŞAK": "77",
        "VAN": "78",
        "YALOVA": "79",
        "YOZGAT": "80",
        "ZONGULDAK": "81",
        "KKTC-GAZİMAĞUSA": "82",
        "KKTC-LEFKOŞA": "83",
        "BAKÜ-AZERBAYCAN": "84",
        "KKTC-GİRNE": "85",
        "TÜRKİSTAN-KAZAKİSTAN": "86",
        "KKTC-GÜZELYURT": "87",
        "BİŞKEK-KIRGIZİSTAN": "88",
        "KOMRAT-MOLDOVA": "89",
        "KKTC-LEFKE": "90",
        "ÜSKÜP-MAKEDONYA": "91",
    }
    return switcher.get(cityName, "0")


f = open("university-data.txt", "a")

mainUrl = 'https://www.basarisiralamalari.com/4-yillik-bolumlerin-basari-siralamalari-taban-puanlari-osym/'
# Opens up the connection and gets the html page from it
uClient = uReq(mainUrl)
pageHtml = uClient.read()

# Closes the connection
uClient.close()

pageSoup = soup(pageHtml.decode('utf-8', 'ignore'), 'html.parser')

uniDiv = pageSoup.find('div', {'id': 'singleContent'})
uniList = uniDiv.find('ul')
allRows = uniList.findAll('li')

allURLs = []

for row in allRows:
    href = row.find('a')
    if href is None:
        continue
    allURLs.append(str(href.get('href')))

index = 1

for url in allURLs:
    # if str(url) == "https://www.basarisiralamalari.com/bilgi-guvenligi-teknolojisi-2022-taban-puanlari-ve-basari-siralamalari/":

    # Opens up the connection and gets the html page from it
    uClient = uReq(url)
    pageHtml = uClient.read()

    # Closes the connection
    uClient.close()

    pageSoup = soup(pageHtml.decode('utf-8', 'ignore'), 'html.parser')

    uniTableList = pageSoup.findAll('table', {'id': 'basaritable'})
    if uniTableList is None:
        uniTableList = pageSoup.findAll('table', {'id': 'universitego'})
    # tableHeader = uniTable.tbody.tr
    for uniTable in uniTableList:
        wholeTbody = uniTable.tbody
        allRows = wholeTbody.findAll('tr')

        for row in allRows:
            cells = row.findAll('td')
            if cells[0].text == 'Üniversite Adı':
                continue
            # Gets the University Name from the first column
            uni = cells[0].text.split('(')[0]
            # Gets city and isState values from the first column as well
            city_isState = re.findall(r'\((.*?) *\)', cells[0].text)

            state = ""
            if len(city_isState) > 0:
                state = city_isState[0]

            city = ""
            cityUniList = cells[0].text.split(')')
            if len(cityUniList) > 1:
                city = cityUniList[1]
            if len(city_isState) > 1:
                city = str(city_isState[1])

            departmentList = re.findall(r'\((.*?) *\)', cells[1].text)
            department = cells[1].text.split("(")[0]

            duration = 4

            language = "Türkçe"
            if len(departmentList) > 0:
                if departmentList[0].find("Alm") > -1:
                    language = "Almanca"
                elif departmentList[0].find("İng") > -1:
                    language = "İngilizce"
                elif departmentList[0].find("Fra") > -1:
                    language = "Fransızca"
                else:
                    language = "Türkçe"

            scholarship = ""
            if len(departmentList) > 0:
                if departmentList[0].find("%100") > -1:
                    scholarship = "%100"
                elif departmentList[0].find("%75") > -1:
                    scholarship = "%75"
                elif departmentList[0].find("%50") > -1:
                    scholarship = "%50"
                elif departmentList[0].find("%25") > -1:
                    scholarship = "%25"
                elif departmentList[0].find("Burslu") > -1:
                    scholarship = "%100"
                elif departmentList[0].find("Ücretli") > -1:
                    scholarship = "%0"
                elif departmentList[0].find("Burssuz") > -1:
                    scholarship = "%0"

            minScore = 0
            minScoreString = (cells[4].text).replace(",", ".")
            try:
                float(minScoreString)
                minScore = Decimal(minScoreString)
            except ValueError:
                print("minScore Not a float")

            placement = 0
            placementString = ""
            if len(cells) > 5:
                if (cells[5].text).find(",") > -1:
                    placementString = (cells[5].text).replace(",", "")
                if (cells[5].text).find(".") > -1:
                    placementString = (cells[5].text).replace(".", "")
                try:
                    int(placementString)
                    placement = int(placementString)
                except ValueError:
                    print("Placement Not an int")

            quota = 0
            try:
                int(cells[3].text)
                quota = int(cells[3].text)
            except ValueError:
                print("Quota Not an int")

            uniType = cells[2].text

            # print("uni= " + uni)
            # print("state= " + state)
            # print("city= " + city)
            # print("department= " + department)
            # print("duration= " + str(duration))
            # print("language= " + language)
            # print("minScore= " + str(minScore))
            # print("placement= " + str(placement))
            # print("quota= " + str(quota))
            # print("uniType= " + uniType)
            # print("scholarship= " + scholarship)
            # print("\n\n")

            f.write('University(universityID: UUID().uuidString, dictionary: ["name": "{0}", "state": "{1}", "city:" "{2}", "department:" "{3}", "duration:" {4}, "language:" "{5}", "minScore:" {6}, "placement:" {7}, "quota:" {8}, "type:" "{9}", "scholarship:" "{10}" ]), \n\n '
                    .format(uni, state, city, department, duration, language, minScore, placement, quota, uniType, scholarship))

            index = index + 1

f.close()
print('success')
