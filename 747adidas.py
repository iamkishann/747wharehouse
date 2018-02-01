import requests, random, time, json
from faker import Faker
from random import getrandbits


print ("################################################")
print ("             DEVELOPED BY @IAMKISHANN.          ")
print ("################################################")

def main():

    faker = Faker()
    s = requests.Session()
    s.headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 GoNativeIOS/1.0 gonative',
        'Content - Type': 'multipart / form - data;boundary = ----WebKitFormBoundaryISjufQPIlrzv35oT',
        'Referer': 'https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create'}
    s.headers.update()
    url = "https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create"



    fname = faker.first_name()
    lname = faker.last_name()
    ##################
    #replase this 
    #if your email 1234lab@gmail.com replase xxx with 1234lab
    #####################

    email = "xxx+{}@gmail.com".format(getrandbits(40)) #"1234lab+{}@gmail.com".format(getrandbits(40)) should look like this
    data = {
        "email":email,
        "firstName":fname,
        "lastName":lname,
        "gender":"F",
        "datepicker":"01/01/1990",
        "dateOfBirth":"1990-01-01",
        "legalCheckbox":"1",
        "countryOfSite":"US",
        "newsletterDomain":"United States",
        "newsletterLanguage":"en",
        "newsletterTypeId":"40000",
        "source":"543452387",
        "eventType":"adi_eCom_Basketball_adidas747",
        "sendMail":"Y",
        "consents":{"consent":[{"consentType":"AMF","consentValue":"Y","consentVersion":"ADIUS_VER_1"}]}
    }
    re = s.post(url, json=data)
    if "success" in re.text:
        print("Entry Successful with ", email, "success")

    else:
        print("Error submitting entry", "error")
        

while True:
    main()
    time.sleep(20)




