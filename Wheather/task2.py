from zeep import Client


wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = " "
client = Client(wsdl=wsdl)


def test01():
    assert client.service.VerifySignature('CMS', sign)["Result"]
