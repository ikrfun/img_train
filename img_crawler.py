from icrawler.builtin import BingImageCrawler
import argparse
import os 

__version__ = "1.0.0"


class Image_Crawler(object):
    def __init__(self,root_dir):
        self.root_dir = root_dir

    def crawl(self,keyword,max_num=1000):
        crawler = BingImageCrawler(storage={'root_dir': keyword})
        crawler.crawl(keyword=keyword, max_num=max_num)

def main(args):
    print(args.root_dir)
    image_crawler = Image_Crawler(args.root_dir)
    image_crawler.crawl(args.keyword,args.num_image)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"Image Crawler v{__version__}")
    parser.add_argument(
        "-k",
        "--keyword",
        dest = "keyword",
        help = "keyword which you want to search",
        type = str,
        required = True,
    )
    parser.add_argument(
        "-n",
        "--number",
        dest="num_image",
        help="number of images",
        type = int,
        default=1000
    )
    parser.add_argument(
        "-r",
        "--rootdir",
        dest="root_dir",
        help="root_dir of download image files",
        type = str,
        default=os.getcwd()
    )
    args = parser.parse_args()

    main(args)