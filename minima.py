#!/usr/bin/env python

from minima import HyperVisor, InstanceService

hyper_visor = HyperVisor()
hyper_visor.print_host_info()

instance_service = InstanceService(hyper_visor)

# instance = instance_service.create_instance("test", 512000, 1, "ubuntu")
instance_service.print_all_instances()

