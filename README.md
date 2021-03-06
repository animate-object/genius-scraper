# Genius Scraper
An application/library for scraping raw text lyrics from rap genius via its public facing API and some less savory 
methods (html scraping). 
Uses Python and the BeautifulSoup (bs4) library.

Development in progress.

The core logic for this application was inspired/lifted from the approach describe [in this article](https://bigishdata.com/2016/09/27/getting-song-lyrics-from-geniuss-api-scraping/)
from Big-ish data.

### Improvements provided by this project (will) include:

* a modular application with an interactive CLI (or perhaps a simple GUI)

* functionality to persist lyrics on the host machine in plain text format

* batch lyric retrieval and storage

#### Possible future enhancements:

* a tie in with the Discogs API to retrieve song titles by album and/or artist. This information is not exposed or easily retrieved from the Genius API at the time of writing.

* a hosted rest API

### To examine and work with the existing code base

You will need a valid Rap Genius ClientId and ClientSecret which you can obtain by following the
instructions on their [api documention page](https://docs.genius.com/). Place the credentials in a JSON file
in `app/resources/secrets` called `genius-secret-key.json`. The file should look like this:

```
{
    "client_id": <your client id>
    "client_secret": <your client secret>
}
```

These credentials are used for OAuth2 token generation, necessary to hit the API endpoints and to identify yourself to the API.


 