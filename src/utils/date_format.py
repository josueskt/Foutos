import datetime
class date_format():
    def convert(self,date):
     return datetime.datetime.strptime(date, '%d/%m/%y')