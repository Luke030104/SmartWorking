import pandas as pd
import bar_chart_race as bcr

df = pd.read_csv('smart_working.csv').set_index('date')

bcr.bar_chart_race(df=df, filename='sw.html', title='Smart Working')


