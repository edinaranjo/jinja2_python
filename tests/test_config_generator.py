from pathlib import Path

CONFIG_DIR = Path("configs")


# -----------------------------------------------------
# Verificar que exista el directorio configs
# -----------------------------------------------------

def test_directorio_configs():

    assert CONFIG_DIR.exists()


# -----------------------------------------------------
# Verificar que existan configuraciones generadas
# -----------------------------------------------------

def test_existen_archivos():

    archivos = list(CONFIG_DIR.glob("*.txt"))

    assert len(archivos) > 0


# -----------------------------------------------------
# Leer el primer archivo generado
# -----------------------------------------------------

def obtener_config():

    archivo = next(CONFIG_DIR.glob("*.txt"))

    return archivo.read_text()


# -----------------------------------------------------
# Verificar hostname
# -----------------------------------------------------

def test_hostname():

    config = obtener_config()

    assert "hostname" in config


# -----------------------------------------------------
# Verificar interfaz Loopback
# -----------------------------------------------------

def test_loopback():

    config = obtener_config()

    assert "interface Loopback0" in config


# -----------------------------------------------------
# Verificar IP de administración
# -----------------------------------------------------

def test_ip_mgmt():

    config = obtener_config()

    assert "ip address" in config


# -----------------------------------------------------
# Verificar helper addresses
# -----------------------------------------------------

def test_helper_addresses():

    config = obtener_config()

    assert "172.18.25.1" in config

    assert "172.18.26.2" in config

    assert "172.18.27.3" in config


# -----------------------------------------------------
# Verificar configuración Syslog
# -----------------------------------------------------

def test_syslog():

    config = obtener_config()

    assert "logging host" in config


# -----------------------------------------------------
# Verificar que termine con end
# -----------------------------------------------------

def test_end():

    config = obtener_config()

    assert config.strip().endswith("end")
