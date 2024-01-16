from itemadapter import ItemAdapter

class QuotescraperPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Modify the 'quote' field
        quote = adapter.get('quote')
        adapter['quote'] = quote.strip()

        # Modify the 'author' field
        author = adapter.get('author')
        if author:
            adapter['author'] = author.strip()

        return item