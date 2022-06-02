# How the database is serialized

## File structure
At the top layer: `db/<app>/<object>`.  Currently `<app>` is one of `ringapp` or `publications`. `ringapp` refers to the RingApp application that 
provides the website, and `publications` is a third-party app that RingApp uses to track citations.  Each `object`
(or model, if you will) is represented beneath its respective app, somehow. Further relationships, such as entries in crosstables expressing many-to-many relations, appear further underneath 
the objects.  

## object ids
Objects are referred to by a tag consisting of an uppercase prefix and their id padded with zeros:
```
RING_000001 <- ring with id 1
PROP_000010 <- property with id 10
CITE_       <- citation
DIM_        <- dimension
ERR_        <- errata
KWD_        <- ring keyword
LOG_        <- logic (inferences between combinations of properties)
METAPROP_   <- properties of properties
PSIDE_      <- pairing of properties with sides (left/right/both)
SUBSET_     <- special subsets of the ring
THM_        <- one of the curated theorems displayed on the site
THMCAT_     <- category keywords for curated theorems
PUB_        <- Publication information (kind of like a bibtex entry)
PUBTYPE_    <- type of publication
PUBLIST_    <- custom lists of publication
PUBLINK_    <- custom links for publications
```

The example below tries to be representative:

## Example
The directory `db/ringapp/ring/RING_000001` shall contain all pertinent information about ring 1.  Its descriptive data 
appears in the file `data.yaml` in this directory, which looks like this:

```citation:
- CITE_000159   # Citation 159 tells you the publication and location therein of the supporting citation
description: Here is a string explaining the ring construction
is_commutative: true
keywords:
- KWD_000017   # Keyword 17 has been associated with this ring
krull_dim: '1' # this field is a string since it could be 'n' or '$\infty$' 
name: 'A name like $\mathbb Z$, which may need to be wrapped in quotes'
notes: null    # An optional string for random notes
optional_template: ''  # DEPRECATED
```

Continuing on, the subdirectory `db/ringapp/ring/RING_000001/properties` will elaborate on associated properties. 
It will contain files named `PROP_XXXXXX.yaml` that look like this:

```citation_left:
- CITE_000159         # The first citation given
- CITE_000160         # Another citation given
citation_right: []    # This is what an empty list looks like in yaml
crosstable_pk: 196    # database generated id for the relation pair
has_on_left: false
has_on_right: false
property: PROP_000002 # Property 2 is the property in question
reason_left: 'Logic 16: division ring ===> valuation ring on the left and right'
reason_right: 'Logic 16: division ring ===> valuation ring on the left and right'
ring: RING_000001     # Ring 1 is the ring in question
```

The subdirectory `db/ringapp/ring/RING_000001/subsets` and `db/ringapp/ring/RING_000001/dimensions` are very similar.

Sometimes a ring requires a LOT more space to elaborate on the construction than is available in the database field. 
In that case, one can include `RING_XXXXXX_details.html` in the `db/ringapp/ring/RING_000001` path, and that will be 
used to provide the expanded-details page for the ring.  They are written as Django templates, so it would be advisable 
to adapt an existing example for your purposes.

Under `db/ringapp/properties/PROP_000001` one will find again a `data.yaml` that describes the property like this:
```
citation: []
commutative_only: false
definition: $xy=yx$ for all $x$ and $y$ in the ring
name: commutative
symmetric: true
```
There is also `db/ringapp/properties/PROP_000001/metaproperties` with files like this:
```citation: []
commutative_only: false
crosstable_pk: 20
example: RING_000012
has_metaproperty: false
metaproperty: METAPROP_000001
property: PROP_000001
```

Other paths are less complicated, and usually just contain a yaml file describing the object.
For example, the `db/ringapp/logic` path just contains files of the form `LOG_XXXXXX.yaml`.
