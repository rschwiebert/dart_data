# Database content

## Description
Each entry in the database is serialized here as a [.yaml file](https://en.wikipedia.org/wiki/YAML).
Entries from crosstables for many-to-many relationships are organized in the file structure.

Here is a representative example for `ring` objects:

```
ringapp/ring
├── RING_000031
│   ├── RING_000031_details.html<- expanded details template
│   ├── data.yaml               <- definition of the ring
│   ├── dimensions.yaml         <- mapping holding dimension data for this ring
│   ├── properties.yaml         <- mapping holding property data for this ring
│   └── subsets.yaml            <- mapping holding subsets information for this ring
```

Other objects are not so complicated. For example, if you look up subset type 1 to see what it is, all the data is 
in this file:
```
ringapp/subset
├── SUBSET_000001.yaml  <- definition of subset type
...
```
Property 154 will likewise look like this:

```
ringapp/property/PROP_000154
├── data.yaml                 <- defintition of the property
└── metaproperties.yaml       <- mapping associating metaproperty information for this property
```

## Importing/Exporting

The [RingApp](https://github.com/rschwiebert/RingApp) Django application has a custom command for importing and 
exporting the database to and from the format above. If you have the software knowhow, it is recommended that you set 
up a development enviornment for this application, and use it to import dart_data, manipulate it, then export it back 
again.  If you cannot do this, then do your best with hand-editing, and another developer can import your edits to check
it for consistency with the rest of the database.