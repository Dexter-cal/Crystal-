import nmap
from crystal.utils.logger import get_logger

logger = get_logger()

class NmapScanner:
    """
    A wrapper class for the Nmap port scanner.
    This class provides methods to scan hosts and parse the results into a
    structured format.
    """
    def __init__(self):
        try:
            self.port_scanner = nmap.PortScanner()
        except nmap.PortScannerError:
            logger.error("Nmap not found. Please ensure nmap is installed and in your PATH.")
            raise

    def scan(self, target, arguments='-sV -O'):
        """
        Performs an Nmap scan on the specified target.

        Args:
            target (str): The target host or IP address to scan.
            arguments (str): The Nmap command-line arguments to use for the scan.

        Returns:
            dict: A dictionary containing the structured scan results, or None if the scan fails.
        """
        logger.info(f"Starting Nmap scan on target: {target} with arguments: {arguments}")
        try:
            self.port_scanner.scan(hosts=target, arguments=arguments)
            return self._parse_results()
        except Exception as e:
            logger.error(f"An error occurred during the Nmap scan: {e}")
            return None

    def _parse_results(self):
        """
        Parses the raw Nmap scan results into a structured JSON-like dictionary.

        Returns:
            dict: A dictionary containing the parsed scan results.
        """
        parsed_results = {}
        for host in self.port_scanner.all_hosts():
            parsed_results[host] = {
                'hostname': self.port_scanner[host].hostname(),
                'state': self.port_scanner[host].state(),
                'os_matches': self.port_scanner[host].get('osmatch', []),
                'ports': []
            }
            for proto in self.port_scanner[host].all_protocols():
                ports = self.port_scanner[host][proto].keys()
                for port in sorted(ports):
                    port_info = self.port_scanner[host][proto][port]
                    parsed_results[host]['ports'].append({
                        'port': port,
                        'protocol': proto,
                        'state': port_info['state'],
                        'service': port_info.get('name', ''),
                        'product': port_info.get('product', ''),
                        'version': port_info.get('version', ''),
                        'extrainfo': port_info.get('extrainfo', ''),
                        'cpe': port_info.get('cpe', '')
                    })
        logger.info(f"Nmap scan finished. Found {len(parsed_results.keys())} host(s).")
        return parsed_results

# Example usage for testing
if __name__ == '__main__':
    scanner = NmapScanner()
    # Use scanme.nmap.org for a safe and legal target
    results = scanner.scan('scanme.nmap.org', arguments='-sV -p 22,80,443')
    import json
    print(json.dumps(results, indent=4))
