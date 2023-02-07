"""A Python Pulumi program"""

import pulumi

import os
import pulumi_vsphere as vsphere
from pulumi_vsphere import  VirtualMachineNetworkInterfaceArgs , VirtualMachineDiskArgs, VirtualMachineCloneArgs, Folder, VirtualMachineCloneCustomizeArgs, VirtualMachineCloneCustomizeLinuxOptionsArgs, VirtualMachineCloneCustomizeNetworkInterfaceArgs
from pulumi import ResourceOptions


def main():

    # Vsphere   datacenter & compute_cluster
    datacenter = vsphere.get_datacenter(name=os.getenv('DATACENTER_NAME'))
    # pulumi.export('dir(datacenter)',dir(datacenter))
    compute_cluster = vsphere.get_compute_cluster(name=os.getenv('COMPUTE_CLUSTER'),datacenter_id=datacenter.id)
    # pulumi.export('dir(compute_cluster)',dir(compute_cluster))
    
     # Create Folder 
    test_folder = Folder("pulumi_resources", 
            datacenter_id=datacenter.id,
            path= "/pulumi-resources",
            type="vm") 

    # Discover the ID of a vSphere datastore object. 
    datastores = [vsphere.get_datastore(name=ds_name,datacenter_id=datacenter.id) for ds_name in (os.getenv('DATASTORE_NAMES')).split(" ")]
    # pulumi.export('datastores',[ds.id for ds in datastores ])

    # discover the ID of an ESXi host.
    esxi_host = [vsphere.get_host(name=host_name,datacenter_id=datacenter.id) for host_name in (os.getenv('ESXI_HOSTS_NAMES')).split(" ")]
    # pulumi.export('esxi hosts',[host for host in esxi_host])

    # The vsphere.getOvfVmTemplate data source can be used to submit an OVF to vSphere 
    # and extract its hardware settings in a form that can be then used as inputs for a vsphere.VirtualMachine resource.
    template = vsphere.get_virtual_machine(name="Ubuntu-22.04.1-Key-Based",
    datacenter_id=datacenter.id)
    pulumi.export('dir(template)',dir(template))
    pulumi.export('dir(template)',template.name)

    # The vsphere.getNetwork data source can be used to discover the ID of a network in vSphere. 
    # This can be any network that can be used as the backing for a network interface for vsphere.VirtualMachine or any other vSphere resource that requires a network. 
    network = vsphere.get_network(name=os.getenv('VSPHERE_NETWORK'),datacenter_id=datacenter.id)
    # pulumi.export('dir(network)',dir(network))


    nodes_ipv4_address = os.getenv('NODES_IPV4_ADDRESS').split(" ")
    # Create VirtualMachine Resource 
    virtual_machinens = []
    for ip_index in range(0,len(nodes_ipv4_address)):
        virtual_machinens.append(
            vsphere.VirtualMachine(resource_name= "node-00" + str(ip_index + 1),
                    opts=ResourceOptions(depends_on=[test_folder]),
                    name="node-00" + str(ip_index + 1),
                    folder="/pulumi-resources",
                    datastore_id=datastores[1].id,
                    resource_pool_id=compute_cluster.resource_pool_id,
                    host_system_id=esxi_host[0].id,
                    num_cpus=4,
                    memory=8192,
                    guest_id=template.guest_id,
                    scsi_type=template.scsi_type,
                    network_interfaces=[VirtualMachineNetworkInterfaceArgs(
                        network_id=network.id
                    )],
                    disks=[VirtualMachineDiskArgs(
                        label="disk-0",
                        size=50,
                        thin_provisioned=True
                    )],
                    clone=VirtualMachineCloneArgs(
                        template_uuid=template.uuid,
                        customize=VirtualMachineCloneCustomizeArgs(
                            dns_server_lists=os.getenv('DNS_SERVER_LISTS').split(" "),
                            ipv4_gateway=os.getenv('IPV4_GATEWAY'),
                            linux_options=VirtualMachineCloneCustomizeLinuxOptionsArgs(
                                domain="kubernetes.com",
                                host_name="node-00" + str(ip_index + 1)
                            ),
                            network_interfaces=[VirtualMachineCloneCustomizeNetworkInterfaceArgs(
                                ipv4_address=nodes_ipv4_address[ip_index],
                                ipv4_netmask=int(os.getenv('IPV4_NETMASK'))
                            )]

                        )
                    )
                )
        )
                    
    # pulumi.export('dir vm',dir(virtual_machine.default_ip_address.all))
        
    

if __name__ == '__main__':
    main() 