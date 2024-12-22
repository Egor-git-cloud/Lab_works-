class Employer():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return (self.name, self.id)

class Manager(Employer):
    def __init__(self, name, id, departament, **kwargs):
        super().__init__(name=name, id=id, **kwargs)
        self.departament = departament
    def manage_project(self):
        return (f'Проектом управляет {self.name}')

class Technician(Employer):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name=name, id=id, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return (f'{self.name} выполняет техническое обслуживание проекта')

class TechManager(Technician, Manager):
    name_list = []
    def __init__(self,  name, id, specialization, departament, **kwargs):
        super().__init__(name=name, id=id, specialization=specialization, departament=departament, **kwargs)

    @classmethod
    def add_employer(cls, name_employer):
        cls.name_employer = name_employer
        TechManager.name_list.append(cls.name_employer)
    @classmethod
    def get_team_info(cls):
        return cls.name_list

tech_manager = TechManager(name="Пупа", id=1, departament="VR", specialization="1")
manag = Manager(name="Лупа", id=2, departament="М")
tech = Technician(name="Конская", id=3, specialization="T")

tech_manager.add_employer(manag)
tech_manager.add_employer(tech)


print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())





