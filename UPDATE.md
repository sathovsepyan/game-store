## Project update February 2019

![](/static/gameshop_snapshot.jpg)

#### Outline

1. Member names and student IDs
1. Features implemented, self-grading, comments.
1. Team assignation.
1. Instructions on how to use the application.

#### 1. Member names and student IDs

* Timur Kartaev, Student ID:  727642
* Satenik Hovsepyan, Student ID: 727561
* Bruno Duarte, Student ID: 727396

#### 2. Features implemented, self-grading, comments

<table>
  <tr>
    <th> 
      Authentication (mandatory, 100-200 points):
    </th>
    <th> 
      Self-grading: 200 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Log in, log out, and register (both as player or developer)</li>
        <li>Email validation</li>
        <li>Use Django auth</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: We used Django's Authentication system (django.contrib.auth) with it's User model, as well as, 
    extended it with Profile model to represent Developers/Players. 
  </td>
</table>

<table>
  <tr>
    <th>
      Basic player functionalities (mandatory, 100-300 points):
    </th>
    <th> 
      Self-grading: 300 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Buy games</li>
        <li>Play games</li>
        <li>Security restrictions, e.g. player is only allowed to play the games they’ve purchased</li>
        <li>Search functionality</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: Playing the game snake was a problem because it needs the input from the keyboard, and when the webpage is loaded, doesn't have the focus. We force with JavaScript to catch the focus of the Iframe after the webpage was loaded.
  </td>
</table>

<table>
  <tr>
    <th>
      Basic developer functionalities (mandatory, 100-200 points):
    </th>
    <th> 
      Self-grading: 200 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Add a game</li>
        <li>Basic game inventory and sales statistics</li>
        <li>Security restrictions, e.g. developers are only allowed to modify/add/etc. their own games, developer can only add games to their own inventory</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: In general, all good.
  </td>
</table>

<table>
  <tr>
    <th>
      Game/service interaction (mandatory 100-200 points):
    </th>
    <th> 
      Self-grading: 200 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Save the current score of the user.</li>
        <li>Update the global high score list.
</li>
        <li>Update high score of the game.</li>
        <li>Messages between the store and the game</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: Updating the score was not a big problem as trying to show the scores, because it needs to be aggreated (MAX() and Group BY in SQL), we dive in the use of overriding templates and methods from the inner Django framework as get_context_data() and get_queryset() as well as the feature of using aggregation within the ORM of Django.
  </td>
</table>


<table>
  <tr>
    <th>
      Quality of Work (mandatory 0-100 points)
    </th>
    <th> 
      Self-grading: 100 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Quality of code</li>
        <li>Purposeful use of the framework</li>
        <li>User experience</li>
        <li>Meaningful testing</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: We separated all apps of Django and put them under a general app folder. Instead of defining methods alone in the views, sometimes depending of the case we use classes that inherits from TemplateView or ListView.
  </td>
</table>



<table>
  <tr>
    <th>
      Non-functional requirements (mandatory 0-200 points)
    </th>
    <th> 
      Self-grading: 200 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Project plan</li>
        <li>Overall documentation, demo, teamwork, and project management</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: We try to stick to the plan, but mainly we attack the requirements by features. A lot of communication and peer-feedback over each attempt. We believe we balance the job very well!
  </td>
</table>


<table>
  <tr>
    <th>
      Save/load and resolution feature (0-100 points)
    </th>
    <th> 
      Self-grading: 100 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>The service supports saving and loading for games with the simple message protocol </li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: All good, just a few more listeners were needed to communicate from the Store to the game and that was it.
  </td>
</table>


<table>
  <tr>
    <th>
      Own game (0-100 points)
    </th>
    <th> 
      Self-grading: 100 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Develop a simple game in JavaScript that communicates with the service</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: We adapt a snake game with the message protocol, the hard part was to make it visible the variables of the state of the game as well as restoring the game, but all good at the end.
  </td>
</table>

<table>
  <tr>
    <th>
      Mobile Friendly (0-50 points)
    </th>
    <th> 
      Self-grading: 50 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>It works with devices with varying screen width and is usable with touch-based devices</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: Bootstrap did the job!
  </td>
</table>

<table>
  <tr>
    <th>
      Social media sharing (0-50 points)
    </th>
    <th> 
      Self-grading: 50 points
    </th>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Enable sharing games in some social media site (Facebook, Twitter, Google+, etc.)</li>
      </ul>
    </td>
  </tr>
  <td colspan="2">
    Comments: Generating the metadata dynamically was a challenge because the host should be included in the path in order for the social service fetch the image. After researching a bit we found request.build_absolute_uri and request.get_host that did the job.
  </td>
</table>


#### 3. Team assignation

* Timur Kartaev: 
    * Design of models, Sign-up of users and developers, Upload games to store, Security for unauthorized access, Sales statistics, Searching of games backend
* Satenik Hovsepyan:
    * Payment gateway, Purchased games by user, Aesthetic for the front-end, Search games in the store front-end, Mobile friendly feature
* Bruno Duarte:
    * Message Protocol, Creation of a new game, Aggregation of scores, Playing a game, Saving and loading games from database, Social media sharing.
    
#### 4. Instructions on how to use the application

Go to: https://wsd-project-007.herokuapp.com/

Sign-up as a Developer and create some games.

In order to test our own game, please create a game with https://wsd-project-007.herokuapp.com/static/snake.html as the URL. 

Then, you should sign-up another account as a Player.

Buy some games as a Player, and start having fun!

