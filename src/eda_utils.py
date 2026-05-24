def calculate_loss_ratio(df):
    return df["TotalClaims"].sum() / df["TotalPremium"].sum()


def calculate_margin(df):
    return df["TotalPremium"] - df["TotalClaims"]


def missing_values_table(df):
    missing = df.isnull().sum()
    percent = (missing / len(df)) * 100

    return percent.sort_values(ascending=False)