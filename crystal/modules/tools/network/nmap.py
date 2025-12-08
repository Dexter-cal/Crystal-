from crystal.modules.tools.runner import ToolRunner

class Nmap:
    """
    A simple wrapper for the 'nmap' command-line tool.
    This provides a direct way to run nmap with custom arguments,
    as opposed to the structured scanning of the vulnscan module.
    """
    def __init__(self):
        self.runner = ToolRunner()

    def run(self, args):
        """
        Runs nmap with the given arguments.

        Args:
            args (list of str): The arguments to pass to nmap (e.g., ['-sV', '-p', '80', 'scanme.nmap.org']).

        Returns:
            A tuple containing (output, error).
        """
        return self.runner.run('nmap', args)
