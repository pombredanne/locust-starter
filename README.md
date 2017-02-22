# locust-starter
## Build

You can build the image with:

```
docker build -t locust-starter .
```

or you can use image `vpavlin/locust-starter` from Docker Hub.

## Run

```
docker run -it --rm -e HOST=http://localhost/ -e PORT=80 -e TEST=obsidian-backend -p 8080:8089 locust-starter
```

where

* `HOST` - is a URL of the host you want to test agains
* `PORT` - is a port to use with `$HOST`
* `TEST` - is a name of the file you want to run (without extension)

Then open browser at http://localhost:8080, fill in how many users you want to simulate and hit Start

## Tests

Prepared load tests can be found in `/locustfiles` directory. 

