# Inventory rules

In this first step inventory file is structured in a YAML file.
inventory.yaml or dev-inventory.yaml for dev purporse

Required field in the inventory :
- hostname
- ip
- site
- role

Optional field :
- vendor
- os_type
- os_version

Validation criteria :
- hostname should not contain not allowed character
- ip must be a valid IPv4
- site is a single word (e.g. lab, home, dc2)
- role must be one of the allowed value (e.g. core, access, distribution, firewall, router)

