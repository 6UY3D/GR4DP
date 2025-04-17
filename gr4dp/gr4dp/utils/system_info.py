import platform

def get_system_info():
    return {
        "platform": platform.system(),
        "release": platform.release(),
        "version": platform.version()
    }
