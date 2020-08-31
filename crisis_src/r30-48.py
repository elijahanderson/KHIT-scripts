import pandas as pd


def r30_48():
    filename = 'C:/Users/mingus/Documents/r30-48n.csv'

    df = pd.read_csv('C:/Users/mingus/Documents/r30-48.csv')
    df.sort_values(by=['full_name', 'actual_date'], inplace=True)
    df = df[df.duplicated(subset=['full_name'], keep=False)]
    df = df.reset_index()

    by_client = df.groupby('full_name')
    for client, frame in by_client:
        if 'Crisis Screening Services' not in frame['program_name'].values:
            print(frame['program_name'])
            df = df.drop(frame['program_name'].index)

    df.to_csv(filename, index=False)


r30_48()
