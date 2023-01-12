"""A Python Pulumi program"""
import os
import pulumi
import pulumi_vsphere as vsphere
from pulumi_vsphere import Folder
 





def main():
    # datacenter = vsphere.get_datacenter(name="RnD4")
    datacenter = vsphere.get_datacenter(name=os.getenv('DATACENTER_NAME'))
    compute_cluster = vsphere.get_compute_cluster(name=os.getenv('COMPUTE_CLUSTER'),
        datacenter_id=datacenter.id)




    datastore = vsphere.get_datastore(name="Vol2_78F19GN",
        datacenter_id=datacenter.id)



    # Create Folder 
    test_folder = Folder("pulumi_resources", 
            datacenter_id=datacenter.id,
            path= "/pulumi-resources",
            type="vm") 

    # collect all hosts
    # pulumi.export("ESXI_HOSTS_NAMES", os.getenv('ESXI_HOSTS_NAMES')
    
    pulumi.log.info("The extracted ESXI host from the environment variable ESXI_HOSTS_NAMES :  " + os.getenv('ESXI_HOSTS_NAMES') )
    pulumi.export("The extracted ESXI host from the environment variable ESXI_HOSTS_NAMES   " , os.getenv('ESXI_HOSTS_NAMES'))

    # esxi_hosts_address = split(os.getenv('ESXI_HOSTS_NAMES')," ")
    # esxi_hosts = []
    # for ip_address in esxi_hosts_address:
    #     esxi_hosts.append(vsphere.get_host(name=ip_address,datacenter_id=datacenter.id))


        


    '''
    vsphere.get_ovf_vm_template() required properties
    host_system_id :The ID of the ESXi host system to deploy the virtual machine.
    name : Name of the virtual machine to create.
    resource_pool_id: The ID of a resource pool in which to place the virtual machine.
    '''
    # k8s_node_ofv_template = vsphere.get_ovf_vm_template(host_system_id="",
    #                                                     name="",
    #                                                     resource_pool_id="")




if __name__ == '__main___':
    main()