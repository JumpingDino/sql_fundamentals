from IPython.display import display, Markdown,  HTML
import sqlfluff
import pandas as pd

def custom_display_sql(query_str):

    """Fix the SQL to have a proper format according to SQLFluff and display it.

    Returns:
        None
    """

    display(Markdown(f"```sql\n{sqlfluff.fix(query_str)}\n```"))

    return None


def custom_display_sql(df: pd.DataFrame, title: str = None):
    """Display a DataFrame with a title.

    Args:
        df (pd.DataFrame): The DataFrame to display.
        title (str, optional): The title of the DataFrame. Defaults to None.

    Returns:
        None
    """
    
    if title:
        display(HTML(f"<h3>{title}</h3>"))

    display(HTML(df.to_html(index=False)))

    return None