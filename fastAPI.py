import asyncio
import aiohttp
import uvicorn
from fastapi import FastAPI, Request
from typing import Optional

# Create title and description for SWAGGER
app = FastAPI(title="Sample FastAPI Application",
              description="Sample FastAPI Application with Swagger",
              version="1.0.0", )


# Create get request

@app.get("/scrape")
def getScrape():
    # Get request from API and return message

    return {"message": "Hello FastAPI"}


# Create post request
@app.post("/scrape")
def postScrape(link: str, default_headers: Request, headers: Optional[dict] = None, cookies: Optional[dict] = None,
               payload: Optional[dict] = None):
    async def postRequest():
        # Create async aihttp session

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(link, params=payload, cookies=cookies) as response:
                response = await response.text()
        return response

    # If we are not getting header from API, We have used default headers

    if headers == {}:
        headers = default_headers.headers['user-agent']
        headers = {'user-agent': headers}

    # Called async function

    result = asyncio.run(postRequest())

    # reutrn HTML paee respones

    return result


if __name__ == "__main__":
    uvicorn.run("fastAPI:app", port=8000, reload=True)
