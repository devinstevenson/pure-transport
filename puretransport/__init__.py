__version__ = '0.1.2'

try:
    from .factory import transport_factory
except ImportError:
    pass
