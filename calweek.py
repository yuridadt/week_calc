from datetime import datetime, timedelta


class CalWeek:
    """
    Class providing arithmetic operations for year-week date format
    """

    def __init__(self, year_week, format='%G-%V'):
        self.year, self.week = [int(val) for val in year_week.split('-')]

        if self.year < 1 or self.year > 9999:
            raise ValueError('Input year in the correct way')
        if self.week < 1 or self.week > 52:
            raise ValueError('Input week in the correct way')

        if format == '%G-%V':
            format = '%G-%V-%u'
            year_week = year_week + '-1'
        self.cur_date = datetime.strptime(year_week, format)
        self.form = format

    def __repr__(self):
        return datetime.strftime(self.cur_date, '%G-%V')

    def __add__(self, other):
        if isinstance(other, int):
            return datetime.strftime(self.cur_date + timedelta(weeks=other), '%G-%V')
        else:
            raise TypeError('Input weeks in numeric format')

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            return datetime.strftime(self.cur_date - timedelta(weeks=other), '%G-%V')
        elif isinstance(other, CalWeek):
            return (self.cur_date - other.cur_date).days // 7
        else:
            raise TypeError('Input weeks in numeric format')


if __name__ == '__main__':
    yw = CalWeek('2019-01')
    print(yw)
    print(str(yw))
    print(yw + 200)
    print(200 + yw)
    print(yw + (-100))
    print(yw - 100)
    print(yw - CalWeek('1000-01'))
