class Shift:
    def __init__(self, shift_id, facility_number, shift_time_id, resident_num):
        self.id = shift_id
        self.facility_num = facility_number
        self.time_id = shift_time_id
        self.resident_num = resident_num
        self.shift_num = 0
        self.facility_name = ''

    def update_shift_num(self):
        index = {
            1: 111,
            2: 121,
            3: 211,
            4: 212,
            5: 213,
            6: 214,
            7: 221,
            8: 231,
            9: 232,
            10: 233,
            11: 234,
            12: 241,
            13: 242,
            14: 243,
            15: 244,
            16: 311,
            17: 321,
            18: 331,
            19: 411,
            20: 412,
            21: 413,
            22: 421,
            23: 431,
            24: 441,
            25: 442,
            26: 443,
            27: 451,
            28: 461,
            29: 462
            30: 463
        }
        self.shift_num = index[self.id]


    def add_facility_name(self):
        if self.shift_num[0] == 1:
            self.facility_name = 'ZSFGPEM'

        elif self.shift_num[0] == 2:
            self.facility_name = 'ZFFGED'

        elif self.shift_num[0] == 3:
            self.facility_name = 'Mission Bay'

        else:
            self.facility_name = 'Moffitt'
