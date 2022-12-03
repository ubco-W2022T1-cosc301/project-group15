# Group 15 Final Report

## Introduction (+!-!+Incomplete+!-!+)
Our group decided to perform an analysis on video game data because 

The dataset that we used is data from Steam, a popular online game store. The dataset includes information such as pricing, genre, release date, tags (which includes information on what features the game implements and/or type of game that it is), developer, publisher, languages, achievements, and much more. We obtained this data from Kaggle, an online database that hosts datasets. This data is under the CC0 (public domain) Licence and originally contained over 40 thousand steam games. The data was originally collected in the middle of 2019.

## Explorative Data Analysis (+!-!+Incomplete+!-!+)
Our group's EDA mostly consisted of looking at the data manually and figuring out what we can clean up had wrangle in our data pipeline. This was due to the dataset we chose containing a lot of text that needed to be separated out into numerical and boolean values before they can be put into use for the analysis.

For example, we separated out the year from the release date and converted it into a numerical value. We also separated out the tags into individual columns and converted them into boolean values. This was done so that we can use the data for our analysis.

In part 2 of the analysis, we also wrote functions to further separate and wrangle large amounts of data which were all crammed into individual cells in the original dataset. The game tags and language columns were the most difficult to wrangle because they contained a lot of data in the form of text.

## Analysis - Part 1
In this part of the data analysis, I attempted to answer some questions on game trends over time. Such as how the game's prices changed, how many games were developed, did more or less games implement online functionalities such as online multiplayer, and did more or less game developers add achievements to their games.

Since the data was originally collected in the middle of 2019, there were a lot of games which were pending release that was not yet added to this dataset, so I decided to cut out all entries from 2019 and onward and only left the years which had a complete list of games.

The dataset also contained a lot of text and missing information. So after filtering out useless columns and rows, I was left with around 2000 entries of good data.
Plotting various values from the filtered data against the release year, we can see some interesting trends in the fields of average price, online multiplayer implementation, games released each year, and achievement implementation.

### Image 1
On the first graph, which is the number of games released each year, we can see that the graph follows an exponential curve. This follows the development trend of technology over those years and from this graph, we can see that the cleaned and wrangled dataset appears to be accurate enough for use in this data analysis.

<img src="images\Final Report Images\Edwin\Games released per year.png">

### Image 2
The second graph that you can see here shows the number of games that implemented online multiplayer over the years. I filtered the tags in the original dataset and marked games which had a tag of both "online" and "multiplayer" to be ones that implemented online multiplayer. We can see from this graph that there were some games which implemented online multiplayer before 2010, but the 2010's are where online multiplayer games really took off. After a bit of searching, I found that just before 2010 is where there was a massive boom in streaming services. Netflix, Hulu, and Amazon Prime Video launched streaming services in 2007, 2008, and 2006 respectively. This boom in streaming services, and the rise of internet connected entertainment in general seems to have kickstarted many developers to start implementing online multiplayer into their games.

<img src="images\Final Report Images\Edwin\Multiplayer games per year.png">

### Image 3
In the third graph, I plotted the average prices of the games and the consumer price index. From here, we can see that despite games becoming more and more complicated and taking more and more money to produce, the average price of games follows closely with the consumer price index. Every 10 points that the consumer price index rises corresponds to about a dollar of the average game price rising. This phenomenon where the average game price follows this closely with the CPI indicates that the gaming industry grew at a steady pace and didn't experience any major disruptions.

<img src="images\Final Report Images\Edwin\Avg price per year vs CPI.png">

### Image 4
The last graph that I have plotted is the number of games that implemented achievements, and the number of achievements in the game year over year. We can see from this graph that a lot more developers have started to implement achievements into their games but there are not that many games that have a huge number of achievements. This graph suggests to me that having an achievement system boosts either the popularity, rating, or money earned by the game. But we can also see that the number of achievements implemented per game remains relatively steady, with most games implementing a maximum of around 150 achievements. This might be because that there is diminishing returns with implementing more achievements into the game so the developers don't bother with it.

<img src="images\Final Report Images\Edwin\Achievement implementation.png">

### Analysis - Part 1 conclusion
From these graphs, we can see how the number of games released matches with the rate of historical technological development, how the rise of internet entertainment has caused developers to make more online games, how prices of games have changed over time while closely following the consumer price index, and how developers have implemented achievements in their games.

## Analysis - Part 2
In the 2nd part of data analysis, I will analysis how many games are in different types of unique genre and game tags with different available languages in games on steam platform in between 1990 to 2018.

There are a lot incomplete and missing data in the dataset. Therefore, after filtering out missing value from columns and rows in the dataset, some data in the graph will show lesser than expected (around 2500 rows of complete data).

### Image 1
On the first graph shows the number of different types of available languages in games from 1990 to 2018. There are 33 different languages available in games on steam platform. We can see that highest used language is English in steam games which it is available in 219 different games. Along with the second highest used language is German in steam games which it is available in 90 different games.

<img src="images\Final Report Images\Adrian\Language.png">

### Image 2
On the second graph shows the number of different types of available languages in games from in year 2018. There are 32 different languages available in games on steam platform in year 2018. We can see that highest used language is Portuguese in steam games in year 2018, and it is available in 5 different games. Along with the second highest used language are Polish and Traditional Chinese which it is available in 4 different steam games in year 2018.

<img src="images\Final Report Images\Adrian\Language2018.png">

### Analysis - Part 2 Language conclusion
From the result of graphs above, we can see that English is the main language that is used in games. In Year 2018, Portuguese language are available in most games on steam platform.

