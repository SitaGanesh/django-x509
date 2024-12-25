from django.conf import settings

DEFAULT_CERT_VALIDITY = getattr(settings, 'DJANGO_X509_DEFAULT_CERT_VALIDITY', 365)
DEFAULT_CA_VALIDITY = getattr(settings, 'DJANGO_X509_DEFAULT_CA_VALIDITY', 3650)
DEFAULT_KEY_LENGTH = str(getattr(settings, 'DJANGO_X509_DEFAULT_KEY_LENGTH', '2048'))
DEFAULT_DIGEST_ALGORITHM = getattr(
    settings, 'DJANGO_X509_DEFAULT_DIGEST_ALGORITHM', 'sha256'
)
CA_BASIC_CONSTRAINTS_CRITICAL = getattr(
    settings, 'DJANGO_X509_CA_BASIC_CONSTRAINTS_CRITICAL', True
)
CA_BASIC_CONSTRAINTS_PATHLEN = getattr(
    settings, 'DJANGO_X509_CA_BASIC_CONSTRAINTS_PATHLEN', 0
)
CA_KEYUSAGE_CRITICAL = getattr(settings, 'DJANGO_X509_CA_KEYUSAGE_CRITICAL', True)
CA_KEYUSAGE_VALUE = getattr(
    settings, 'DJANGO_X509_CA_KEYUSAGE_VALUE', 'cRLSign, keyCertSign'
)
CERT_KEYUSAGE_CRITICAL = getattr(settings, 'DJANGO_X509_CERT_KEYUSAGE_CRITICAL', False)
CERT_KEYUSAGE_VALUE = getattr(
    settings, 'DJANGO_X509_CERT_KEYUSAGE_VALUE', 'digitalSignature, keyEncipherment'
)  # noqa
CRL_PROTECTED = getattr(settings, 'DJANGO_X509_CRL_PROTECTED', False)
DJANGO_X509_CA_MODEL = 'django_x509.Ca'  # Adjust the model if necessary