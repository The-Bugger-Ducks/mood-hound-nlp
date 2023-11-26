# =============================================================================
# Acessando os dados disponibilizados
# =============================================================================
import pandas as pd


def access_data():
    dtype = {
        "submission_date": "str",
        "product_id": "category",
        "product_name": "str",
        "overall_rating": "int8",
        "review_text": "object",
        "reviewer_birth_year": "str",
        "reviewer_state": "category",
        "reviewer_gender": "category",
    }
    use_cols = list(dtype.keys())

    url = "https://raw.githubusercontent.com/americanas-tech/b2w-reviews01/main/B2W-Reviews01.csv"
    df = pd.read_csv(
        url,
        sep=",",
        dtype=dtype,
        usecols=use_cols,
        parse_dates=["submission_date"],
        low_memory=False,
    )

    return df
