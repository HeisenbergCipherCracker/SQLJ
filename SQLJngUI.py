import argparse
import warnings
from logger.logs import logger

def Argument_parser():
    parser = argparse.ArgumentParser(description="SQLJng")

    # Adding arguments
    parser.add_argument("-u", "--url", help="Enter the url of the target", required=True)
    parser.add_argument("-H", "--headers", help="Add headers", required=False)

    # Additional arguments can be added as needed
    parser.add_argument("-p", "--port", type=int, help="Specify a port number", required=False)
    parser.add_argument("--enable-feature", action="store_true", help="Enable a specific feature", required=False)
    parser.add_argument("--types", type=str, help="Specify the type of the attack", required=True)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    parser.add_argument("-verbose", action="store_true", help="Enable verbose mode", required=False)
    parser.add_argument("-other",  help="Enable other features", required=False)

    # Parse the command line arguments
    args = parser.parse_args()

    # Accessing values
    url = args.url
    headers = args.headers
    port = args.port
    enable_feature = args.enable_feature
    attack_type = args.types
    if "www.google.com" in url or "https://www.google.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the google.com")
    
    elif "www.youtube.com" in url or "https://www.youtube.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the youtube.com")
    
    elif "www.facebook.com" in url or "https://www.facebook.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the facebook.com")
    
    elif "www.instagram.com" in url or "https://www.instagram.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the instagram.com")
    
    elif "www.twitter.com" in url or "https://www.twitter.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the twitter.com")
    
    elif "www.linkedin.com" in url or "https://www.linkedin.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the linkedin.com")

    elif "www.reddit.com" in url or "https://www.reddit.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the reddit.com")

    elif "www.pinterest.com" in url or "https://www.pinterest.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the pinterest.com")

    elif "www.tumblr.com" in url or "https://www.tumblr.com" in url:
        warnings.warn("This attack may encounter you with legall issues. Please check the url and try again.")
        logger.critical("This attack may encounter you with legall issues. Please check the url and try again.you are trying to perform attack on the tumblr.com")

    else:
        pass

    # Your logic here based on the provided arguments
    

if __name__ == "__main__":
    Argument_parser()
