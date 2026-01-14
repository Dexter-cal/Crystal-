document.addEventListener('DOMContentLoaded', () => {

    const vulnscanForm = document.getElementById('vulnscan-form');
    const payloadForm = document.getElementById('payload-form');
    const toolForm = document.getElementById('tool-form');
    const outputPanel = document.getElementById('output-panel');

    // Helper function to display results
    const displayOutput = (data, isError = false) => {
        outputPanel.innerHTML = ''; // Clear previous output
        const pre = document.createElement('pre');
        if (isError) {
            pre.style.color = '#f7768e'; // Error color
            pre.textContent = JSON.stringify(data, null, 2);
        } else {
            pre.style.color = '#a9b1d6'; // Default text color
            pre.textContent = JSON.stringify(data, null, 2);
        }
        outputPanel.appendChild(pre);
    };

    const displayLoading = () => {
        outputPanel.innerHTML = '<p class="text-gray-500">Loading...</p>';
    };

    // VulnScan form handler
    vulnscanForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        displayLoading();

        const target = document.getElementById('vulnscan-target').value;
        const args = document.getElementById('vulnscan-args').value;

        try {
            const response = await fetch('/api/scan/start', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ target, arguments: args }),
            });
            const data = await response.json();
            displayOutput(data, !response.ok);
        } catch (error) {
            displayOutput({ error: error.message }, true);
        }
    });

    // Payload form handler
    payloadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        displayLoading();

        const lhost = document.getElementById('payload-lhost').value;
        const lport = parseInt(document.getElementById('payload-lport').value, 10);
        const type = document.getElementById('payload-type').value;
        const encode = document.getElementById('payload-encode').value;

        try {
            const response = await fetch('/api/payload/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ lhost, lport, type, encode }),
            });
            const data = await response.json();
            displayOutput(data, !response.ok);
        } catch (error) {
            displayOutput({ error: error.message }, true);
        }
    });

    // Tool form handler
    toolForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        displayLoading();

        const tool = document.getElementById('tool-name').value;
        const argsString = document.getElementById('tool-args').value;
        // Split arguments by space, respecting quoted strings
        const args = argsString.match(/\\"[^\\"]+\\"|[^\\s]+/g) || [];

        try {
            const response = await fetch('/api/tool/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ tool, args }),
            });
            const data = await response.json();
            // The tool output is often a raw string, not JSON, so handle it differently
            if (response.ok) {
                 outputPanel.innerHTML = `<pre>${data.output}</pre>`;
            } else {
                 displayOutput(data, true);
            }
        } catch (error) {
            displayOutput({ error: error.message }, true);
        }
    });
});
