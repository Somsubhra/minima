class Instance:

    def __init__(self, hyper_visor):
        self.hyper_visor = hyper_visor
        self.conn = hyper_visor.get_connection()

    def print_all_domains(self):
        domains = self.get_all_domains()

        if len(domains) != 0:
            for domain in domains:
                print domain.name()
        else:
            print "No instances found on hypervisor " + self.hyper_visor.get_host_name()

    def get_all_domains(self):
        return self.conn.listAllDomains(0)
