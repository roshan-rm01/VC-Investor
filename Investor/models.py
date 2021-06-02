from django.db import models


class Investor(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    firm = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    founder = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(default='VCInvestor/static/london.png')
    location = models.CharField(max_length=100)
    SECTOR_CHOICE = (
        ('entertainment', 'Entertainment'),
        ('fintech', 'Fintech'),
        ('technology', 'Technology'),
        ('enterprise', 'Enterprise'),
        ('travel', 'Travel'),
        ('healthcare', 'Healthcare'),
        ('robotics', 'Robotics'),
    )
    sector = models.CharField(choices=SECTOR_CHOICE, max_length=100)
    INVESTMENT_STAGE = (
        ('series b', 'Series B'),
        ('series c', 'Series C'),
        ('series d', 'Series D'),
        ('series e', 'Series E')
    )
    stage = models.CharField(choices=INVESTMENT_STAGE, max_length=100)
    description = models.TextField()
    launch_year = models.IntegerField()
    valuation = models.DecimalField(decimal_places=1, max_digits=100000)
    revenue = models.DecimalField(decimal_places=2, max_digits=100000)
    personal_opinion = models.TextField()

    def __str__(self):
        return self.name
