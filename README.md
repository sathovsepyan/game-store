###### CS-C3170 - Web Software Development

# WSD Autum 2018 Project - Game Store

Members: _Timur Kartaev, Satenik Hovsepyan, Bruno Duarte_

## Overview

##### Features to implement

1. TODO
1. TODO
1. 

##### Brief explanation on how to implement the previous features

1. TODO
1. TODO
1. 

##### Extra features to implement

1. TODO
1. TODO
1. 

##### Brief explanation on how to implement the previous features

1. TODO
1. TODO  
1. 

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
    
##### Views

 * TODO


## Planification

#### Strategy on the group for getting things done

1. We plan to have regular meetings, at least once a week to split tasks and assign features.
1. We would use GDrive for collaborative common documents and to eventually use them as a reference in our day-to-day tasks.
1. We would use Aalto Gitlab to keep track of our project and source code.

#### Implementation order and timetable (draft)

 * TODO

##### Timetable (draft)
 
<table>
  <tr>
    <td> Column 1 </td>
    <td> Column 2 </td>
    <td> Column 3 </td>
    <td> Column 4 </td>
    <td> Column 5 </td>
    <td> Column 6 </td>
  </tr>
  <tr>
    <td> Column 1 </td>
    <td> Column 2 </td>
    <td> Column 3 </td>
    <td> Column 4 </td>
    <td> Column 5 </td>
    <td> Column 6 </td>
  </tr>
  <tr>
    <td> Column 1 </td>
    <td> Column 2 </td>
    <td> Column 3 </td>
    <td> Column 4 </td>
    <td> Column 5 </td>
    <td> Column 6 </td>
  </tr>
</table>