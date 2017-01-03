import libvirt
import time


class InstanceService:

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

    ##############################
    #     Details methods        #
    ##############################
    @staticmethod
    def get_instance_id(instance):
        return instance.ID()

    @staticmethod
    def get_instance_uuid(instance):
        return instance.UUIDString()

    @staticmethod
    def get_instance_os_type(instance):
        return instance.OSType()

    @staticmethod
    def instance_has_snapshot(instance):
        return instance.hasCurrentSnapshot()

    @staticmethod
    def instance_has_managed_save_image(instance):
        return instance.hasManagedSaveImage()

    @staticmethod
    def get_instance_name(instance):
        return instance.name()

    @staticmethod
    def get_instance_hostname(instance):
        return instance.hostname()

    @staticmethod
    def get_instance_hardware_info(instance):
        state, max_memory, memory, cpus, cpu_time = instance.info()
        return {
            "state": state,
            "max_memory": max_memory,
            "memory": memory,
            "cpus": cpus,
            "cpu_time": cpu_time
        }

    @staticmethod
    def get_instance_hardware_state(instance):
        return InstanceService.get_instance_hardware_info(instance)["state"]

    @staticmethod
    def get_instance_max_memory(instance):
        return InstanceService.get_instance_hardware_info(instance)["max_memory"]

    @staticmethod
    def get_instance_memory(instance):
        return InstanceService.get_instance_hardware_info(instance)["memory"]

    @staticmethod
    def get_instance_cpus(instance):
        return InstanceService.get_instance_hardware_info(instance)["cpus"]

    @staticmethod
    def get_instance_cpu_time(instance):
        return InstanceService.get_instance_hardware_info(instance)["cpu_time"]

    @staticmethod
    def is_instance_active(instance):
        return instance.isActive()

    @staticmethod
    def is_instance_persistent(instance):
        return instance.isPersistent()

    @staticmethod
    def is_instance_updated(instance):
        return instance.isUpdated()

    @staticmethod
    def get_instance_state(instance):
        return instance.state()

    @staticmethod
    def get_instance_current_time(instance):
        struct = instance.getTime()
        return time.ctime(float(struct['seconds']))
