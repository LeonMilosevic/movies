"""File will contain type annotations for functions and variables."""

from typing import Any, Dict, List

from pandas import DataFrame

FileName = str
FileHeader = List[str]
MovieFiles = Dict[FileName, FileHeader]
DataFrameMap = Dict[FileName, DataFrame]
ColumnTypeMap = Dict[str, List[str]]
Json = Dict[str, Any]
