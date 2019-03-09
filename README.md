# pure-pyhive
Provides a thrift_transport for use with hive connections with PyHive by defaulting to Pure-SASL.

# Why 
PyHive relies on the sasl library for hive connections, but allows the user to optionally provide thier own thrift_transport instead of relying on the PyHive to create it. The main use case for this is Windows users where the sasl library is extremely difficult to compile from source. 

The other main use case for providing your own thrift_transport is to use other socket types, such as SSL.

The pure-pyhive has basic support for using SSL sockets in the thrift transport.


### Examples

See examples folder


### Installation

clone repo and run 
```python setup.py install```

or 

```pip install pure-pyhive```

### Dependencies
```
PyHive - you will need to install separately
pure-sasl
thrift
thrift_sasl
```

### Caveats

When using a SQLAlchemy engine, it will automatically pass a port number of 10000 to the hive connection even if you explicitly do not put a port number in your connection string.

PyHive has an assertion that will not allow the keyword arguments `[host, port, auth, kerberos_service_name, password]` to have any other values besides `None` if a `thrift_transport` is specified. So using SQLAlchemy engine will raise a `ValueError`.

I see this assertion to be pointless, as providing any of these keywords will have no effect if a `thift_transport` is specified. 

I recommend editing your `hive.py` file to comment out this part on lines 135-137 (as of version 0.6.1) if you want to use SQLAlchemy.
```
    if has_incompatible_arg:
        raise ValueError("thrift_transport cannot be used with "
                         "host/port/auth/kerberos_service_name/password")
```

# Contributions

Contributions Welcome. 
