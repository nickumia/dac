# JSON Collections

## RFC Definition

JavaScript Object Notation is defined [here](https://datatracker.ietf.org/doc/html/rfc7159).

## Supported Feature Data

While JSON is typically a JavaScript structure, it is used in any different
applications for a multitude of reason.  Based on the definition, it makes
sense to handle the following three cases,

1. A Dictionary of key-value pairs,
    - Keys: A unique ID for a value in the dictionary.
    - Values: individual data associated with a key.  Values are generally
      data points.
1. An Array of dictionary objects,
    - Records: Each element in the array represents a collection of data
      referring to a single data point.
    - Header Record (optional)*: The first record can be a dictionary of tags
      similar to the header of a CSV file.  If provided, the index (if
      list) or key (if dictionary) of subsequent records can be tied to the
      header for additional context.
1. Simple value data
    - There is a single piece of data representing one data point with no
      context.
      
\* Not supported at this time.

\* Note: Recursive [arrays/dictionaries] of [arrays/dictionaries] of ... are not
supported either.

## Supported Feature Functions

- Data can be extracted in record-format.  A list of records is returned.
- Data can be extracted by key tag (Only by key name specified in a JSON
dictionary representation).
- Two lists of records can be merged from two different sources.
- A group of keys can be merged from two different sources.
- A list of individual data points can be extracted retaining contextual information
about the record entry at minimum.  It also supports information
about neighbor data points to maintain ordering positions.
