import platform
import getpass


class windows:
    @staticmethod
    def getosrelease():
        return str(platform.release())

    @staticmethod
    def getosversion():
        return str(platform.version())

    @staticmethod
    def getosprocesser():
        return str(platform.processor())

    @staticmethod
    def getosarchitecture():
        return str(platform.architecture())

    @staticmethod
    def getosusername():
        return str(getpass.getuser())


class macos:
    @staticmethod
    def getosrelease():
        return str(platform.release())

    @staticmethod
    def getosversion():
        return str(platform.mac_ver()[0])

    @staticmethod
    def getosprocessor():
        return str(platform.processor())

    @staticmethod
    def getosarchitecture():
        return str(platform.processor())


class linux:
    @staticmethod
    def getosdistro():
        return str(platform.linux_distribution())

    @staticmethod
    def getosrelease():
        return str(platform.release())

    @staticmethod
    def getosversion():
        return str(platform.dist()[1])

    @staticmethod
    def getosprocessor():
        return str(platform.processor())

    @staticmethod
    def getosarchitecture():
        return str(platform.machine())

    @staticmethod
    def getosusername():
        return str(getpass.getuser())
