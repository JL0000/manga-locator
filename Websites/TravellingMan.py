from Websites.Website import Website

class TravellingMan(Website):
    def __init__(self):
        super().__init__()
        self.base_html = "https://travellingman.com"

    def find_matches(self, soup):
        return soup.select("div.product-card--list")

    def get_name(self, match):
        return match.select("a > span")[0].text.strip()
    
    def get_price(self, match):
        price = match.select("div.list-view-item__link > div.list-view-item__price-column > dl > div.price__regular > dd > span ")
        if price:
            return price[0].text.strip()
        else:
            return "Sold out"
    
    def get_link(self, match):
        return self.base_html + match.select("a")[0].get("href")
        


