import polars as pl
from typing import Collection, Iterable, List, Tuple, Optional

class ParseJson:
    """Class to interact and flatten json in Polars DataFrame
    """
    def __init__(
        self,
        table: str,
        conn_str: str
    ):
        self.table = table
        self.conn_str = conn_str


    def rename_cols(self, df: pl.DataFrame, keys_and_values: Collection[Iterable]) -> pl.DataFrame:
        """Helper function to rename columns in nested structure
        to ensure unique names are preserved
        """
        rename_cols = []
        for key, val in keys_and_values:
            if type(val) == pl.Struct:
                for i, _ in enumerate(val.fields):
                    rename_cols.append(key+'_'+val.fields[i].name)
                df = df.select(
                    pl.all().exclude(key),
                    pl.col(key).struct.rename_fields(rename_cols)
                )
        return df

    def find_struct_to_explode():
        for key, val in keys_and_values:
            if type(val) == pl.List:
                return key
        return None

    def find_struct_to_unnest():
        for key, val in keys_and_values:
            if type(val) == pl.Struct:
                return key
        return None

    def needs_flattening(self, keys_and_values: Collection[Iterable]) -> Tuple:
        """Helper function to find what columns need exploding and unnesting
        """
        expl = []
        unnst = []
        for key, val in keys_and_values:
            if type(val) == pl.List:
                expl.append(key)
            if type(val) == pl.Struct:
                unnst.append(key)
        return expl, unnst

    def explode_cols(
        self,
        df: pl.DataFrame,
        explode_col: str
    ) -> pl.DataFrame:
        pass


    def unnest_cols(
        self,
        df: pl.DataFrame,
        unnest_col: List
    ) -> pl.DataFrame:
        try:
            df.unnest(unnest_col)
        except pl.DuplicateError:

    def flatten_df(
        self,
        df: pl.DataFrame
    ) -> pl.DataFrame:
        """Function to explode and unnuest nested json structure in DataFrame
        """
        expl, unnst = self.needs_flattening(keys_and_values=df.schema.items())
        if len(expl) == 0 and len(unnst) == 0:
            return df
        else:
            if len(unnst) != 0:
                df = self.unnest_cols(df, unnst)
                try:
                    for col in unnst:
                        df = df.unnest(col)
                except pl.DuplicateError:
                    try:
                        df = self.rename_cols(df, keys_and_values)
                    except pl.SchemaError:
                        raise
                return(self.flatten_df(df))
            if len(expl) != 0:
                for col in expl:
                    df = df.explode(col)
                return self.flatten_df(df)

    def write_to_db(self, df) -> None:
        df = df.with_columns(
            pl.lit(
                value=self.table,
                dtype=pl.Utf8
            ).alias('src')
        )
        df.write_database(
            table_name=self.table,
            connection=self.conn_str,
            if_exists='replace',
            engine='sqlalchemy'
        )


    def run(
        self,
        src: str,
        schema
    ) -> None:
        src_df = pl.read_json(source=src, schema=schema)
        df = self.flatten_df(src_df)
        self.write_to_db(df)