### Image 3
On the third graph shows the number of different types of genre from 1990 to 2018. There are 18 different types of genre on steam platform. We can see that Indie type is the most used genre tag in steam games, and it is in 107 different games. Along with the second highest used genre tag is Action type, and it is in 101 different types of games.

<img src="images\Final Report Images\Adrian\Genre.png">

### Image 4
On the forth graph shows the number of different types of genre from in year 2018. There are 15 different types of genre on steam platform in year 2018. We can see that Indie, RPG, Sports, and Casual type are the highest used genre tags in steam games in year 2018, and it is in 3 different games in each of genre tag. Along with the second highest used genre tags are Racing, Early Access, Simulation and Strategy type, and it is in 2 different types of games in each of genre in year 2018.

<img src="images\Final Report Images\Adrian\Genre2018.png">

### Image 5
On the fifth graph shows the number of unique types of game tags from 1990 to 2018. The data in the graph is quite a lot is because there are 247 unique game tags collected from the filtered dataset. We can see that Indie type is the highest used genre tag in steam games, and it is in 119 different games. Along with the second highest used game tag Action type, and it is in 112 different types of games.

<img src="images\Final Report Images\Adrian\GameTag.png">

### Image 6
On the sixth graph shows the number of unique types of game tags from in year 2018. The data in the graph is still quite a lot is because there are 235 unique game tags collected from the filtered dataset in year 2018. We can see that Great Soundtrack type are the most used game tags in steam games in year 2018, and it is in 4 different games. Along with the second most used game tags are Singleplayer, Indie, RPG, Family Friendly, Casual, Replay Value, Sports, Historical, Local Multiplayer, Hidden Object, and it is in 3 different types of games in each of game tags in year 2018.

<img src="images\Final Report Images\Adrian\GameTag2018.png">

### Analysis - Part 2 Genre and Game Tags conclusion
From the result of graphs above, we can see the highest used types of genre and games tags in games on steam are Indie or Action type of games from 1990 to 2018. In year 2018, the result of genre tags are in most games on steam are Indie, RPG, Sports and Casual. However, the result of game tags on steam are in most games is Great Soundtrack type of games.


## Analysis - Part 3
In this part, I am checking how the recent review have an influence on the overall percent rating of different game as well as which game has the highest recent review for different rating categories such as very positive review game, mixed review game and negative review game.

The data was cleaned to drop off any columns that is not necessary for comparison and there is splitting of columns into different small columns respectively since review column has a lot of information which includes number of users, percentage of users that rate the game positive as well as the overall review of the game. Since the review column have different writing format, rows are dropped that have very little information as well as null rows so that comparison will be much easier. Sorting is also done in descending order in order to draw the graph for the game that have a highest recent positive reviews.

### Image 1
<img src= "images\Final Report Images\Sitt Hmue Paing\Very Positive reviews game.png">
<img src= "images\Final Report Images\Sitt Hmue Paing\Highest recent review for very positive games.png">

The bar graphs shows the comparison between recent and overall users review percentage on very positive rated game. All the rating in the graph both recent and overall only consist of positive review and as we can see there are some variation in the graph as the overall percentage increase/decrease or no change. The increases in overall percentage clearly tell us that there is a rise in recent positive review which in turn increase the growth of overall positive review. For decrease positive review, there may be reasons like the number of negative reviews exceeded that of the number of positive review from the user hence it will dropped the overall positive percent review. For no change graph, we can say that both the negative rating and the positive rating from the users are equal so there will be no further changes on the overall reviews. It shows that the change in recent positive review influence the change in overall positive reviews. The game get the overall rating of very positive since the positive user from both current and previous number greatly out weight the number of negative rating from different users from previous or current.

The second graph above clearly shows that Counter-Strike game has the highest positive users rating in very positive review categories, followed by Rainbow Six Siege and Team Fortress 2.

### Image 2
<img src= "images\Final Report Images\Sitt Hmue Paing\Mixed review game.png">
<img src= "images\Final Report Images\Sitt Hmue Paing\Highest recent review for very positive games.png">


One comparison bar graph done previous between the recent and overall percentage review which is focussing on very positive review game is not enough to convince that the same thing apply for the other game that have different rating like mixed and negative reviews. Here is the second graph focussing on mixed reviewed game. The same as the previous comparison bar graph there is a increase/decrease or no change in overall rating. We can say that the change in recent percent review affected the overall percent review for the mixed reviewed game as well. The games are in mixed categories since negative reviews made by different users outnumbered the number of positive reviews from both current and previous user. Another reason for increase in negative review can be because of new updates made on the game. New updates can have pros and cons which also depends on the user's taste. Since there is more recent negative percentage review on the updates of the game that in turn affect the overall percentage review dropped gradually or drastically. 

The second graph above clearly shows that Playerunknown's battlegrounds has the highest positive recent users in mixed review categories, followed by KurtzPel and Battalion 1944.

### Image 3
<img src= "images\Final Report Images\Sitt Hmue Paing\Negative review game.png">
<img src= "images\Final Report Images\Sitt Hmue Paing\Highest recent review for negative games.png">

We can see from the above graph that the overall the change in recent percentage review can affect the overall percentage review. The first game has no recent review so the overall percentage rating remain unchanged but for the other games on the graph, we can clearly see that there is the change in overall review due to the change in recent review. The game can be in very negative categories because it does not suit most of the players taste as well as game update can further cause more issues rather than making the game better than the previous versions. The game are in the very negative categories because the users that rated the game as negative greatly out weight the number of  from both current/previous users that rated the game as positive.

Based on the second graph shown above we can see that Command & Conquer 4: Tiberian Twilight has the highest positive review in negative review categories from the users followed by Flatout 3: Chaos & Destruction and Spacebase DF-9.

## Conclusion (+!-!+Incomplete+!-!+)