import libvirt


class Instance:

    def __init__(self, hyper_visor):
        self.hyper_visor = hyper_visor
        self.conn = hyper_visor.get_connection()

    #############################################
    #           All the listing methods         #
    #############################################
    def get_all_instances(self):
        return self.conn.listAllDomains(0)

    def print_all_instances(self):
        self.print_instances(self.get_all_instances())

    def get_active_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_ACTIVE)

    def print_active_instances(self):
        self.print_instances(self.get_active_instances())

    def get_inactive_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_INACTIVE)

    def print_inactive_instances(self):
        self.print_instances(self.get_inactive_instances())

    def get_persistent_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_PERSISTENT)

    def print_persistent_instances(self):
        self.print_instances(self.get_persistent_instances())

    def get_transient_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_TRANSIENT)

    def print_transient_instances(self):
        self.print_instances(self.get_transient_instances())

    def get_running_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_RUNNING)

    def print_running_instance(self):
        self.print_instances(self.get_running_instances())

    def get_paused_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_PAUSED)

    def print_paused_instances(self):
        self.print_instances(self.get_paused_instances())

    def get_shutoff_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_SHUTOFF)

    def print_shutoff_instances(self):
        self.print_instances(self.get_shutoff_instances())

    def get_other_instances(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_OTHER)

    def print_other_instances(self):
        self.print_instances(self.get_other_instances())

    def get_instances_with_managed_save(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_MANAGEDSAVE)

    def print_instances_with_managed_save(self):
        self.print_instances(self.get_instances_with_managed_save())

    def get_instances_without_managed_save(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_NO_MANAGEDSAVE)

    def print_instances_without_managed_save(self):
        self.print_instances(self.get_instances_without_managed_save())

    def get_instances_with_auto_start(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_AUTOSTART)

    def print_instances_with_auto_start(self):
        self.print_instances(self.get_instances_with_auto_start())

    def get_instances_without_auto_start(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_NO_AUTOSTART)

    def print_instances_without_auto_start(self):
        self.print_instances(self.get_instances_without_auto_start())

    def get_instances_with_snapshot(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_HAS_SNAPSHOT)

    def print_instances_with_snapshot(self):
        self.print_instances(self.get_instances_with_snapshot())

    def get_instances_without_snapshot(self):
        return self.conn.listAllDomains(libvirt.VIR_CONNECT_LIST_DOMAINS_NO_SNAPSHOT)

    def print_instance_without_snapshot(self):
        self.print_instances(self.get_instances_without_snapshot())

    def print_instances(self, instances):
        if len(instances) != 0:
            for domain in instances:
                print domain.name()
        else:
            print "No instance found on hypervisor " + self.hyper_visor.get_host_name()

    #############################
    #       Lookup methods      #
    #############################
    def get_instance_by_id(self, instance_id):
        return self.conn.lookupByID(instance_id)

    def get_instance_by_name(self, instance_name):
        return self.conn.lookupByName(instance_name)

    def get_instance_by_uuid(self, instance_uuid):
        return self.conn.lookupByUUID(instance_uuid)
