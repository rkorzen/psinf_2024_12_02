from ldap3 import Server, Connection, MOCK_SYNC
from ldap3.core.exceptions import LDAPException

# Tworzenie serwera LDAP w trybie mock
server = Server('my_fake_ldap_server', get_info=MOCK_SYNC)
conn = Connection(server, user='cn=admin,dc=example,dc=com', password='password', client_strategy=MOCK_SYNC)

# Dodanie danych
conn.bind()
conn.add('cn=John Doe,ou=users,dc=example,dc=com', ['inetOrgPerson'], {'sn': 'Doe', 'cn': 'John Doe'})
print(conn.entries)
