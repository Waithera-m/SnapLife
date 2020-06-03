# SnapLife
#### The web site allows users to create profiles and upload images
#### By **Waithera-m**
## Description
SnapLife is a django application that allows users to create profiles, upload images, like and comment on images, and follow other users.
## Setup/Installation Requirements
To use the application, users need internet access and web browsers, preferably  Chrome, Safari, and Firefox.
## Set-Up a Local Project
* Fork the repository
* Clone the repository
    ```$ git clone  https://github.com/Waithera-m/SnapLife.git```
* Activate a virtual environment
    ```$ python3.8 -m venv virtual```
* Install all prerequisites
    ```$ pip install -r requirements.txt```
* Create file to store sensitive environment variables 
## Known Bugs
* The copy button does not work; therefore users have to manually select and copy the image urls
## Behavior Driven Development (BDD)

#### Landing View
![image](https://user-images.githubusercontent.com/60571734/83613158-11271580-a58c-11ea-872f-fb8073b8465b.png)

#### Timeline View
![image](https://user-images.githubusercontent.com/60571734/83613394-6400cd00-a58c-11ea-925c-99346177ece7.png)
![image](https://user-images.githubusercontent.com/60571734/83613507-8d215d80-a58c-11ea-8001-a23a863b6e56.png)

#### Profile View
![image](https://user-images.githubusercontent.com/60571734/83613666-c6f26400-a58c-11ea-8de3-a97ae5b8b880.png)

#### User's Posts View
![image](https://user-images.githubusercontent.com/60571734/83554455-74c22c00-a515-11ea-91da-91f2a467abca.png)

#### Results Page
![image](https://user-images.githubusercontent.com/60571734/83555961-c8ce1000-a517-11ea-8bbd-a7a9acb94a08.png)


|Behavior                |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads |Users click on sign in or sign up link | If users are authenticated users they are logged in if users click on sign up link they are directed to registration form view |
|The landing page loads|Authenticated users who have profiles see their timelines new users see people they could follow and an option to  create profile | Autheticated users with profiles click on displayed posts and a modal pops up with the clicked images' details including like and comment links|
|The landing page loads|Users click on view profile link in card |Users are directed to the view page associated with the given profile|
|The profile page loads|Users click on posts link|Users see the posts created by the profile's owner|
|The landing/profile page loads|Users click on logout navbar link|Users are logged out and redirected to the login page|
## Technologies Used
* HTML - HTML was used to dictate the structure of views' templates.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Javascript - The high-level programming language was used to create a function to support the follow feature
* Python 3.8.2 - The language was used to create classes, testcases, and functions to retrieve data 
* [django 3.0.6](https://www.djangoproject.com/) - django is a Python web framework.The framework's apps, urls, and views were used to refactor code and promote code maintenance. Inbuilt filters,classes, and methods were used to initialize the created app and installed extensions and loop through and display saved images and navigate to different views. 
## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creator via this email address: njihiamary11@gmail.com
## Demo
You can view changes made to the website by visiting this working live demo: https://snaplife.herokuapp.com/accounts/login/?next=/
### License
*MIT*
MIT License Copyright (c) 2020 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) 2020 **Waithera-m**