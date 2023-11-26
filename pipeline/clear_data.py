# =============================================================================
# Análise exploratória e adaptações
# =============================================================================
import pandas as pd
from datetime import datetime
from storage import update_stats
from timeit import timeit


def clear_data(df):
    df_after = df

    try:
        df_after.rename(
            columns={
                "overall_rating": "stars",
                "submission_date": "created_at",
                "review_text": "text",
            },
            inplace=True,
        )
        df_after["processed_at"] = datetime.now()
        df_after = df_after[~df_after["text"].isna()].reset_index(drop=True)
        df_after = df_after[df_after["text"].str.contains("\w")]
        df_after = df_after[df_after["text"].str.len() > 3]
        df_after = df_after.drop_duplicates("text").reset_index(drop=True)
        df_after["created_at"] = pd.to_datetime(df_after["created_at"])
        df_after = df_after.drop(
            columns=[
                "reviewer_id",
                "product_brand",
                "site_category_lv1",
                "site_category_lv2",
                "review_title",
                "recommend_to_a_friend",
            ]
        )

    except Exception as e:
        if e:
            print(str(e))
        elif df_after["text"].isnull() and df_after["stars"].isnull():
            print("Há nulos no df")

    analysis_table = {
        "Formato do dataset": [df.shape, df_after.shape],
        "Avaliações nulas": [
            int(df["text"].isnull().sum()),
            int(df_after["text"].isnull().sum()),
        ],
        "Registros duplicados": [
            int(df["text"].duplicated(keep=False).sum()),
            int(df_after["text"].duplicated(keep=False).sum()),
        ],
    }

    analysis_table = pd.DataFrame(analysis_table)
    analysis_table.index = ["Antes das adaptações", "Depois das adaptações"]
    print(
        "-----------------------------------------------------------------------------"
    )
    print(analysis_table)

    index = ["prior_adaptation ", "after_adaptation"]

    data_analysis_table = {
        "clear_data_statistics": {
            "format_of_the_dataset": dict(zip(index, ([df.shape, df_after.shape]))),
            "null_evaluations": dict(
                zip(
                    index,
                    [
                        int(df["text"].isnull().sum()),
                        int(df_after["text"].isnull().sum()),
                    ],
                )
            ),
            "duplicate_records": dict(
                zip(
                    index,
                    [
                        int(df["text"].duplicated(keep=False).sum()),
                        int(df_after["text"].duplicated(keep=False).sum()),
                    ],
                )
            ),
        }
    }
    update_stats(data_analysis_table)

    return df_after
