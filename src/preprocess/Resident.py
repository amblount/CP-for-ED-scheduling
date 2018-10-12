class Resident:
    def __init__(self, id, consec_days_worked):
        self.id = id
        self.csec_days = consec_days_worked
        self.last_day_worked = 0
        self.next_working_day = 0

    def add_day(self):
        self.csec_days += 1

    def days_constraint(self):
        if self.csec_days == 7:
            reset_csec_days()
            return('already worked 7 consecutive days')

    def reset_csec_days(self):
        self.csec_days = 0
        self.next_working_day = self.last_day_worked + 1
        
