"""
Provides for custom transport for Hive connections

"""
from __future__ import unicode_literals
import os
import sys
import ssl
from thrift.transport.TSSLSocket import TSSLSocket
from thrift.transport.TSocket import TSocket
import thrift_sasl


def transport_factory(host, port, username, password, **kwargs):
    """
    Creates a thrift_sasl transport for use with HIVE/PyHive. Only pass this object
    to PyHive connection.
    :param host: str
    :param port: int/str
    :param username: str
    :param password: str
    :param kwargs: optional
        use_ssl=True will use a SSL socket with validate=False, default is False
        socket_kwargs={}, pass custom kwargs to SSL socket
    :return:
    """
    sasl_auth = 'PLAIN'
    use_ssl = kwargs.get('use_ssl', False)
    socket_kwargs = kwargs.get('socket_kwargs')
    if use_ssl:
        if socket_kwargs:
            socket = TSSLSocket(host, port, **socket_kwargs)
        else:
            socket = TSSLSocket(host, port, cert_reqs=ssl.CERT_NONE)
    else:
        socket = TSocket(host, port)  # basic socket

    if os.name == 'posix':
        import sasl

        def sasl_factory():
            sasl_client = sasl.Client()
            sasl_client.setAttr('host', host)
            if sasl_auth == 'GSSAPI':
                sasl_client.setAttr('service', kerberos_service_name)
            elif sasl_auth == 'PLAIN':
                sasl_client.setAttr('username', username)
                sasl_client.setAttr('password', password)
            else:
                raise AssertionError
            sasl_client.init()
            return sasl_client

        # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        # socket = TSSLSocket(host, port, ssl_context=ssl_context)

    elif sys.platform == 'win32' or sys.platform == 'cygwin':
        from sasl_compat import PureSASLClient

        def sasl_factory():
            return PureSASLClient(host, username=username, password=password,
                                  service=kerberos_service_name, mechanism=sasl_auth)

    else:
        raise NotImplementedError("transport not supported for this platform")

    transport = thrift_sasl.TSaslClientTransport(sasl_factory, sasl_auth, socket)
    return transport



