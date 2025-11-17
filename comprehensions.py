sample_articles = [
  {
    "title": "Understanding List Comprehensions in Python",
    "source": {"name": "TeachNews"},
    "description": "A deep dive into list comprehensions and their benefits.",
    "category": "Education"
  },
  {
    "title": "Latest Tech Trends in 2024",
    "source": {"name": "TechDaily"},
    "description": "An overview of the most significant technology trends this year.",
    "category": "Technology"
  },
  {
    "title": "Health Benefits of Regular Exercise",
    "source": {"name": "HealthLine"},
    "description": "Exploring the various health advantages of maintaining a regular exercise routine.",
    "category": "Health"
  },
  {
    "title": "Global Economic Outlook for 2024",
    "source": {"name": "FinanceWorld"},
    "description": "Predictions and analyses of the global economy for the upcoming year.",
    "category": "Finance"
  },
  {
    "title": "Travel Destinations to Explore in 2024",
    "source": {"name": "Wanderlust"},
    "description": "Top travel destinations to consider for your 2024 vacations.",
    "category": "Travel"
  },
  {
    "title": "Advancements in Renewable Energy",
    "source": {"name": "EcoNews"},
    "description": "Latest developments in renewable energy technologies and their impact.",
    "category": "Environment"
  }
]


def extract_titles_traditional(articles):
  """Extract titles using traditional for loop."""
  titles = []
  for article in articles:
    if len(article["title"]) > 200:
      titles.append(article["title"])
  return titles


def extract_titles(articles):
  """Extract titles using list comprehension."""
  return [article["title"] for article in articles if len(article["title"]) > 200]


def extract_article_summaries(articles):
  return {
    article["title"]: article["description"]
    for article in articles
    if len(article["description"]) < 5
  }


def get_sources_traditional(articles):
  sources = set()
  for article in articles:
    if article.get("source") and article.get("source").get("name"):
      sources.add(article["source"]["name"])
  return sources


def get_sources(articles):
  """
    {
      expression
      for member in iterable
      if condition
    }
  """
  return {
    article.get("source").get("name")
    for article in articles
    if article.get("source") and article.get("source").get("name")
  }


def categorize_articles(articles):

  sources = get_sources(articles)
  results = {}

  for source in sources:
    if source not in results:
      results[source] = []

    for article in articles:
      if source == article.get("source").get("name"):
        results[source].append(article)

  return results


def categorize(articles):
  sources = get_sources(articles)
  return {
    source: [
      article
      for article in articles
      if source == article.get("source").get("name")
    ]
    for source in sources
  }


print("Categorized Articles:", categorize_articles(sample_articles))
print()
print("========")
print()
print("Categorized Articles with Comprehension:", categorize(sample_articles))