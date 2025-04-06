class Date:
    def __init__(self, time: str):
        self.time: str = time
        [year, month, days] = self._parse_date(time)
        self._validation(year, month, days)
        all_days = self._days_zero_point(year, month, days)
        self.all_days: int = all_days



    def add_days(self, days: int):
        self.all_days += days

        return self._return_time(self.all_days)

    def add_month(self, month: int):
        pass

    def add_years(self, year: int) -> int:
        pass

    def _days_zero_point(self, year: int, month: int, days: int,
    ) -> int:  
        all_days = 0

        all_days += days

        for i in range(1, month):
            all_days += self._days_month(i, year)

        for i in range(0, year):
            all_days += self._days_year(i)

        return all_days
    
    def _return_time(self, all_days: int) -> str:
        years = 0
        months = 1

        while all_days > self._days_year(years):
            all_days -= self._days_year(years)
            years += 1

        while all_days > self._days_month(months, years):
            all_days -= self._days_month(months, years)
            months += 1
        if months < 10:
            months = "0" + str(months)
        if all_days < 10:
            all_days = "0" + str(all_days)

        self.time = f"{years}-{months}-{all_days}"

        return  self.time
            
    def _parse_date(self, time: str) -> list[int]:
        try:
            year = int(time.split("-")[0])
            month = int(time.split("-")[1])
            days = int(time.split("-")[2])
        except:
            raise TypeError("Не верный формат даты!")

        return [year, month, days]

    def _validation(self, year: int, month: int, days: int):
        if 0 > year > 9999:
            raise ValueError("Дата не входит в допустимые границы")
        if 1 > month > 12:
            raise ValueError("Дата не входит в допустимые границы")
        if days > self._days_month(month, year) < 1:
            raise ValueError("Дата не входит в допустимые границы")

    def _high_year(self, year):  # проверка на високосный год
        if year // 400 == 0:
            return True
        elif year / 4 * 10 % 10 == 0:
            return True
        else:
            return False

    def _days_month(
        self, month, year
    ):  # высчитывает кол. дней в месяце и прибавляет если високосный
        list_days_in_a_month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        days = list_days_in_a_month[month]
        if self._high_year(year) and month == 2:
            return days + 1
        else:
            return days

    def _days_year(self, year) -> int:  # кол. дней в году
        if self._high_year(year):
            return 366
        else:
            return 365


