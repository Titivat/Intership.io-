from flask import Flask
from requests import get
from bs4 import BeautifulSoup

app = Flask(__name__)

def getLogoImage():
    url = "https://theinternship.io/"
    response = get(url)

    html_soup = BeautifulSoup(response.text, "html.parser")
    companyInformationList = html_soup.find_all("div", class_ = "partner")

    companyDic = {}

    for content in companyInformationList:
        companyLogo = content.find("img", class_ = "center-logos").get("src") 
        companyDetail = content.find("span", class_ = "list-company").text
        companyDic[ companyLogo ] = len(companyDetail)
        
    companyDic = sorted( companyDic.items(), key=lambda companyDetail: companyDetail[1])

    jsonFile = {}
    logoList = []

    for logoName in companyDic:
        logoList.append( { 'logo': url + logoName[0] } )
    
    jsonFile["companies"] = logoList

    return jsonFile

@app.route("/companies")
def getLogoImageAPI():
    return getLogoImage()

if __name__ == "__main__":
    app.run()
