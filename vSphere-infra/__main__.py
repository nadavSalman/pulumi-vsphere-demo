"""A Python Pulumi program"""

import pulumi_vsphere as vsphere
from pulumi_vsphere import Folder

datacenter = vsphere.get_datacenter(name="RnD4")

# Create Folder 
from pulumi_vsphere import Folder

test_folder = Folder("pulumi_resources", 
           datacenter_id=datacenter.id,
           path= "/pulumi-resources",
           type="vm") 