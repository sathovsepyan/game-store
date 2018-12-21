###### CS-C3170 - Web Software Development

# WSD Autum 2018 Project - Game Store

Members: 
  *  Timur Kartaev 727642
  *  Satenik Hovsepyan 727561
  *  Bruno Duarte 727396

## Overview

##### Features to implement

1. Authentication
1. Basic player functionalities 
1. Basic developer functionalities
1. Game/service interaction
1. Quality of Work
1. Non-functional requirements

##### Brief explanation on how to implement the previous features

1. Register, login and reset the password is already implemented in Django and we just plan to use them.
1. We are going to create models to represent the games, purchases, and the search feature and also built in constraints on what each user can play according their purchases.
1. We are going to create a model "profile" to represent Developers and they can add or remove games from their shelf.
1. We are going to use the API of the browser called "messages" to capture the data sent between the iframes.
1. All code is going to be documented and separeted in files to accordingly apply the DRY paradigm.

##### Extra features to implement

1. Mobile Friendly
1. Social media sharing
1. RESTful API 
1. 3rd party login
1. Save/load and resolution feature 
1. Own game

##### Brief explanation on how to implement the previous features

1. We plan to use bootstrap for the mobile friendly components
1. We plan to use OpenGraph.  
1. Different views for providing the REST service.
1. We are going to use the third party app (python-auth) for Social Media login
1. We are going to store the state of the game in a model
1. We are going to develop a very basic game of guessing cards/values.

*Note*: We plan to start implementing extra features in aforementioned order and implement as many of them as we have time for using our best effort.

## Models and views needed (draft)

##### Models

 * Profile
    * role = CharField
    * games = ManyToMany(Game)
 * Category
    * title = CharField 
    * slug = SlugField
 * Game
    * title = CharField
    * url = URLField
    * price = PositiveInegerField 
    * category = ForeignKey(Category) 
    * developer = ForeignKey(User) 
    * status = CharField
    * is_deleted = BooleanField
 * Order
    * code = UUID4Field
    * user = ForeignKey(User) 
    * cart = ForeignKey(Cart) 
    * status = CharField
    * total_amount = PositiveIntegerField
 * Cart
    * user = ForeignKey(User) 
    * status = CharField 
    * created = DateTimeField
 * OrderItem
    * game = ForeignKey(Game) 
    * cart = ForeignKey(Cart) 
    * price = PositiveIntegerField
    * amount = PositiveIntegerField
 * Payments
    * order = ForeignKey(Order) 
    * status = CharField
 * GameScore
    * game = ForeignKey(Game) 
    * user = ForeignKey(User) 
    * score = IntegerField
 * GameState
    * game = ForeignKey(Game)
    * user = ForeignKey(User)
    * state = JSONField
    * saved = DateTimeField

##### Views


##### Authentication
* LoginView
* RegisterView
* PasswordResetView

##### Basic player functionalities
* GameListView
* CartView
* CheckOutView
* OrderFinishedView
* ProfileView
* GamePlayView

##### Basic developer functionalities
* CreateGameView
* EditGameView
* RemoveGameView
* GameListView
* SaleStatisticsView

##### Game/service interaction
* SaveUserScoreView
* ScoreDashboardView

##### RESTful API
* GameListView
* HighScoresView
* StatisticsView








## Planification

#### Strategy on the group for getting things done

1. We plan to have regular meetings, at least once a week to split tasks and assign features.
1. We would use GDrive for collaborative common documents and to eventually use them as a reference in our day-to-day tasks.
1. We would use Aalto Gitlab to keep track of our project and source code.

#### Implementation order and timetable (draft)

 * Week 0 is the week 52 from 2018
 * Week 1 corresponds to the week 1 from 2019

##### Timetable (draft)
 
###### Week 0 is the week 52 from 2018, Week 1 corresponds to the week 1 from 2019
 
<table>
		<tr>
		   <th colspan="2"> Week and Dates </th>
		   <th> Tasks </th>
		</tr>
		<tr>
		   <td> Week 0 </td>
		   <td> 24-30.12 </td>
		   <td>
			  <ul>
				 <li>Models creation</li>
				 <li>Testing initial deployment to Heroku</li>
			  </ul>
		   </td>
		</tr>
		<tr>
		   <td> Week 1 </td>
		   <td> 01-06.01 </td>
		   <td>
			  <ul>
				 <li>Authentication, register as a player and developer with email confirmation and reset password </li>
			  </ul>
		   </td>
		</tr>
		<tr>
		   <td> Week 2 </td>
		   <td> 07-13.01 </td>
		   <td>
			  <ul>
			  <li>  
				 Browse of games, the store itself where the games can be bought. 
			  </li>
			  <li>  Including the search of games, and games should have a category.</li>
			  <li> 
				 Inventory of games acquired by a given player
			  </li>
		   </td>
		</tr>
		<tr>
		   <td> Week 3 </td>
		   <td> 14-20.01 </td>
		   <td>
			  <ul>
				 <li>Display the highscores of a given game. </li>
				 <li> 
					Buy games through the payment gateway.
				 </li>
			  </ul>
		   </td>
		</tr>
		<tr>
		   <td> Week 4 </td>
		   <td> 21-27.01 </td>
		   <td>
			  <ul>
				 <li>The view for playing the game, and actually play the game. </li>
				 <li>
					Add and remove games to the store, modify price, and other details.
				 </li>
				 <li> 
					Sales statistics, visualization for that developer.
				 </li>
				 <li>Partial deployment to Heroku</li>
			  </ul>
		   </td>
		</tr>
		<tr>
		   <td> Week 5 </td>
		   <td> 28-31.01 </td>
		   <td>
			  <ul>
				 <li>Message service between the game and the store, user related saved games.</li>
				 <li> 
					Saving the state of a given game for a given player.
				 </li>
				 <li> 
					Loading the state of a given game for a given player.
				 </li>
			  </ul>
		   </td>
		</tr>
		<tr>
		   <td> Week 6 </td>
		   <td> 04-10.02 </td>
		   <td>
			  <ul>
				 <li>Adding the RESTful capabilities to the existing models.</li>
				 <li> Implementation of sharing through social media.</li>
				 <li> Creation of a self-made game to deploy to the Store.</li>
			  </ul>
		   </td>
		</tr>
		<tr>
		   <td> Week 7 </td>
		   <td> 11-17.02 </td>
		   <td>
			  <ul>
				 <li> Bug fixes</li>
			  </ul>
		   </td>
		</tr>
		<tr>
		   <td> Week 8 </td>
		   <td> 18-19.02 </td>
		   <td>
			  <ul>
				 <li>Documentation.</li>
				 <li>Final deployment and delivery to Heroku.</li>
			  </ul>
		   </td>
		</tr>
</table>