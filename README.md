# map-reduce-html
A collection of useful Map Reduce functions that give insight on HTML documents

## Programs and Outputs

### Word Count
#### To Run
```console
-- Using the provided shell script
$ ./run.sh WordCount

# Running it on your own
$ XXX
```

#### Example Output
```txt
the 202466
and 195977
for 79271
var 52680
with  31424
this  30190
more  29278
your  27984
you 27554
new 26347
```

### Bigrams
#### To Run
```console
# Using the provided shell script
$ ./run.sh Bigrams

# Running it on your own
$ XXX
```

#### Example Output
```txt
var:var 10548
and:the 10281
and:screen  9414
for:the 8596
learn:more  6992
and:and 6668
more:read 6130
solid:solid 6009
all:and 5931
the:university  5189
```

### Inverted Index

#### To Run
```console
# Using the provided shell script
$ ./run.sh InvertedIndex

# Running it on your own
$ XXX
```

#### Example Output
```txt
aaa	ag.ny.gov www.uwsp.edu cas.kumc.edu shop.nd.edu
aaaa	fedv6-deployment.antd.nist.gov smolka.wicmb.cornell.edu	
aaads	reunions.berkeley.edu	
aaai	computing.llnl.gov	
aaalac	animalcare.umich.edu	
aaar	blog.epa.gov
aaas	awardsdatabase.usc.edu cis.mit.edu polisci.mit.edu cint.lanl.gov foodscience.cals.cornell.edu viterbischool.usc.edu hr.wisc.edu viterbi.usc.edu www.ccny.cuny.edu nlmdirector.nlm.nih.gov careers.state.gov cee.usc.edu ame.usc.edu ame-www.usc.edu www.utsystem.edu
aaasi global.uconn.edu www.global.uconn.edu
aac fyp.uconn.edu achieve.uconn.edu aac.uconn.edu arch.usc.edu education.indiana.edu iss.uconn.edu calendar.uconn.edu events.uconn.edu registrar.wisc.edu sis.wisc.edu
aacap members.precisionhealth.umich.edu
```

### Out-Links
#### To Run
```console
# Using the provided shell script
$ ./run.sh OutLinks

# Running it on your own
$ XXX
```

### In-Links
#### To Run
```console
# Using the provided shell script
$ ./run.sh InLinks

# Running it on your own
$ XXX
```

#### Example Output
```txt
0	entomology.cals.cornell.edu 
1-800-206-1957	www.scdhec.gov  
1.bp.blogspot.com	ugradcareerblog.kelley.iu.edu 
1.usa.gov	2016.export.gov 1.usa.gov 
10.2.100.96:9026	www.mdhs.ms.gov
10.8.53.17	www.iedc.in.gov
100.ucla.edu	happenings.ucla.edu
100students.universityofcalifornia.edu	admission.universityofcalifornia.edu
1220040d-e2a9-4d47-9628-25dccd7809e8.static.pub.wix-code.com	www.servealabama.gov
132.236.160.66	flowerbulbs.cornell.edu
```

### N-Degrees

#### To Run
```console
# Using the provided shell script
$ ./run.sh NDegrees

# Running it on your own
$ XXX
```

#### Output
The program required 23 hops to converge. The number of hosts per hop can be found below:
- 1: 23
- 2: 77
- 3: 95
- 4: 128
- 5: 109
- 6: 88
- 7: 122
- 8: 393
- 9: 904
- 10: 1082
- 11: 888
- 12: 1862
- 13: 4052
- 14: 2155
- 15: 1486
- 16: 2952
- 17: 2793
- 18: 2249
- 19: 1390
- 20: 944
- 21: 252
- 22: 21
- 23: 12
