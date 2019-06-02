import json
import os
import sys

from ipykernel.kernelbase import Kernel
from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

class EchoKernel(Kernel):
    implementation = 'Echo'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "Echo kernel - as useful as a parrot"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            stream_content = {'name': 'stdout', 'text': code}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

MU_REPL_KERNEL_JSON = {
    "argv": [sys.executable, "-m", "mu.modes.python3replrun", "-f", "{connection_file}"],
    "display_name": "Echo",
}



def register_repl_kernel():
    with TemporaryDirectory() as td:
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(MU_REPL_KERNEL_JSON, f, sort_keys=True)
        KernelSpecManager().install_kernel_spec(td, 'echo', user=True)


def unregister_repl_kernel():
    KernelSpecManager().remove_kernel_spec('echo')

