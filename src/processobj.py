class Descriptor(object):
    
    def __init__(self): 
        self._name = ''
        
    def __get__(self, instance, owner):
        print ("Getting: %s" % self._name)
        return self._name
 
    def __set__(self, instance, name):
        print ("Setting: %s" % name)
        self._name = name.title()
 
    def __delete__(self, instance):
        print ("Deleting: %s" % self._name)
        del self._name
        
    def getStr(self, str):
        print( "####",self._name)

class JavaProcess():
    def xyb2bProcesses(self):
        xyb2bService = Descriptor()
        xyb2bService.module = ["UserApplication","SkuApplication","PayApplication"]
        return xyb2bService
    
    def adminProcesses(self):
        adminService = Descriptor()
        adminService.module = ["AdminApplication"]
        return adminService
    
    def apiProcesses(self):
        apiService = Descriptor()
        apiService.module = ["ApiApplication"]
        return apiService
    
    def suplierProcesses(self):
        supplierService = Descriptor()
        supplierService.module = ["SuplierApplication"]
        return supplierService
    
    def helperProcess(self, processModule):
        processModule.append("HelperApplication")

