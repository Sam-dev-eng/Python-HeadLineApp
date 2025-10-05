

class Doctor:
    DOCTORS = []
    def __init__(self, name, department, contact, time_of_work):
        self._name = name
        self._department = department
        self._contact = contact
        self._time_of_work = time_of_work
        self.DOCTORS.append(self)

    @property
    def department(self):
       return self._department
    @department.setter
    def department(self, value):
        self._department = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value

    @property
    def time_of_work(self):
        return self._time_of_work
    @time_of_work.setter
    def time_of_work(self, value):
        self._time_of_work = value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

