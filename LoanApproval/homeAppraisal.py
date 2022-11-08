import requests
import zeep


def home_appraisal(home_price, loan_amount):
    wsdl = "http://localhost:8082/?wsdl"
    client = zeep.Client(wsdl=wsdl)
    r = client.service.home_eval(home_price, loan_amount)
    return r

    # url = "http://localhost:8082/?wsdl"
    # payload = '''
    #         <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.homeAppraisal">
    #            <soapenv:Header/>
    #            <soapenv:Body>
    #               <spy:home_eval>
    #                  <!--Optional:-->
    #                  <spy:homePrice>{homeprice}</spy:homePrice>
    #                  <!--Optional:-->
    #                  <spy:loanAmount>{loanAmount}</spy:loanAmount>
    #               </spy:home_eval>
    #            </soapenv:Body>
    #         </soapenv:Envelope>'''.format(homeprice=home_price, loanAmount=loan_amount)
    # # headers
    # headers = {
    #     'Content-Type': 'text/xml; charset=utf-8'
    # }
    # # POST request
    # response = requests.request("POST", url, headers=headers, data=payload)
    #
    # # prints the response
    # print(response.text)
    # print(response)

