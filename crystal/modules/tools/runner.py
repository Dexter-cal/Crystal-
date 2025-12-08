import subprocess
from crystal.utils.logger import get_logger

logger = get_logger()

class ToolRunner:
    """
    A generic wrapper for running external command-line tools.
    """
    def run(self, command, args=None):
        """
        Executes a command-line tool with the given arguments.

        Args:
            command (str): The name of the command to execute (e.g., 'whois').
            args (list of str, optional): A list of arguments to pass to the command.

        Returns:
            tuple: A tuple containing (output, error).
                   Returns (None, "Error message") if the command is not found.
        """
        if args is None:
            args = []

        full_command = [command] + args
        logger.info(f"Executing tool: {' '.join(full_command)}")

        try:
            process = subprocess.Popen(
                full_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(timeout=60) # 60-second timeout

            if process.returncode != 0:
                logger.error(f"Tool '{command}' exited with error code {process.returncode}: {stderr.strip()}")
                return None, stderr.strip()

            return stdout.strip(), None

        except FileNotFoundError:
            logger.error(f"Command not found: {command}. Please ensure it is installed and in your PATH.")
            return None, f"Command not found: {command}"
        except subprocess.TimeoutExpired:
            logger.error(f"Command '{command}' timed out after 60 seconds.")
            process.kill()
            return None, "Command timed out."
        except Exception as e:
            logger.error(f"An unexpected error occurred while running '{command}': {e}")
            return None, f"An unexpected error occurred: {e}"

# Example usage for testing
if __name__ == '__main__':
    runner = ToolRunner()

    print("--- Testing whois ---")
    output, error = runner.run('whois', ['google.com'])
    if error:
        print(f"Error: {error}")
    else:
        print(f"Output:\n{output}")

    print("\n--- Testing nmap ---")
    # Using nmap's fast scan on a safe target
    output, error = runner.run('nmap', ['-F', 'scanme.nmap.org'])
    if error:
        print(f"Error: {error}")
    else:
        print(f"Output:\n{output}")

    print("\n--- Testing invalid command ---")
    output, error = runner.run('not_a_real_command')
    if error:
        print(f"Error: {error}")
    else:
        print(f"Output:\n{output}")
