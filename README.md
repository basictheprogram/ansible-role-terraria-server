# Ansible Role: Terraria Server

# Role Name #
Installs Terraria Server on Ubuntu servers.

## Requirements ##
None.

## Role Variables ##
Available variables are listed below, along with default values (see `defaults/main.yml`):

  tshock_url: "https://github.com/NyxStudios/TShock/releases/download"

The base url for the terraria server zip file.

  tshock_version: "4.3.26"

The version of the terraria server zip file to download.

  tshock_filename: "tshock-{{ tshock_version }}.zip"

The filename of the terraria server zip file.

  tshock_download: "{{ tshock_url }}/v{{ tshock_version }}/{{ tshock_filename }}"

The full uri of the terraria server zip file to download.

## Dependencies ##
None.

## Example Playbook ##
```yaml
- hosts: terraria_server
  vars:
    tsock_version: "4.3.26"

  roles:
    - { role: basictheprogram.terraria_server, become: yes }
```

## License ##
BSD, MIT

## Author Information ##
[Bob Tanner](https://github.com/basictheprogram)
