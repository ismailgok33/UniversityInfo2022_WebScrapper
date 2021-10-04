from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from decimal import Decimal
import re


def uniNameToCityName(uniName):
    if uniName.lower().find("İstanbul".lower()) > -1:
        return "İSTANBUL"
    elif uniName.lower().find("Ankara".lower()) > -1:
        return "ANKARA"
    elif uniName.lower().find("İzmir".lower()) > -1:
        return "İZMİR"
    elif uniName.lower().find("Adana".lower()) > -1:
        return "ADANA"
    elif uniName.lower().find("Adıyaman".lower()) > -1:
        return "ADIYAMAN"
    elif uniName.lower().find("Afyonkarahisar".lower()) > -1:
        return "AFYONKARAHİSAR"
    elif uniName.lower().find("Ağrı".lower()) > -1:
        return "AĞRI"
    elif uniName.lower().find("Aksaray".lower()) > -1:
        return "AKSARAY"
    elif uniName.lower().find("Amasya".lower()) > -1:
        return "AMASYA"
    elif uniName.lower().find("Antalya".lower()) > -1:
        return "ANTALYA"
    elif uniName.lower().find("Ardahan".lower()) > -1:
        return "ARDAHAN"
    elif uniName.lower().find("Artvin".lower()) > -1:
        return "ARTVİN"
    elif uniName.lower().find("Aydın".lower()) > -1:
        return "AYDIN"
    elif uniName.lower().find("Balıkesir".lower()) > -1:
        return "BALIKESİR"
    elif uniName.lower().find("Bartın".lower()) > -1:
        return "BARTIN"
    elif uniName.lower().find("Batman".lower()) > -1:
        return "BATMAN"
    elif uniName.lower().find("Bayburt".lower()) > -1:
        return "BAYBURT"
    elif uniName.lower().find("Bilecik".lower()) > -1:
        return "BİLECİK"
    elif uniName.lower().find("Bingöl".lower()) > -1:
        return "BİNGÖL"
    elif uniName.lower().find("Bitlis".lower()) > -1:
        return "BİTLİS"
    elif uniName.lower().find("Bolu".lower()) > -1:
        return "BOLU"
    elif uniName.lower().find("Burdur".lower()) > -1:
        return "BURDUR"
    elif uniName.lower().find("Bursa".lower()) > -1:
        return "BURSA"
    elif uniName.lower().find("Çanakkale".lower()) > -1:
        return "ÇANAKKALE"
    elif uniName.lower().find("Çankırı".lower()) > -1:
        return "ÇANKIRI"
    elif uniName.lower().find("Çorum".lower()) > -1:
        return "ÇORUM"
    elif uniName.lower().find("Denizli".lower()) > -1:
        return "DENİZLİ"
    elif uniName.lower().find("Diyarbakır".lower()) > -1:
        return "DİYARBAKIR"
    elif uniName.lower().find("Düzce".lower()) > -1:
        return "DÜZCE"
    elif uniName.lower().find("Edirne".lower()) > -1:
        return "EDİRNE"
    elif uniName.lower().find("Elazığ".lower()) > -1:
        return "ELAZIĞ"
    elif uniName.lower().find("Erzincan".lower()) > -1:
        return "ERZİNCAN"
    elif uniName.lower().find("Eskişehir".lower()) > -1:
        return "ESKİŞEHİR"
    elif uniName.lower().find("Gaziantep".lower()) > -1:
        return "GAZİANTEP"
    elif uniName.lower().find("Giresun".lower()) > -1:
        return "GİRESUN"
    elif uniName.lower().find("Gümüşhane".lower()) > -1:
        return "GÜMÜŞHANE"
    elif uniName.lower().find("Hakkari".lower()) > -1:
        return "HAKKARİ"
    elif uniName.lower().find("Hatay".lower()) > -1:
        return "HATAY"
    elif uniName.lower().find("Iğdır".lower()) > -1:
        return "IĞDIR"
    elif uniName.lower().find("Isparta".lower()) > -1:
        return "ISPARTA"
    elif uniName.lower().find("Kahramanmaraş".lower()) > -1:
        return "KAHRAMANMARAŞ"
    elif uniName.lower().find("Karabük".lower()) > -1:
        return "KARABÜK"
    elif uniName.lower().find("Karamn".lower()) > -1:
        return "KARAMAN"
    elif uniName.lower().find("Kars".lower()) > -1:
        return "KARS"
    elif uniName.lower().find("Kastamonu".lower()) > -1:
        return "KASTAMONU"
    elif uniName.lower().find("Kayseri".lower()) > -1:
        return "KAYSERİ"
    elif uniName.lower().find("Kilis".lower()) > -1:
        return "KİLİS"
    elif uniName.lower().find("Kırıkkale".lower()) > -1:
        return "KIRIKKALE"
    elif uniName.lower().find("Kırşehir".lower()) > -1:
        return "KIRŞEHİR"
    elif uniName.lower().find("Kocaeli".lower()) > -1:
        return "KOCAELİ"
    elif uniName.lower().find("Konya".lower()) > -1:
        return "KONYA"
    elif uniName.lower().find("Kütahya".lower()) > -1:
        return "KÜTAHYA"
    elif uniName.lower().find("Malatya".lower()) > -1:
        return "MALATYA"
    elif uniName.lower().find("Manisa".lower()) > -1:
        return "MANİSA"
    elif uniName.lower().find("Mardin".lower()) > -1:
        return "MARDİN"
    elif uniName.lower().find("Mersin".lower()) > -1:
        return "MERSİN"
    elif uniName.lower().find("Muğla".lower()) > -1:
        return "MUĞLA"
    elif uniName.lower().find("Muş".lower()) > -1:
        return "MUŞ"
    elif uniName.lower().find("Nevşehir".lower()) > -1:
        return "NEVŞEHİR"
    elif uniName.lower().find("Niğde".lower()) > -1:
        return "NİĞDE"
    elif uniName.lower().find("Ordu".lower()) > -1:
        return "ORDU"
    elif uniName.lower().find("Osmaniye".lower()) > -1:
        return "OSMANİYE"
    elif uniName.lower().find("Rize".lower()) > -1:
        return "RİZE"
    elif uniName.lower().find("Sakarya".lower()) > -1:
        return "SAKARYA"
    elif uniName.lower().find("Samsun".lower()) > -1:
        return "SAMSUN"
    elif uniName.lower().find("Şanlıurfa".lower()) > -1:
        return "ŞANLIURFA"
    elif uniName.lower().find("Siirt".lower()) > -1:
        return "SİİRT"
    elif uniName.lower().find("Sinop".lower()) > -1:
        return "SİNOP"
    elif uniName.lower().find("Sivas".lower()) > -1:
        return "SİVAS"
    elif uniName.lower().find("Şırnak".lower()) > -1:
        return "ŞIRNAK"
    elif uniName.lower().find("Tekirdağ".lower()) > -1:
        return "TEKİRDAĞ"
    elif uniName.lower().find("Tokat".lower()) > -1:
        return "TOKAT"
    elif uniName.lower().find("Trabzon".lower()) > -1:
        return "TRABZON"
    elif uniName.lower().find("Tunceli".lower()) > -1:
        return "TUNCELİ"
    elif uniName.lower().find("Uşak".lower()) > -1:
        return "UŞAK"
    elif uniName.lower().find("Van".lower()) > -1:
        return "VAN"
    elif uniName.lower().find("Yalova".lower()) > -1:
        return "YALOVA"
    elif uniName.lower().find("Yozgat".lower()) > -1:
        return "YOZGAT"
    elif uniName.lower().find("Zonguldak".lower()) > -1:
        return "ZONGULDAK"
    elif uniName.lower().find("Gazimağusa".lower()) > -1:
        return "GAZİMAĞUSA-KKTC"
    elif uniName.lower().find("Lefkoşa".lower()) > -1:
        return "LEFKOŞA-KKTC"
    elif uniName.lower().find("Bakü".lower()) > -1:
        return "BAKÜ-AZERBAYCAN"
    elif uniName.lower().find("Girne".lower()) > -1:
        return "GİRNE-KKTC"
    elif uniName.lower().find("Türkistan".lower()) > -1:
        return "TÜRKİSTAN-KAZAKİSTAN"
    elif uniName.lower().find("Güzelyurt".lower()) > -1:
        return "GÜZELYURT-KKTC"
    elif uniName.lower().find("Bişkek".lower()) > -1:
        return "BİŞKEK-KIRGIZİSTAN"
    elif uniName.lower().find("Komrat".lower()) > -1:
        return "KOMRAT-MOLDOVA"
    elif uniName.lower().find("Lefke".lower()) > -1:
        return "LEFKE-KKTC"
    elif uniName.lower().find("Üsküp".lower()) > -1:
        return "ÜSKÜP-MAKEDONYA"
    else:
        return ""


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
    # if str(url) == "https://www.basarisiralamalari.com/alman-dili-ve-edebiyati-2022-taban-puanlari-ve-basari-siralamalari/":

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
            city = str(uniNameToCityName(uni))
            cityUniList = cells[0].text.split(')')
            if len(cityUniList) > 1:
                if len(cityUniList[1]) != 0:
                    city = cityUniList[1]
            if len(city_isState) > 1:
                if len(city_isState[1]) != 0:
                    city = str(city_isState[1])

            departmentList = re.findall(r'\((.*?) *\)', cells[1].text)
            department = cells[1].text.split("(")[0]

            if len(departmentList) > 0:
                if departmentList[0].find("KKTC") > -1:
                    department = department + "(KKTC)"
                if departmentList[0].find("İ.Ö") > -1:
                    department = department + "(İ.Ö)"
                if departmentList[0].find("U.Ö") > -1:
                    department = department + "(U.Ö)"
                if departmentList[0].find("MTOK") > -1:
                    department = department + "(MTOK)"

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
                    scholarship = "%100 Burslu"
                elif departmentList[0].find("%75") > -1:
                    scholarship = "%75 Burslu"
                elif departmentList[0].find("%50") > -1:
                    scholarship = "%50 Burslu"
                elif departmentList[0].find("%25") > -1:
                    scholarship = "%25 Burslu"
                elif departmentList[0].find("Burslu") > -1:
                    scholarship = "%100 Burslu"
                elif departmentList[0].find("Ücretli") > -1:
                    scholarship = "%0 Burslu"
                elif departmentList[0].find("Burssuz") > -1:
                    scholarship = "%0 Burslu"

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

            # f.write('University(universityID: UUID().uuidString, dictionary: ["name": "{0}", "state": "{1}", "city": "{2}", "department": "{3}", "duration": {4}, "language": "{5}", "minScore": {6}, "placement": {7}, "quota": {8}, "type": "{9}", "scholarship": "{10}" ]), \n\n '
            #         .format(uni.strip(), state.strip(), city.strip(), department.strip(), duration, language.strip(), minScore, placement, quota, uniType.strip(), scholarship.strip()))

            f.write('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10} # \n'
                    .format(uni.strip(), state.strip(), city.strip(), department.strip(), duration, language.strip(), minScore, placement, quota, uniType.strip(), scholarship.strip()))

            index = index + 1

f.close()
print('success')
