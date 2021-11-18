# Straight Talk
#### By Mary Njenga, Nancy Murithi, Robbin Mwangi, Brain Cheruiyot, Alphone Kipngeno, Ali Hassan
## Table of Content
+ [Description](#description)
+ [Installation Requirement](#Installation)
+ [Behaviour Driven Development](#Behaviour-Driven-Development)
+ [Technology Used](#technology-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

****
## Description 
- This is a for blogging website where you can create and share your opinions and other users can read and comment on them.

## User Story in Pictures
####  User view
* User can view the blog posts on the site
* User can view the most recent posts
* User can subscribe to blog mailing list and receives an email alert when a new post is made.
* User can comment on blog posts

## Site image
![Site Image](app/static/photos/site.png)

## Live link
`https://straighttalk.herokuapp.com/`
## Installation
### Requirements
* python3.6
* pip 

### Installation process
* Open terminal
* run `git clone https://github.com/Nancy-codergirl/Straight-talk-blog.git`

### Dependancy Installation process
```
$ pip install -r requirements.txt

```

### Running the Application
To view the website run the command
```
$ chmod a+x start.sh
$ ./start.sh

```
To run the tests run the command
```
$ python3.6 manage.py test

```
## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|  Form validation    | User submits empty or invalid data on form | An error is message is displayed    |
|  Sign up   | User enters a input for all fields and submits    | User is redirected to log in page|
|  Log in   | User enters valid details  | User is logged in and redirected to main page|
|  New Blog   | User enters submits a new Blog  | Blog is added to list |
|  Comment   | User clicks on comment link | All comments are displayed and user can submit a new comment|
|  Profile   | User clicks on account link | Account details and posts made by the user are displayed |
|  Log out   | User logs out |Redirected to main page and a message shown |

****

[Go Back to the top](#Straight-Talk)
## Technology Used
* Python
* Html
* css

****
[Go Back to the top](#Straight-Talk)
## Licence
MIT License

Copyright (c) 2021

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


****
[Go Back to the top](#Straight-Talk)
## Authors Info
* Email - [Mary Njenga](mary.njenga@student.moringaschool.com)
* Email - [Robbin Mwangi](robbin.githimbo@student.moringaschool.com)
* Email - [Nancy Murithi](nancy.murithi@student.moringaschool.com)
* Email - [Alphones Kipnengo](alphones.kipngeno@student.moringaschool.com)
* Email - [Ali Hassan](mary.njenga@student.moringaschool.com)
* Email - [Brain Cheruiyot](brain.cheruiyot@student.moringaschool.com)

[Go Back to the top](#Straight-Talk)
