class Solution:
    def dayOfYear(self, date: str) -> int:
        date_main = date.split("-")
        days_of_months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        def CheckLeap(Year):
            if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
                return True
        if CheckLeap(int(date_main[0])) == True:
            days_of_months = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        months_dict = {}
        for x, y in enumerate(days_of_months):
            months_dict[x + 1] = y
        month_number = int(date_main[1])
        used_days = months_dict[month_number]
        current_days = int(date_main[2])
        return used_days + current_days
        