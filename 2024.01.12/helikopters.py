class attackhelicopter:
    def __init__(self, type, id, crew_size, first_deploy, sensors, missles):
        self.type = type
        self.id = id
        self.crew_size = crew_size
        self.first_deploy = first_deploy
        self.sensors = sensors
        self.missles = missles

first_type = attackhelicopter("Ah-64 Apache helikopter","234240", "2", "2023.06.16.", "night vision és target acquisition", "AGM-114 Hellfire és Hydra 70 rakétatárolókkal")     
sec_tpye = attackhelicopter("OH-58 Kiowa helikopter", "534532", "2", "2022.10.10.", "target acquisition és laser designation", "")

print(first_type.id)