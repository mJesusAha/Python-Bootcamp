import threading, time, random


class DoctorHands:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand
        self.right_hand = right_hand


class Doctors:
    rlock1 = threading.RLock()  # Функция блокировки повторного получения
    rlock2 = threading.RLock()
    rlock3 = threading.RLock()
    rlock4 = threading.RLock()
    rlock5 = threading.RLock()
    Doctor1 = DoctorHands(rlock5, rlock1)
    Doctor2 = DoctorHands(rlock1, rlock2)
    Doctor3 = DoctorHands(rlock2, rlock3)
    Doctor4 = DoctorHands(rlock3, rlock4)
    Doctor5 = DoctorHands(rlock4, rlock5)


class start_t:
    def run(Doctor, name):
        time.sleep(random.randint(0, 10) / 10)
        f = Doctor.left_hand.acquire()
        ff = Doctor.right_hand.acquire()  # ставит блокировку
        if ff or f:
            #  Получить вилку вторую
            print(name, ": BLAST!", sep="")
        Doctor.right_hand.release()  # снимает блокировку
        Doctor.left_hand.release()  # снимает блокировку

    def startT(name_, Doctor):
        return threading.Thread(target=start_t.run, args=(Doctor, name_)).start()


if __name__ == "__main__":
    start_t.startT("Doctor 9", Doctors.Doctor1)
    start_t.startT("Doctor 10", Doctors.Doctor2)
    start_t.startT("Doctor 11", Doctors.Doctor3)
    start_t.startT("Doctor 12", Doctors.Doctor4)
    start_t.startT("Doctor 13", Doctors.Doctor5)
