#黛灰が何日生きているか
import datetime

bd = datetime.date(1998,9,28)
today = datetime.date.today()
now = today - bd

print("今日も",now.days,"日、生きててえらいよ黛",sep='')
