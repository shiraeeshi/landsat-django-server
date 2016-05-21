# Landsat django server project

This project shows how to create a tile server with GeoTrellis ingested tiles.

#### Dependencies

- https://github.com/geotrellis/geotrellis-landsat-tutorial
- geotrellis-python

#### How to run

- Follow the readme in https://github.com/geotrellis/geotrellis-landsat-tutorial
- Make sure that you have geotrellis-python installed
- `cd` into `landsat-django-server` directory (the root directory of this repository) and then run:

`python manage.py runserver 8080`

- You can find `static/index.html` file in `geotrellis-landsat-tutorial` repository's folder. If you open it in browser (with active internet connection), you will be able to see the tiles on a map.
