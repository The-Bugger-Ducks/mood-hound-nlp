import pandas as pd


# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
def clear_data(df):
    before_format = df.shape
    before_null = df["review_text"].isnull().sum()
    before_duplicated = df["review_text"].duplicated(keep=False).sum()

    df = df.dropna()
    df["reviewer_birth_year"] = (
        df["reviewer_birth_year"]
        .apply(lambda x: str(x)[:-2] if x != "0" else "0")
        .astype("int16")
    )
    df.rename(
        columns={
            "overall_rating": "stars",
            "submission_date": "created_at",
            "review_text": "text",
        },
        inplace=True,
    )
    df = df[~df["text"].isna()].reset_index(drop=True)
    df = df[df["text"].str.contains("\w")]
    df = df[df["text"].str.len() > 3]
    df = df.drop_duplicates("text").reset_index(drop=True)
    df["created_at"] = pd.to_datetime(df["created_at"])

    print(
        "-----------------------------------------------------------------------------"
    )
    analysis_table = {
        "Formato do dataset": [before_format, df.shape],
        "Avaliações nulas": [before_null, df["text"].isnull().sum()],
        "Registros duplicados": [
            before_duplicated,
            df["text"].duplicated(keep=False).sum(),
        ],
    }
    analysis_table = pd.DataFrame(analysis_table)
    analysis_table.index = ["Antes das adaptações", "Depois das adaptações"]
    print(analysis_table)

    return df
