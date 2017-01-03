#!/usr/bin/env python

from minima import HyperVisor, InstanceService

hyper_visor = HyperVisor()
hyper_visor.print_host_info()

instance_service = InstanceService(hyper_visor)
instance_service.print_all_instances()
