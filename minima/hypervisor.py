import libvirt


class HyperVisor:
    def __init__(self):
        self.conn = libvirt.open("qemu:///system")

        if not self.conn:
            print "Failed to open connection to qemu:///system"
            raise Exception("Connection failed")

    def print_host_info(self):
        print "Hostname: " + str(self.get_host_name())
        print "Free Memory: " + str(self.get_free_memory_in_bytes()) + " bytes"
        print "Max vCPUs: " + str(self.get_max_vcpus())
        print "Virtualization Type: " + str(self.get_virtualization_type())
        print "Version: " + str(self.get_version())
        print "Library Version: " + str(self.get_lib_version())
        print "Canonical URI: " + str(self.get_uri())
        print "Connection Encrypted: " + str(self.is_encrypted())
        print "Connection Secure: " + str(self.is_secure())
        print "\n"
        print "Node Info"
        print "----------"
        print "Model: " + str(self.get_node_model())
        print "Memory: " + str(self.get_node_memory_size_in_mb()) + "MB"
        print "NUMA nodes: " + str(self.get_node_number_of_numa_nodes())
        print "CPUs: " + str(self.get_node_number_of_cpus())
        print "CPU Frequency: " + str(self.get_node_mhz_of_cpus()) + "MHz"
        print "CPU Sockets: " + str(self.get_node_number_of_cpu_sockets())
        print "CPU Cores per Socket: " + str(self.get_node_number_of_cpu_cores_per_socket())
        print "CPU Threads per Core: " + str(self.get_node_number_of_cpu_threads_per_core())

    def get_connection(self):
        return self.conn

    def get_host_name(self):
        return self.conn.getHostname()

    def get_max_vcpus(self):
        return self.conn.getMaxVcpus(None)

    def get_node_info(self):
        return self.conn.getInfo()

    def get_node_model(self):
        return self.get_node_info()[0]

    def get_node_memory_size_in_mb(self):
        return self.get_node_info()[1]

    def get_node_number_of_cpus(self):
        return self.get_node_info()[2]

    def get_node_mhz_of_cpus(self):
        return self.get_node_info()[3]

    def get_node_number_of_numa_nodes(self):
        return self.get_node_info()[4]

    def get_node_number_of_cpu_sockets(self):
        return self.get_node_info()[5]

    def get_node_number_of_cpu_cores_per_socket(self):
        return self.get_node_info()[6]

    def get_node_number_of_cpu_threads_per_core(self):
        return self.get_node_info()[7]

    def get_cells_free_memory(self):
        num_nodes = self.get_node_number_of_numa_nodes()
        return self.conn.getCellsFreeMemory(0, num_nodes)

    def get_virtualization_type(self):
        return self.conn.getType()

    def get_version(self):
        return self.conn.getVersion()

    def get_lib_version(self):
        return self.conn.getLibVersion()

    def get_uri(self):
        return self.conn.getURI()

    def is_encrypted(self):
        return self.conn.isEncrypted()

    def is_secure(self):
        return self.conn.isSecure()

    def is_alive(self):
        return self.conn.isAlive()

    def get_free_memory_in_bytes(self):
        return self.conn.getFreeMemory()

    def get_free_pages(self):
        return self.conn.getFreePages()

    def get_memory_parameters(self):
        return self.conn.getMemoryParameters()

    def get_memory_stats(self):
        return self.conn.getMemoryStats(libvirt.VIR_NODE_MEMORY_STATS_ALL_CELLS)

    def get_security_model(self):
        return self.conn.getSecurityModel()

    def get_sys_info(self):
        return self.conn.getSysinfo()

    def get_cpu_map(self):
        return self.conn.getCPUMap()

    def get_cpu_stats(self):
        return self.conn.getCPUStats()

    def get_cpu_model_names(self):
        return self.conn.getCPUModelNames('x86_64')
