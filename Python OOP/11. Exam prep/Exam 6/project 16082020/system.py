from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
      #  software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        try:
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
     #   software = LightSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        try:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]

            hardware.uninstall(software)
            System._software.remove(software)

        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        used_memory = sum([s.memory_consumption for s in System._software])
        used_capacity = sum([s.capacity_consumption for s in System._software])
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])

        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {int(used_memory)} / {int(total_memory)}\n"
        result += f"Total Capacity Taken: {int(used_capacity)} / {int(total_capacity)}"

        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            number_express = len([s for s in h.software_components if s.software_type == "Express"])
            number_light = len([s for s in h.software_components if s.software_type == "Light"])
            used_memory = sum([s.memory_consumption for s in h.software_components])
            used_capacity = sum([s.capacity_consumption for s in h.software_components])
            all_software = ', '.join([s.name for s in h.software_components])

            result += f"Hardware Component - {h.name}\n"
            result += f"Express Software Components: {number_express}\n"
            result += f"Light Software Components: {number_light}\n"
            result += f"Memory Usage: {int(used_memory)} / {int(h.memory)}\n"
            result += f"Capacity Usage: {int(used_capacity)} / {int(h.capacity)}\n"
            result += f"Type: {h.hardware_type}\n"
            if h.software_components:
                result += f"Software Components: {all_software}\n"
            else:
                result += f"Software Components: 'None'\n"
        return result