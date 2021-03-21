from utils.judete import Judete
from utils.person import Person
from utils.vaccin import Vaccinuri


class Configuration:
    # To modify
    cookie = "SESSION=as65fd4a6s5df4g6a54sf6g5a4"
    persoane = {
        'demo': Person('1234567890123', '1234567')
    }

    looking_for_judet = Judete.B.value
    looking_for_vaccin = Vaccinuri.PFIZER.value
    looking_for_person = persoane['demo']
    # or
    # looking_for_person = Person('1234567890123', '1234567')

    # Basically don't touch
    search_url = 'https://programare.vaccinare-covid.gov.ro/scheduling/api/centres?sort=true'
    appointment_url = f'https://programare.vaccinare-covid.gov.ro/#/appointment/new/{looking_for_person.recipient_id}'
    time_to_wait_success = 500
