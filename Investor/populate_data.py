from .models import Company
from django.utils.text import slugify


def populate():
    Company.objects.create(
        name="Starling Bank",
        founder="Anne Boden",
        slug=slugify("Starling Bank"),
        image="static/img/Starling_Bank_Logo.png",
        location="United Kingdom",
        sector="fintech",
        stage="series d",
        description="Starling Bank is one of the latest unicorn companies from the UK. With its HQ based in London, "
                    "Starling Bank is a Neobank that aims to challenge traditional banks. Its current account "
                    "incorporates many features such as access to the Starling Bank Marketplace where users can "
                    "access a variety of financial services ranging from investments via Wealthify to insurance via "
                    "So-sure. Starling Bank also offers business banking that utilises many features such as HMRC tax "
                    "calculations and saving reports for small to medium-size enterprises. Website: "
                    "https://www.starlingbank.com ",
        launch_year=2014,
        valuation=1300,
        revenue=145,
        personal_opinion="Starling Bank is operating in the competitive field of UK challenger banks. Already 2 main "
                         "challenger banks offer similar services to Starling Bank, Revolut and Monzo. However, "
                         "Starling Bank is unique as out of the main challenger banks it was the only one to become "
                         "profitable in 2020, granted this was when the UK government was issuing Covid loans at "
                         "generous rates. Nevertheless, Starling Bank is a major player in the UK fintech scene and "
                         "based on recent figures on January 2021 they have experienced a 400% increase in revenue "
                         "growth year over year. The future is bright for Starling Bank and with backing from Goldman "
                         "Sachs, Starling may be heading for an IPO near in the future. "
    )
    Company.objects.create(
        name="Revolut",
        founder="Nikolay Storonsky",
        slug=slugify("Revolut"),
        image="static/img/Revolut_Logo.png",
        location="United Kingdom",
        sector="fintech",
        stage="series d",
        description="Based in London, England, Revolut has emerged as one of the best digital banks for international "
                    "money transfers. Its main products include a current account for banking, a trading platform and "
                    "an insurance platform. Operating in more than 30 countries, Revolut aims to become a major "
                    "player in global banking, with a mission to become a first choice bank for younger people. With "
                    "funding led by some of the biggest VC firms such as DST Global, Revolut shows no sign of slowing "
                    "down and plans to introduce many new features such as a subscription management system to track "
                    "and cancel subscriptions on the Revolut app. Website: https://www.revolut.com/",
        launch_year=2015,
        valuation=10000,
        revenue=160,
        personal_opinion="Revolut is interesting in the way that it stands out compared with other challenger banks. "
                         "Unlike digital banks such as Monzo, Revolut is aiming to become a super app for financial "
                         "services. For example, if all services a user may want are found in one app such as finding "
                         "the best insurance, Revolut prospers in users spending more time on their app and its "
                         "commission with its various services. The revenue stream with Revolut is very diverse "
                         "however the company has been riddled with some controversy relating to employment practices "
                         "and problems with flagging inadequate payments. Revolut is still growing with a reported "
                         "180% growth in revenue year over year in 2020. "
    )
    Company.objects.create(
        name="Yubo",
        founder="Sacha Lazimi",
        slug=slugify("Yubo"),
        image="static/img/Yubo_Logo.jpg",
        location="France",
        sector="entertainment",
        stage="series c",
        description="Yubo is a social media app targeting people under 25, most notably generation Z. Unlike "
                    "traditional social media which relies heavily on advertising for revenue, Yubo uses in-app "
                    "purchases as a form of monetisation. Its main feature is that users are presented with a range "
                    "of rooms that are populated with people who share the same interest as the user and are of "
                    "similar age. These rooms are usually of people live-streaming themselves through video or voice "
                    "and also use messaging to talk to specific people within a room. Users can also pay for features "
                    "like promoting certain rooms on the top of recommendations and to boost live stream "
                    "capabilities. Website: https://yubo.live/ ",
        launch_year=2015,
        valuation=45.8,
        revenue=14,
        personal_opinion="Yubo is entering a competitive field of social media where any sort of small innovational "
                         "features can easily be copied by the big players like Instagram. However, Yubo is different "
                         "in the sense that it focuses on friendship rather than followers. The main premise of the "
                         "app was never to allow people to follow one another but to establish a friendship with "
                         "someone, similar to how teens create friendships with each other in schools. With revenue "
                         "growth at 100% year over year in 2020 and with over 10 million downloads on the Google play "
                         "store, Yubo shows no sign of slowing down. Although what needs to be taken into account is "
                         "that users may encounter predators on this app, it is an app to meet strangers at the end "
                         "of the day. Yubo however, does a good job protecting young users by filtering out harmful "
                         "rooms and removing as much explicit content as possible. "
    )
    Company.objects.create(
        name="MessageBird",
        founder="Adriaan Mol",
        slug=slugify("MessageBird"),
        image="static/img/Messagebird_Logo.jpg",
        location="Netherlands",
        sector="enterprise",
        stage="series c",
        description="MessageBird is a cloud communications platforms that provide APIs and cloud storage for "
                    "communications. Its products range from omnichannel messaging across platforms such as Whatsapp "
                    "and Messenger to customer support via FAQ bots. Customer support plays a pivotal role in the "
                    "MessageBird platform as it offers a platform to host all customer enquires across different "
                    "channels. Users are also able to automate tasks such as implementing a chatbot and automatically "
                    "schedule appointments for customers for video calls. Website: https://www.messagebird.com/",
        launch_year=2011,
        valuation=3000,
        revenue=268,
        personal_opinion="MessageBird began as an alternative to Twilio by providing roughly the same communication "
                         "services. Over the years, however, MessageBird has shifted its resources towards becoming "
                         "an omnichannel-as-a-service platform. With this shift, MessageBird has given itself a "
                         "unique identity in customer support and management. What is now apparent is that the "
                         "pandemic has highlighted the need for digital solutions to enhance digital offerings so "
                         "it's no surprise that MessageBird benefitted massively. Its year over year revenue growth "
                         "of 50% in 2020 is significant however the company is still incurring single-digit million "
                         "euro losses. The future for MessageBird is still bright as with its recent acquisition of "
                         "SparkPost, MessageBird is looking to enhance its email service. "
    )
    Company.objects.create(
        name="Kry",
        founder="Johannes Schildt",
        slug=slugify("Kry"),
        image="static/img/Kry_Logo.jpg",
        location="Sweden",
        sector="healthcare",
        stage="series d",
        description="Kry is Sweden's first and largest digital healthcare provider that allows users to consult with "
                    "doctors digitally either through video, message or voice call. Its main operation is in the "
                    "Nordic regions but its global footprint expands to the UK, France and USA under the name Livi. "
                    "With major backing from global players such as Accel, Kry is positioned to revolutionise digital "
                    "healthcare in the Nordic region and the rest of Europe. Introductions to mental health services "
                    "will soon roll out to enhance Kry's offerings. Website: https://www.kry.se/",
        launch_year=2014,
        valuation=2000,
        revenue=60,
        personal_opinion="Kry has benefitted massively from the pandemic, as stay-at-home measures were implemented, "
                         "Kry saw its largest influx of appointments. With revenue growth at 100% year over year in "
                         "2020, Kry has a great future for health tech, especially in the Nordic region. For Sweden, "
                         "healthcare needed a major transformation and when Kry was introduced, the strain on "
                         "Sweden's healthcare system reduced as more people opted to use Kry services. The Swedish "
                         "healthcare system improved as a result so it's no surprise the Kry is trying to replicate "
                         "this with many other European countries. However, competition is fierce and major "
                         "disrupters across Europe like Babylon Health (British) and Alan (French) have already "
                         "established market shares in their respective regions. "
    )
    Company.objects.create(
        name="Wandelbots",
        founder="Christian Piechnick",
        slug=slugify("Wandelbots"),
        image="static/img/Wandelbots_Logo.png",
        location="Germany",
        sector="robotics",
        stage="series b",
        description="Programming is a hard concept to grasp for many people so when it comes to robotics, it might be "
                    "a barrier for companies who may not have the expertise to program and handle robots. Wandelbots "
                    "kills two birds with one stone by creating no-code robots. These robots are unique as to control "
                    "them you would only need to use a tablet and a TracePen to draw the movement of the robot. "
                    "Wandelbots already has major clients ranging from Volkswagen to BMW. The Wandelbot robots are "
                    "major game-changers and could disrupt the decades-long industry of software developed robots in "
                    "manufacturing. Website: https://wandelbots.com/",
        launch_year=2017,
        valuation=77.3,
        revenue=4,
        personal_opinion="Wandelbots saw a massive increase in demand during the pandemic. The no-code robots are "
                         "popular with international buyers trying to on-shore key processes in the supply chain. For "
                         "many companies, it seems like a no-brainer to enquire about these robots because there are "
                         "many advantages to this such as the reduction of cost through software maintenance. These "
                         "robots will be big with car manufacturers initially from Germany then gradually beyond "
                         "Europe. "
    )
    Company.objects.create(
        name="Comtravo",
        founder="Michael Riegel",
        slug=slugify("Comtravo"),
        image="static/img/Comtravo_Logo.jpg",
        location="Germany",
        sector="travel",
        stage="series b",
        description="Based in Berlin, Germany, Comtravo is a leading business travel provider for small-to-medium "
                    "size enterprises. It combines customer support with artificial intelligence to offer business "
                    "individuals easy travelling options that are comparable to vacationers. With artificial "
                    "intelligence, Contravo can find the best deals for business people travelling overseas. From "
                    "deal on flights all the way to hotel bookings, Contravo wants to assist businesses every step of "
                    "the way on how to help make business travel an easy and effective process for business "
                    "individuals. Website: https://comtravo.com/",
        launch_year=2015,
        valuation=46.4,
        revenue=26,
        personal_opinion="Comtravo automates business travel bookings which can reduce the time-consuming burden of "
                         "finding the best deals on various websites. It also has a user-friendly interface that is "
                         "simple enough for any business to use. Before the pandemic, Comtravo seems like a good bet "
                         "as business travel was never as simple as vacation travel but now the pandemic has "
                         "highlighted the efficiency of working from home. Many businesses are now operating "
                         "domestically and reducing the number of people going abroad so it's no surprise that 2020 "
                         "was not the best year for Comtravo. The future for Comtravo still seems bright but "
                         "uncertain. On one hand, if travel starts to pick up once the pandemic ends then Comtravo "
                         "can see itself return to pre-pandemic levels. On the other hand, companies may reduce "
                         "overseas travel and look to remote working which will hurt Comtravo. "
    )
    Company.objects.create(
        name="Red Points",
        founder="Laura Urquizu",
        slug=slugify("Red Points"),
        image="static/img/Red_Points_Logo.jpg",
        location="Spain",
        sector="enterprise",
        stage="series c",
        description="Red Points is a platform used to protect brand identity and trademarks. Its main product uses "
                    "artificial intelligence to scour sites and track any counterfeit goods that could harm the "
                    "reputation of a brand and infringes on trademarks. Popular with brands that sell products on "
                    "e-commerce sites, Red Points can also take down fake accounts across many sites. It can also "
                    "track and remove illegal content from video sites such as Youtube to protect company brands. "
                    "Website: https://www.redpoints.com/",
        launch_year=2011,
        valuation=178,
        revenue=41,
        personal_opinion="E-commerce is now one of the fastest-growing sectors in the world. The pandemic has led to "
                         "e-commerce gradually taking over traditional brick and mortar stores. With brands now "
                         "operating online, protection for trademarks and reputation is needed more than ever. Based "
                         "on research from the International Chamber of Commerce, counterfeiting will be a $4.2 bn "
                         "industry with damages exceeding $323 bn. Red Points can play a key role in disrupting the "
                         "counterfeiting market and protect brands from significant damages. In the long run, "
                         "Red Points has a great future for protecting brands. Currently, Red Points is still scaling "
                         "operations but it wouldn't be a surprise if it is acquired from a large cybersecurity "
                         "company. "
    )
    Company.objects.create(
        name="Hopin",
        founder="Johnny Boufarhat",
        slug=slugify("Hopin"),
        image="static/img/Hopin_Logo.png",
        location="United Kingdom",
        sector="technology",
        stage="series b",
        description="Hopin is an all-in-one online events platform that is used to host live events. Some notable use "
                    "cases range from hosting online career fairs to hosting conference meetings. Unlike other online "
                    "video platforms, Hopin can host up to 50000 people and offers unique features such as the "
                    "ability to schedule networking sessions and integrate events with a variety of applications like "
                    "Twitter. Events can also be monetised by selling virtual tickets. Website: https://hopin.com/",
        launch_year=2019,
        valuation=4000,
        revenue=50,
        personal_opinion="Hopin has got to be one of the most successful companies to benefit from the pandemic. "
                         "Currently, it's profitable and has seen a 250% revenue growth year over year in 2020. With "
                         "backing from major players like Andreessen Horowitz, Hopin shows no sign of slowing down "
                         "and may even go for an IPO soon. However, the pandemic was a major factor that contributed "
                         "to its growth so there should be some questions on whether there is a future for online "
                         "events after the pandemic. Hopin competitors are Zoom and Run The World so they aren't the "
                         "first to establish online events but they are the most innovative in terms of creating a "
                         "virtual platform for people to organise events. "
    )
    Company.objects.create(
        name="Graphcore",
        founder="Nigel Toon",
        slug=slugify("Graphcore"),
        image="static/img/Graphcore_Logo.png",
        location="United Kingdom",
        sector="technology",
        stage="series e",
        description="Graphcore is a British semiconductor company that creates processors for artificial "
                    "intelligence. Its IPU (Intelligence Processing Unit) processors are the worlds most complex and "
                    "are used to advance AI innovation. Graphcore's processors are said to revolutionise different "
                    "industries ranging from finance to telecommunications. In finance, Graphcore IPU processors can "
                    "speed up algorithmic trading by handling large amounts of data. For telecommunications, "
                    "Graphcore can enable new applications to utilise 5G technology. Website: "
                    "https://www.graphcore.ai/",
        launch_year=2016,
        valuation=2000,
        revenue=7,
        personal_opinion="Graphcore is now at a stage where it's looking to IPO soon. Its main competitor is Nvidia "
                         "and considering the market share Nvidia has on AI chips, Graphcore has a major challenge on "
                         "its hands. The UK tech scene is a booming sector with great chip manufacturers like ARM "
                         "holdings however, now that Nvidia is taking over ARM holdings there may be reduced "
                         "partnerships between the company. Despite the major challenge of Nvidia, Graphcore is still "
                         "a great company and one that would be instrumental for the future. As the world is "
                         "currently suffering from a chip shortage at this time in 2021, Graphcore can help "
                         "revolutionise an industry dominated by Nvidia. More companies are now looking for "
                         "alternative chip manufacturers so it's no surprise that Graphcore is backed by Microsft, "
                         "Samsung and BMW. "
    )
