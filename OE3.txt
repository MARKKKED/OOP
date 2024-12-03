class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged in.")

    def post(self, content):
        print(f"{self.username} posted: {content}")


class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story):
        print(f"{self.username} shared an Instagram story: {story}")


class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        print(f"{self.username} tweeted: {tweet_content}")


insta_account = InstagramAccount("insta_user", "insta_pass", 500)
insta_account.login()
insta_account.post("Hello, Instagram!")
insta_account.share_story("My first story!")
print(f"Followers: {insta_account.number_of_followers}")


twitter_account = TwitterAccount("twitter_user", "twitter_pass", 120)
twitter_account.login()
twitter_account.post("Hello, Twitter!")
twitter_account.tweet("This is my first tweet!")
print(f"Number of Tweets: {twitter_account.number_of_tweets}")
