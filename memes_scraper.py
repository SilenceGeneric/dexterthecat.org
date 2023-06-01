import requests
from bs4 import BeautifulSoup


def get_memes(filters):
  """Gets a list of memes from Reddit."""

  # Get the top 25 posts from the /r/memes subreddit.
  url = "https://www.reddit.com/r/memes/top/.json?limit=25"
  response = requests.get(url)
  data = response.json()

  # Get the image URLs for the top 25 posts.
  image_urls = []
  for post in data["data"]["children"]:
    if filters == None or all(filter in post["data"]["title"] for filter in filters):
      image_urls.append(post["data"]["url"])

  return image_urls


def main():
  """The main function."""

  # Get a list of memes from Reddit.
  image_urls = get_memes()

  # Create a new HTML file and add the memes to it.
  with open("index.html", "w") as f:
    f.write("<html><head><title>Meme Scraper</title></head><body><ul><li>")
    for image_url in image_urls:
      f.write("<img src='{}'></li>".format(image_url))
    f.write("</ul></body></html>")


if __name__ == "__main__":
  # Get the search terms from the user.
  search_terms = input("Enter search terms: ")

  # Split the search terms into a list.
  filters = search_terms.split()

  # Get the memes that match the search terms.
  image_urls = get_memes(filters)

  # Create the HTML file.
  main()
