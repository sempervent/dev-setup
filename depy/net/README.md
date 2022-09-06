# Tools for use with requests

## files.py

The `Files` class can be used to prepare the `files=` argument of a `requests` 
operation. Say you intend to upload both `README.md` and `files.py` to an endpoint,
you can use the following code:
```
files = Files(['files.py', 'README.md'])
response = requests.request('PUT', url, files=files.get())

````
The `Files` class automatically converts the inputs into a tuple or list of
tuples ready for the `requests` engine to parse, and the MIME-type is generated
by the `python-magic` module. Additionally it includes a 
`Files.sizes()` method to retrieve file sizes in the case that information is
needed.
