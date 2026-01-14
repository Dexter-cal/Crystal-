from crystal.modules.tools.runner import ToolRunner

class Whois:
    """
    A simple wrapper for the 'whois' command-line tool.
    """
    def __init__(self):
        self.runner = ToolRunner()

    def run(self, domain):
        """
        Performs a whois lookup on the given domain.

        Args:
            domain (str): The domain to look up.

        Returns:
            A tuple containing (output, error).
        """
        return self.runner.run('whois', [domain])
