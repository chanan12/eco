import pandas as pd


def load_data():
    return pd.read_csv("eco.csv")


def process_eco_value(df):
    years = [c for c in df.columns if c != "Country Code"]
    p = pd.melt(df, id_vars=["Country Code"], value_vars=years,
                var_name="Year",
                value_name="eco"
                )
    return p

def get_processsed_data():
    """
    Entry point for the dash app to get the data to display.
    :return:
    """
    df = load_data()
    return process_eco_value(df)


if __name__ == "__main__":
    df = load_data()
    print(
        process_eco_value(df)
    )
