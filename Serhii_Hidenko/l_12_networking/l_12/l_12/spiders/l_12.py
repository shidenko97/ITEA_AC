import scrapy
from w3lib.html import remove_tags


class L12Spider(scrapy.Spider):
    name = "l_12"
    domain = "https://stackoverflow.com"  # Base url for parsing

    def start_requests(self):
        """Start parsing from first page of questions"""

        yield scrapy.Request(
            url=f"{self.domain}/questions?tab=newest&page=1",
            callback=self.parse_pages
        )

    def parse_pages(self, response):
        """Parse base page and all questions on the page"""

        yield self.format(response)
        for link in response.css('div.question-summary a.question-hyperlink'):
            url = f"{self.domain}{link.attrib['href']}"
            yield scrapy.Request(url=url, callback=self.format)

    @staticmethod
    def format(response):
        """Format parse result"""

        custom_fields = {}
        custom_params = {
            "datetime": "time[itemprop=\"dateCreated\"]::attr(datetime)",
            "author": "div.user-details[itemprop=\"author\"] a",
        }

        # Process not required single fields
        for field, selector in custom_params.items():
            custom_field = response.css(selector)

            if len(custom_field):
                custom_fields[field] = format_value(custom_field.get())
            else:
                custom_fields[field] = ""

        return {
            "title": format_value(response.css("title").get()),
            "headers": list(
                map(
                    lambda header: format_value(header),
                    response.css("h1, h2, h3, h4, h5, h6").getall()
                )
            ),
            "datetime": custom_fields["datetime"],
            "tags": list(
                map(
                    lambda tag: format_value(tag),
                    response.css("div.post-taglist div.grid a").getall()
                )
            ),
            "author": custom_fields["author"],
            "answers": list(
                map(
                    lambda tag: format_value(tag),
                    response.css("#answers div.answer .post-text").getall()
                )
            ),
        }


def format_value(value: str) -> str:
    """Remove html tags from parsed value and strip the text"""

    return remove_tags(value).strip()
