import suds
from suds.client import Client

# SOAP request URL
class serverRequest():
  # structured XML
  def fnGetTestHistory(Customer,serialNumber):

    url = "http://mxgdlm7web06/MES_TiS_GDL_Pruebas_ALL/MES_TIS_GDL.asmx?WSDL"
    SOAPclient = Client(url)

    request = SOAPclient.factory.create('tns:fnGetTestHistory')
    request.CustomerName = Customer
    request.SerialNumber = serialNumber
    response = SOAPclient.service.fnGetTestHistory(request)
    return response

  def fnLookupCustAssy(Customer,serialNumber):

      url = "http://mxgdlm7web06/MES_TiS_GDL_Pruebas_ALL/MES_TIS_GDL.asmx?WSDL"
      SOAPclient = Client(url)

      request = SOAPclient.factory.create('tns:fnLookupCustAssy')
      request.CustomerName = Customer
      request.SerialNumber = serialNumber
      response = SOAPclient.service.fnLookupCustAssy(request)
      return response
###################################################################################################################################3
'''
Suds ( https://fedorahosted.org/suds/ )  version: 1.1.2

Service ( MES_TIS_GDL ) tns="http://www.jabil.com"
   Prefixes (0)
   Ports (2):
      (MES_TIS_GDLSoap)
         Methods (21):
            GetASYPack(xs:string startDate, xs:string endDate)
            GetAssemblyProperty()
            GetBoardHistory(xs:int CustomerID, xs:string SerialNumber)
            GetBoardHistoryShort(xs:string SerialNumber)
            GetChildSNBYLinkObject(xs:string Customer, xs:string SerialNumber, xs:string LinkObject)
            GetChildSNBySN(xs:string strSN, xs:string strCustomer)
            GetChildSNBySNBYLinkObject(xs:string strSN, xs:string strCustomer, xs:string LinkObject)
            GetFilePathBySN(xs:string SN)
            GetPVStepsByAssembly(xs:string assembly, xs:string revision)
            GetPVStepsByAssemblyCoordinates(xs:string assembly, xs:string revision)
            GetRepairDatesBySerialNumber(xs:string serialnumber)
            GetRepairDianostic(xs:string startDate, xs:string endDate)
            GetTRWithLatestTarsTime(xs:string Customer, xs:string Serialnumber, xs:string TestItems)
            GetTestLoops(xs:string SerialNumber)
            GetTestResult(xs:string Customer, xs:string Serialnumber, xs:string TestItems)
            GetWifiAddForGP(xs:string SN)
            GetWifiAddForGPSMT(xs:string SN)
            TIS(xs:string sQMType, xs:string sCustomer, xs:string sSerialNo, xs:string sTester, xs:string sProcessStep)
            fnGetCustomerDivision(xs:string SerialNumber)
            fnGetTestHistory(xs:string CustomerName, xs:string SerialNumber)
            fnLookupCustAssy(xs:string CustomerName, xs:string SerialNumber)
         Types (0):
      (MES_TIS_GDLSoap12)
         Methods (21):
            GetASYPack(xs:string startDate, xs:string endDate)
            GetAssemblyProperty()
            GetBoardHistory(xs:int CustomerID, xs:string SerialNumber)
            GetBoardHistoryShort(xs:string SerialNumber)
            GetChildSNBYLinkObject(xs:string Customer, xs:string SerialNumber, xs:string LinkObject)
            GetChildSNBySN(xs:string strSN, xs:string strCustomer)
            GetChildSNBySNBYLinkObject(xs:string strSN, xs:string strCustomer, xs:string LinkObject)
            GetFilePathBySN(xs:string SN)
            GetPVStepsByAssembly(xs:string assembly, xs:string revision)
            GetPVStepsByAssemblyCoordinates(xs:string assembly, xs:string revision)
            GetRepairDatesBySerialNumber(xs:string serialnumber)
            GetRepairDianostic(xs:string startDate, xs:string endDate)
            GetTRWithLatestTarsTime(xs:string Customer, xs:string Serialnumber, xs:string TestItems)
            GetTestLoops(xs:string SerialNumber)
            GetTestResult(xs:string Customer, xs:string Serialnumber, xs:string TestItems)
            GetWifiAddForGP(xs:string SN)
            GetWifiAddForGPSMT(xs:string SN)
            TIS(xs:string sQMType, xs:string sCustomer, xs:string sSerialNo, xs:string sTester, xs:string sProcessStep)
            fnGetCustomerDivision(xs:string SerialNumber)
            fnGetTestHistory(xs:string CustomerName, xs:string SerialNumber)
            fnLookupCustAssy(xs:string CustomerName, xs:string SerialNumber)
         Types (0):
'''