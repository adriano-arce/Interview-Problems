import re
import os
import urllib.request


def get_urls(filename):
    """
    Returns a sorted list of puzzle URLs from the given log file. The hostname
    comes from the filename and puzzle URLs contain the word puzzle. If a URL is
    duplicated, then we only include it once.
    """
    under_index = filename.find("_")
    log_index = filename.find(".log")
    prefix = "http://" + filename[under_index + 1:log_index]
    with open(filename, "r") as f:
        lines = f.read().split("\n")
    pattern = r"GET (\S*/puzzle/\S*\w+-(\w+).jpg) HTTP"
    regex = re.compile(pattern)

    url_dict = {}
    for line in lines:
        match = regex.search(line)
        if match:
            url_dict[prefix + match.group(1)] = match.group(2)
    return sorted(url_dict, key=lambda u:url_dict[u])


def download_imgs(urls, dest):
    """
    Downloads the given list of URLs into the given destination directory.
    """
    if not os.path.exists(dest):
        os.makedirs(dest)

    html_data = ["<html><body>\n"]
    for i, url in enumerate(urls):
        img_name = "img{}.jpg".format(i)
        print("Retrieving {}...".format(img_name))
        urllib.request.urlretrieve(url, os.path.join(dest, img_name))
        html_data.append('<img src="{}">'.format(img_name))
    html_data.append("\n</body></html>\n")

    with open(os.path.join(dest, "index.html"), "w") as f:
        f.write("".join(html_data))


def main():
    log_files = ["animal_code.google.com.log", "place_code.google.com.log"]
    for log_file in log_files:
        print("Processing the", log_file, "logfile...")
        under = log_file.find("_")
        dest = log_file[:under]
        urls = get_urls(log_file)
        download_imgs(urls, dest)

if __name__ == "__main__":
    main()