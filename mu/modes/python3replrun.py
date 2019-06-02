if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    from . python3repl import EchoKernel
    IPKernelApp.launch_instance(kernel_class=EchoKernel)
