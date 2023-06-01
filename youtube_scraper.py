import requests
from bs4 import BeautifulSoup


def get_youtube_videos(channel_id):
  """Gets a list of YouTube videos from a channel."""

  # Get the URL of the channel's videos.
  url = "https://www.youtube.com/channel/{}/videos".format(channel_id)

  # Get the HTML of the page.
  response = requests.get(url)
  data = response.content

  # Parse the HTML.
  soup = BeautifulSoup(data, "html.parser")

  # Get the video elements.
  videos = soup.find_all("div", class_="ytd-video-renderer")

  # Create a list of video IDs.
  video_ids = []
  for video in videos:
    video_id = video["data-video-id"]
    video_ids.append(video_id)

  return video_ids


def main():
  """The main function."""

  # Get the channel ID.
  channel_id = input("Enter the channel ID: ")

  # Get the video IDs.
  video_ids = get_youtube_videos(channel_id)

  # Create the HTML file.
  with open("index.html", "w") as f:
    f.write("<html><head><title>Dexter the Cat</title><style>body { background-color: #212121; color: #E8EAE9; } ul { list-style-type: none; margin: 0; padding: 0; } li { display: inline-block; width: 200px; margin: 10px; } img { width: 100%; } a { color: #E8EAE9; } a:hover { color: #ffffff; } iframe { width: 100%; height: 315px; max-height: 100%; }</style></head><body><ul>")
    for video_id in video_ids:
      f.write("<li><a href='https://www.youtube.com/watch?v={}'><img src='https://img.youtube.com/vi/{}/hqdefault.jpg'></a></li>".format(video_id, video_id))
    f.write("</ul></body></html>")


if __name__ == "__main__":
  main()
