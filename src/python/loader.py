import requests
import requests.auth
import twitter

class UniPost():
    text =""
    def __init__(self, text):
        self.text = text



def construct_header(credentials, url):
    client_auth = requests.auth.HTTPBasicAuth(credentials["client_id"], credentials["client_secret"])
    post_data = {"grant_type": "password", "username": credentials["username"], "password": credentials["password"]}
    headers = {"User-Agent": credentials["user_agent"]}
    response = requests.post(url, auth=client_auth, data=post_data,
                             headers=headers)
    responseData = response.json()

    access_token = responseData["access_token"]
    token_type = responseData["token_type"]

    return {"User-Agent": credentials["user_agent"], "Authorization": token_type + " " + access_token}


def get_data_reddit(headers,topic):
    response = requests.get("https://oauth.reddit.com/r/"+topic, headers=headers)

    status = response
    head = response.headers
    data = response.json()

    used = head["X-Ratelimit-Used"]
    rem = head["X-Ratelimit-Remaining"]
    res = head["X-Ratelimit-Reset"]

    return [ UniPost(r["data"]["selftext"]) for r in  data["data"]["children"]]


def get_data_twitter(credentials,topic):
    api = twitter.Api(consumer_key= credentials["consumer_key"],
                      consumer_secret=credentials["consumer_secret"],
                      access_token_key=credentials["token_key"],
                      access_token_secret=credentials["token_secret"])
    return [ UniPost( r.text) for r in api.GetSearch(topic)]
