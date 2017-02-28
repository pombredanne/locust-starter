# locust-starter
## Build

You can build the image with:

```
docker build -t locust-starter .
```

or you can use image `vpavlin/locust-starter` from Docker Hub.

## Run

```
docker run -it --rm -e HOST=http://localhost/ -e PORT=80 -e TEST=obsidian-backend locust-starter obsidian-backend -c 15 -r 15 -n 100
```

where

* `HOST` - is a URL of the host you want to test agains
* `PORT` - is a port to use with `$HOST`
* `-c` - Number of concurrent users
* `-r` - User addition per second
* `-n` - Number of request

This will report number of sent requests and a summary at the backend

```
 Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s
--------------------------------------------------------------------------------------------------------------------------------------------
 POST /forge/commands/obsidian-new-project/execute                 29     0(0.00%)    1754    1031    7032  |    1300    1.00
 POST /forge/commands/obsidian-new-quickstart/validate             33     0(0.00%)     345     229     744  |     320    0.80
 GET /forge/version                                                38     0(0.00%)     201     124     641  |     150    0.90
--------------------------------------------------------------------------------------------------------------------------------------------
 Total                                                            100     0(0.00%)                                       2.70

Percentage of the requests completed within given times
 Name                                                           # reqs    50%    66%    75%    80%    90%    95%    98%    99%   100%
--------------------------------------------------------------------------------------------------------------------------------------------
 POST /forge/commands/obsidian-new-project/execute                  29   1300   1400   1500   1500   2900   6600   7000   7000   7032
 POST /forge/commands/obsidian-new-quickstart/validate              33    320    370    390    400    450    510    740    740    744
 GET /forge/version                                                 38    150    190    230    260    350    370    640    640    641
--------------------------------------------------------------------------------------------------------------------------------------------
```

## Tests

Prepared load tests can be found in `/locustfiles` directory. 

