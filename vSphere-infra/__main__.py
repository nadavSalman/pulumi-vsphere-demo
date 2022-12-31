"""A Python Pulumi program"""

import pulumi_vsphere as vsphere

datacenter = vsphere.get_datacenter(name="RnD4")
    