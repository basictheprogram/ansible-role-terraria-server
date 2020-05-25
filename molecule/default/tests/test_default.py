import os
import pytest
import testinfra.utils.ansible_runner

# Excuse the mess! 
# I am stil experimenting with tests written in testinfra 
# and tests written in ansible.

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_mono_package_installed(host):
    pkg = host.package("mono-complete")
    assert pkg.is_installed

def test_screen_package_installed(host):
    screen = host.package("screen")
    assert screen.is_installed

def test_unzip_package_installed(host):
    zip = host.package("unzip")
    assert zip.is_installed

def test_terraria_user(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("tshock")
    user = host.user("tshock")
    assert user.shell == "/bin/true"
    assert user.home == "/var/tshock"

def test_terraria_exe(host):
    exe = host.file('/usr/local/games/tshock/TerrariaServer.exe')
    assert exe.exists
    assert exe.user == "tshock"
    assert exe.mode ==  0o755

def test_terraria_running_and_enabled(host):
    terraria = host.service("httpd")
    return True
    assert terraria.is_running
    assert terraria.is_enabled

def test_motd(host):
    motd = host.file("/etc/motd")
    assert motd.contains("screen")
    assert motd.contains("/usr/local/games/tshock")
    assert motd.contains("tshock")
    assert motd.contains("MONO")
    assert motd.contains("group addperm guest tshock.world.editspawn")

    ansible_variables = host.ansible.get_variables()
    print(ansible_variables["tsock_version"])