# Seguração

## Proteger o acesso do Admin

# Bloqueia acesso ao /api/admin
<code>
    <Location "/api/admin">
        Require all denied
    </Location>

    <LocationMatch "^/api/admin/">
        Require all denied
    </LocationMatch>
</code>