
import ldap

LDAP_SERVER = "ldap://localhost"
BASE_DN = "dc=example,dc=org"
ADMIN_DN = "cn=admin,dc=example,dc=org"
PASSWORD = "admin"

try:
    # Połączenie z serwerem LDAP
    conn = ldap.initialize(LDAP_SERVER)
    conn.simple_bind_s(ADMIN_DN, PASSWORD)
    print("Połączono z serwerem LDAP!")

    # Wyszukaj użytkowników
    search_filter = "(objectClass=inetOrgPerson)"
    search_attributes = ["cn", "sn", "mail"]
    results = conn.search_s(BASE_DN, ldap.SCOPE_SUBTREE, search_filter, search_attributes)

    # Wyświetl wyniki
    for dn, entry in results:
        print(f"DN: {dn}")
        for attr, values in entry.items():
            print(f"  {attr}: {values}")
except ldap.LDAPError as e:
    print(f"Błąd LDAP: {e}")
finally:
    conn.unbind()
