import pandas as pd
import matplotlib.pyplot as plt
import pyspark.pandas as ps


def load_data(name):

    df = pd.read_csv(f'Data/{name}.csv', skiprows=24, encoding='latin2',delimiter=';', names=['year', 'month', 'day', f'temperature_{name}', 'flag'], header=0)
    df = ps.DataFrame(df)
    df[f'temperature_{name}'] = df[f'temperature_{name}'].str.replace(',','.').astype(float)
    df['date'] = ps.to_datetime(df[['year', 'month', 'day']])
    df.set_index('date',inplace=True)

    return df[f'temperature_{name}'].to_frame()


def main():

    df_d = load_data('Doksany')
    df_c = load_data('Churanov')

    df = df_d.join(df_c)


    #df_month = df.resample('Y').mean()
    #df.plot()
    #plt.show()
    print(df)

    # TODO regresy řád 1
    # TODO vyhlazení plovoucí průměry











if __name__ == '__main__':
    main()

