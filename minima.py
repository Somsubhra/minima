#!/usr/bin/env python

from minima import HyperVisor, Instance

hyper_visor = HyperVisor()
hyper_visor.print_host_info()

instance = Instance(hyper_visor)
instance.print_all_domains()
