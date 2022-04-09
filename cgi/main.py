from PyPDF2 import PdfFileMerger


def main():
    base = '/Users/tuecuong/Downloads/Temp/Rubix'

    # The output of this command in base folder: ls -1 -rt */*
    ls_pdfs = '''
Starting/Getting Started.pdf
Starting/Authorization.pdf
Starting/Cluster Configuration.pdf
Starting/Scheduled Node Updates.pdf
Starting/Cluster Notifications.pdf
Starting/Compliance.pdf
Starting/Cluster Access.pdf
Starting/IAM roles for service accounts.pdf
Starting/Cluster OIDC Management (Admin).pdf
Starting/OIDC End-User Access Management.pdf
Starting/IAM FAQ .pdf
Starting/CloudWatch Logs.pdf
Starting/Kubernetes Events.pdf
Starting/Rubix Control Plane Logs.pdf
Monitoring/Kubernetes Dashboard Access.pdf
Monitoring/Prometheus Access.pdf
Networking/Network Policies.pdf
Networking/Required Connectivity.pdf
Networking/AWS Load Balancers.pdf
Networking/Expose Service via Denali.pdf
Networking/Ingress Nginx Controller.pdf
Networking/TLS termination.pdf
Networking/Elastic Fabric Adapter (EFA).pdf
Networking/Egress Proxy.pdf
'''.strip()
    pdfs = [f"{base}/{file}" for file in ls_pdfs.split('\n')]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()


if __name__ == '__main__':
    main()
