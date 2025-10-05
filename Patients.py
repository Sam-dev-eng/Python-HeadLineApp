
class Patient:
    Pateints = []
    def __init__(self, name, age, contact,reason):
        self._name = name
        self._age = age
        self._contact = contact
        self._reason = reason
        self._doctors = ""
        self._status = ""
        self.Pateints.append(self)

    @property
    def age(self):
       return self._department
    @age.setter
    def age(self, value):
        self._department = value

    @property
    def reason(self):
        return self._reason
    @reason.setter
    def reason(self, value):
        self._reason = value


    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value

    @property
    def doctor(self):
        return self._time_of_work
    @doctor.setter
    def doctor(self, value):
        self._time_of_work = value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value


    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

