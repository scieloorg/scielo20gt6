"""
In order to use this configuration,
it should be passed as the "--config" parameter, like:

  jupyter nbconvert --config nbconvert_config.py [...]

This configuration just makes the following filters available
to the jinja templates when converting jupyter notebooks
to other formats using nbconvert.
"""
from io import StringIO
import re
import warnings

from lxml import etree
import pandas as pd


# This was made using pandoc 2.3.1,
# which nbconvert complains that isn't supported, but it works!
# So let's get rid from these warnings
warnings.filterwarnings(
    action="ignore",
    message="You are using an unsupported version of pandoc",
    category=RuntimeWarning,
)


def html2df(html):
    # Here the pd.read_html can't be used since:
    # - It ignores the rowspan
    # - It casts to some data type other than a raw string
    # Only the leftmost columns might have some <th> w/ rowspan > 1
    table_tree = etree.HTML(html).xpath("//table")[0]
    rev_table = [[etree.tounicode(td, method="text", with_tail=False)
                  for td in reversed(tr.xpath("th|td"))]
                 for tr in table_tree.xpath("//tr")]
    rev_df = pd.DataFrame(rev_table, dtype=str).fillna(method="ffill")
    header_nrows = len(table_tree.xpath("//thead/tr"))
    headerless_df = rev_df.iloc[:, ::-1]
    header = headerless_df.iloc[:header_nrows].values.tolist()
    return headerless_df.iloc[header_nrows:].T.set_index(header).T


def df_max_lengths(data):
    word_lengths = data.T.reset_index().T.applymap(
        lambda x: max(map(len, re.sub("[-;.]", " ", str(x)).split()),
                      default=0)
    ).max().fillna(0)
    return word_lengths.values.tolist()


# The "get_config" is implicit from nbconvert
get_config().TemplateExporter.filters = {
    "html2df": html2df,
    "df_max_lengths": df_max_lengths,
}
