'''
Created on Oct 23, 2011

@author: mpastern
'''

############ GENERATED CODE ############

from org.ovirt.sdk.python.utils.searchhelper import SearchHelper
from org.ovirt.sdk.python.utils.parsehelper import ParseHelper
from org.ovirt.sdk.python.infrastructure.common import Base   
from org.ovirt.sdk.python.utils.filterhelper import FilterHelper
from org.ovirt.sdk.python.utils.urlhelper import UrlHelper
from org.ovirt.sdk.python.xml import params


class NIC(params.NIC, Base):
    '''
    VM nic
    '''    
    def __init__(self, vm, nic):        
        self.parentclass = vm
        self.superclass  = nic
        
    def __new__(cls, vm, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, nic)
        return obj
        
#TODO: add template for the sub-resource action        
    def do(self):
        '''
        dummy action
        '''        
        url = '/api/vms/{vm:id}/nics/{nic:id}/do'
        
        action = params.Action(vm=self.superclass)        
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(), 
                                                                     '{nic:id}': self.get_id()}), 
                                          body=ParseHelper.toXml(action))    

        return result

    def update(self):
        '''
        dummy
        '''        
        url = '/api/vms/{vm:id}/nics/{nic:id}'
        
        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(), 
                                                                     '{nic:id}': self.get_id()}), 
                                         body=ParseHelper.toXml(self.superclass))

        return NIC(self.parentclass, result)
    
    def delete(self, force=False, grace_period=False):            
        '''
        Deletes the VM NIC
        '''
        url = '/api/vms/{vm:id}/nics/{nic:id}'
        
        if ((force or grace_period) is not False):            
            action = params.Action(force=force, grace_period=grace_period)                
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(), 
                                                                         '{nic:id}': self.get_id()}), 
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(), 
                                                                         '{nic:id}': self.get_id()}),
                                             headers={"Content-type":None})
        return result

class NICs(Base):
    '''
    VM nics collection
    '''
    
    def __init__(self, vm):
        """Constructor."""
        self.parentclass = vm
        
    def get(self, name='None', **kwargs):
        '''
        Retrieves the NIC
        '''
        
        url = '/api/vms/{vm:id}/nics'
        
        if(name is not None): kwargs['name']=name        
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_nic()

        return NIC(self.parentclass, 
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))
    
    def list(self, **kwargs):
        '''
        List all VM's NICs
        '''        
        
        url = '/api/vms/{vm:id}/nics'
        
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_nic()  
                                  
        return ParseHelper.toSubCollection(NIC, 
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))
    
    def add(self, nic):
        '''
        Creates the VM
        '''
        
        url = '/api/vms/{vm:id}/nics'        
        
        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}), 
                                      body=ParseHelper.toXml(nic))

        return NIC(self.parentclass, result)
        
class VM(params.VM, Base):
    '''
    VM Resource
    '''        
    
    def __init__(self, vm):            
#TODO: find better solution than predefining sub-collection
            self.nics = []
            self.nics = NICs(vm)
            
            self.superclass = vm
            
    def __new__(cls, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm)
        return obj
            
    def start(self):
        '''
        Starts the VM
        '''        
        url = '/api/vms/{vm:id}/start'
        
        action = params.Action(vm=self.superclass)        
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}), 
                                          body=ParseHelper.toXml(action))
        
        return result

    def update(self):
        '''
        Updates the VM
        '''        
        url = '/api/vms/{vm:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}), 
                                         body=ParseHelper.toXml(self.superclass))        
        return VM(result)

    def delete(self, force=False, grace_period=False):            
        '''
        Deletes the VM
        '''
        url = '/api/vms/{vm:id}'
        
        if ((force or grace_period) is not False):            
            action = params.Action(force=force, grace_period=grace_period)                
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}), 
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                             headers={"Content-type":None})
        return result

class VMs(Base):
    '''
    VMs Collection
    '''
    
    def __init__(self):
        """Constructor."""
    
    def get(self, name='*', **kwargs):
        '''
        Retrieves the VM
        '''
        url = '/api/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_vm()        

        return VM(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        List all VMs
        @param       query: oVirt engine dialect query
        @param     **kwargs: used to filter collection members if no search capabilities 
                            available at given collection resource        
        '''

        url='/api/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_vm()

        return ParseHelper.toCollection(VM, 
                                        FilterHelper.filter(result, kwargs))
    
    def add(self, vm):
        '''
        Creates the VM
        '''
        
        url = '/api/vms'        
        
        result = self._getProxy().add(url=url, 
                                      body=ParseHelper.toXml(vm))
        
        return VM(result)
