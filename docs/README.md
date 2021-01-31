# Carbon API

> Created by Amal Shaji [Email](mailto:amalshajid@gmail.com) [GitHub](https://github.com/amalshaji) [Twitter](https://twitter.com/pydantic)

## Source Code

https://github.com/amalshaji/carbon-api

## Introduction

[Carbon](https://carbon.now.sh/) is a service used for creating beautiful screenshots of code snippets. [Carbon API](https://apicarbon.herokuapp.com/) is a unofficial API for creating code screenshots based on the carbon website.

Simply send a code snippet or code file as `POST` request to the API endpoint and it will return the image file.

## BASE URL

- https://apicarbon.herokuapp.com/


## Endpoint

- [POST] /api/ 

  - Data accepted in `multipart/formdata` format
  - Either the `code` field or a code file is required
  - All other configuration can be found in the [interactive docs](https://apicarbon.herokuapp.com/docs)

## Example

  - Sending code as a string

  ![code.PNG](docs/code.PNG)

  - Sending code as a file

  ![file.PNG](docs/file.PNG)

## How it works

The screenshots are actually taken from the [official carbon website](https://carbon.now.sh). [Pyppeteer](https://github.com/pyppeteer/pyppeteer) package is used to grab screenshot from the website.


⚠️ Do not spam the API, as it calls the carbon instance and may get DDoSed. If you want an API that generates screenshots at a high traffic, it is suggested to host you own `Carbon` instance as the code is [MIT Licensed](https://github.com/carbon-app/carbon/blob/main/LICENSE).