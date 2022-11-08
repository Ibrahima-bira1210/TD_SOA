import zeep


def is_solvable(ssn):
    wsdl = "http://localhost:8084/?wsdl"
    client = zeep.Client(wsdl=wsdl)
    r = client.service.is_solvable(ssn)
    return r





    # url = "http://localhost:8084/?wsdl"
    # payload = '''
    #             <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.verifCreditService">
    #                <soapenv:Header/>
    #                <soapenv:Body>
    #                   <spy:is_solvable>
    #                      <!--Optional:-->
    #                      <spy:ssn>{ssn}</spy:ssn>
    #                   </spy:is_solvable>
    #                </soapenv:Body>
    #             </soapenv:Envelope>'''.format(ssn=ssn)
    # # headers
    # headers = {
    #     'Content-Type': 'text/xml; charset=utf-8'
    # }
    # # POST request
    # response = requests.request("POST", url, headers=headers, data=payload)
    #
    # # prints the response
    # r = response.content
    # print(r)