# CSV Collections

## RFC Definition

Comma-Separated Values is defined [here](https://datatracker.ietf.org/doc/html/rfc4180).

## Supported Feature Data

Based on the definition, it makes sense to manipulate the following attributes,

- Headers: A top row that describes the column fields of the remaining entries
    - If a header is defined, each column of the header acts as a sort of tag
			for the data.
		- If a header is not defined, each column is numbered by index and used as
			a tag instead.

- Records: Each row that represents a collection of data referring to a single
data point.

- Attributes: Each column that represents a particulate detail about a record.

## Supported Feature Functions

- Data can be extracted in record-format.  A list of records is returned.
- Data can be extracted by attribute tag (either by header name or header index
depending on the specification of a header).
- Two lists of records can be merged from two different sources.
- A group of attributes can be merged from two different sources.
- A list of individual data points can be extracted retaining contextual information
about the record entry and header tag at minimum.  It also supports information
about neighbor data points to maintain ordering positions.
