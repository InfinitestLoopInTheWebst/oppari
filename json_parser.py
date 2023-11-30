import polars as pl
from typing import OrderedDict

class ParseJson:
    """Class to flatten json in Polars DataFrame
    """
    def __init__(
        self,
        table: str,
        conn_str: str
    ):
        self.table = table
        self.conn_str = conn_str


    def rename_cols(self, df: pl.DataFrame, keys_and_values: OrderedDict[str, pl.PolarsDataType]) -> pl.DataFrame:
        """Helper function to rename columns in nested structure
        to ensure unique names are preserved
        """
        for key, val in keys_and_values:
            rename_cols = []
            if type(val) == pl.Struct:
                for i, _ in enumerate(val.fields):
                    rename_cols.append(key+'_'+val.fields[i].name)
                df = df.select(
                    pl.all().exclude(key),
                    pl.col(key).struct.rename_fields(rename_cols)
                )
        return df

    def find_struct_to_explode(self, keys_and_values: OrderedDict[str, pl.PolarsDataType]) -> str:
        """Helper function to find structures to explode.
        Returns first eligible
        """
        for key, val in keys_and_values:
            if type(val) == pl.List:
                return key
        return None

    def find_struct_to_unnest(self, keys_and_values: OrderedDict[str, pl.PolarsDataType]) -> str:
        """Helper function to find structures to unnest.
        Returns first eligible
        """
        for key, val in keys_and_values:
            if type(val) == pl.Struct:
                return key
        return None

    def unnest_cols(
        self,
        df: pl.DataFrame,
        unnest_col: str
    ) -> pl.DataFrame:
        """Helper function to unnest columns
        """
        try:
            df = df.unnest(unnest_col)
        except pl.DuplicateError:
            try:
                df = self.rename_cols(df, keys_and_values=df.schema.items())
            except pl.SchemaError:
                raise
        return df

    def flatten_df(
        self,
        df: pl.DataFrame
    ) -> pl.DataFrame:
        """Function to explode and unnuest nested json structure in DataFrame
        """
        explode_col = self.find_struct_to_explode(keys_and_values=df.schema.items())
        unnest_col = self.find_struct_to_unnest(keys_and_values=df.schema.items())
        if not explode_col and not unnest_col:
            return df
        if explode_col:
            df = df.explode(explode_col)
        if unnest_col:
            df = self.unnest_cols(df, unnest_col)
        return self.flatten_df(df)

    def write_to_db(self, df: pl.DataFrame) -> None:
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

    def run(self, src: str, schema: OrderedDict[str, pl.PolarsDataType]) -> None:
        src_df = pl.read_json(source=src, schema=schema)
        df = self.flatten_df(src_df)
        self.write_to_db(df)
