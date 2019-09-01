import twint

c = twint.Config()
c.User_full = True
c.Search = "#HeadCount OR #deepmurder OR #shaft OR #hampstead OR #vault since:2019-06-14 until:2019-06-16"
c.Output = "Test2.csv"
c.Limit = 10000
c.Store_csv = True
c.Lang = "en"

twint.run.Search(c)

